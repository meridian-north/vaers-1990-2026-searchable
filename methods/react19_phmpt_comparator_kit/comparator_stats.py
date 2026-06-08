#!/usr/bin/env python3
"""
comparator_stats.py — turn raw rate ratios into properly-bounded leads.

Post-processes a phmpt_arm_join comparator JSON: for every 2x2 (vaccine vs placebo,
serious vs not) it computes the risk ratio with a 95% CI (log method,
Haldane-Anscombe 0.5 correction for zero cells), a Fisher exact two-sided p-value
(lgamma hypergeometric — exact, no scipy), and then screens the whole FAMILY of
comparisons for multiplicity with Benjamini-Hochberg FDR and Bonferroni. A lead
"survives" only if its FDR q-value < 0.05 AND its CI excludes 1.0.

This is the rigor gate: with ~25 unadjusted comparisons and small counts, most
elevated ratios are noise. After this, each cell carries its uncertainty, and the
honest verdict is usually "no comparison survives" — properly-bounded leads, not
signals.

  python3 comparator_stats.py --in /tmp/phmpt_comparator.json --out /tmp/phmpt_stats.json

stdlib only (math). Deterministic. Leads, not verdicts.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

Z95 = 1.959963984540054


def rr_ci(a: int, n1: int, c: int, n2: int):
    """Risk ratio (a/n1)/(c/n2) with 95% CI (log method). Haldane-Anscombe +0.5
    on a zero numerator cell so the ratio/CI stay defined."""
    aa, cc, nn1, nn2 = a, c, n1, n2
    if a == 0 or c == 0:
        aa, cc = a + 0.5, c + 0.5
        nn1, nn2 = n1 + 1, n2 + 1
    if nn1 == 0 or nn2 == 0 or cc == 0:
        return None, None, None
    r1, r2 = aa / nn1, cc / nn2
    if r2 == 0:
        return None, None, None
    rr = r1 / r2
    # SE of ln(RR) for risk ratio
    try:
        se = math.sqrt(1.0 / aa - 1.0 / nn1 + 1.0 / cc - 1.0 / nn2)
    except ValueError:
        return rr, None, None
    return rr, rr * math.exp(-Z95 * se), rr * math.exp(Z95 * se)


def _lhyper(a, b, c, d):
    n = a + b + c + d
    return (math.lgamma(a + b + 1) + math.lgamma(c + d + 1) +
            math.lgamma(a + c + 1) + math.lgamma(b + d + 1) -
            math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(c + 1) -
            math.lgamma(d + 1) - math.lgamma(n + 1))


def fisher_2sided(a: int, b: int, c: int, d: int) -> float:
    """Fisher exact two-sided p for 2x2 [[a,b],[c,d]] via lgamma hypergeometric.
    Sums probabilities of all tables (fixed margins) no more likely than observed."""
    r1, r2, c1 = a + b, c + d, a + c
    p_obs = _lhyper(a, b, c, d)
    lo, hi = max(0, c1 - r2), min(r1, c1)
    tot = 0.0
    for ap in range(lo, hi + 1):
        bp, cp = r1 - ap, c1 - ap
        dp = r2 - cp
        lp = _lhyper(ap, bp, cp, dp)
        if lp <= p_obs + 1e-9:
            tot += math.exp(lp)
    return min(1.0, tot)


def bh_fdr(pvals: list) -> list:
    """Benjamini-Hochberg q-values, aligned to input order."""
    m = len(pvals)
    order = sorted(range(m), key=lambda i: pvals[i])
    q = [1.0] * m
    prev = 1.0
    for rank in range(m, 0, -1):           # largest p first
        idx = order[rank - 1]
        val = min(prev, pvals[idx] * m / rank)
        q[idx] = val
        prev = val
    return q


def cell(label: str, a: int, n1: int, c: int, n2: int) -> dict:
    b, d = n1 - a, n2 - c
    rr, lo, hi = rr_ci(a, n1, c, n2)
    p = fisher_2sided(a, b, c, d)
    return {"label": label, "vaccine_serious": a, "vaccine_n": n1,
            "placebo_serious": c, "placebo_n": n2,
            "rr": round(rr, 3) if rr else None,
            "ci95": [round(lo, 3), round(hi, 3)] if lo else None,
            "fisher_p": round(p, 4), "ci_excludes_1": (lo is not None and (lo > 1 or hi < 1))}


def analyze(comp: dict) -> dict:
    nv = comp["arms"].get("vaccine", {}).get("subjects_randomized", 0)
    npl = comp["arms"].get("placebo", {}).get("subjects_randomized", 0)
    cells = []
    av = comp["arms"].get("vaccine", {}).get("subjects_with_serious_ae", 0)
    ap = comp["arms"].get("placebo", {}).get("subjects_with_serious_ae", 0)
    cells.append(cell("OVERALL", av, nv, ap, npl))
    for s in comp.get("by_soc", []):
        cells.append(cell("SOC:" + s["soc"], s["vaccine_serious_subj"], nv,
                          s["placebo_serious_subj"], npl))
    for k, r in comp.get("by_age", {}).items():
        if r["vaccine"]["n"] or r["placebo"]["n"]:
            cells.append(cell("AGE:" + k, r["vaccine"]["serious_subj"], r["vaccine"]["n"],
                              r["placebo"]["serious_subj"], r["placebo"]["n"]))
    for k, r in comp.get("by_sex", {}).items():
        if r["vaccine"]["n"] or r["placebo"]["n"]:
            cells.append(cell("SEX:" + k, r["vaccine"]["serious_subj"], r["vaccine"]["n"],
                              r["placebo"]["serious_subj"], r["placebo"]["n"]))
    pv = [c["fisher_p"] for c in cells]
    q = bh_fdr(pv)
    m = len(cells)
    for i, c in enumerate(cells):
        c["fdr_q"] = round(q[i], 4)
        c["bonferroni_p"] = round(min(1.0, c["fisher_p"] * m), 4)
        c["survives"] = bool(c["fdr_q"] < 0.05 and c["ci_excludes_1"])
    survivors = [c["label"] for c in cells if c["survives"]]
    return {"schema": "garrison/comparator_stats/v1",
            "trial": comp.get("trial"), "arm_field": comp.get("arm_field"),
            "comparisons": m, "alpha": 0.05,
            "method": "RR log-CI (Haldane), Fisher exact 2-sided, BH-FDR + Bonferroni",
            "survivors_after_fdr": survivors,
            "cells": cells,
            "interpretation": ("No comparison survives multiplicity adjustment with a "
                               "CI excluding 1.0 — properly-bounded leads, not signals."
                               if not survivors else
                               f"{len(survivors)} comparison(s) survive FDR with CI "
                               "excluding 1.0 — still leads; require replication + "
                               "per-PT + time-to-onset before any inference."),
            "stance": "question_no_conclusion"}


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    comp = json.loads(Path(args.inp).read_text())
    rep = analyze(comp)
    print(f"\n{'='*78}\n  COMPARATOR STATS — {rep['trial']} ({rep['arm_field']}), "
          f"{rep['comparisons']} comparisons, BH-FDR\n{'='*78}")
    print(f"  {'cell':42s} {'RR':>5} {'95% CI':>15} {'p':>7} {'q(FDR)':>7} surv")
    for c in sorted(rep["cells"], key=lambda x: x["fisher_p"]):
        ci = f"[{c['ci95'][0]},{c['ci95'][1]}]" if c["ci95"] else "NA"
        print(f"  {c['label'][:42]:42s} {str(c['rr']):>5} {ci:>15} {c['fisher_p']:>7} "
              f"{c['fdr_q']:>7} {'YES' if c['survives'] else '-'}")
    print(f"\n  survivors after FDR (CI excludes 1.0): {rep['survivors_after_fdr'] or 'NONE'}")
    print(f"  → {rep['interpretation']}\n{'='*78}")
    if args.out:
        Path(args.out).write_text(json.dumps(rep, indent=2))
        print(f"  → {args.out}")
    return 0


if __name__ == "__main__":
    # quick self-test of the stats on a known 2x2 before any real use
    if len(sys.argv) == 1:
        # classic: a=10/100 vs c=20/100 → RR 0.5
        rr, lo, hi = rr_ci(10, 100, 20, 100)
        assert abs(rr - 0.5) < 1e-9, rr
        # Fisher on [[10,90],[20,80]] ~ p≈0.07; sanity range
        p = fisher_2sided(10, 90, 20, 80)
        assert 0.02 < p < 0.12, p
        q = bh_fdr([0.01, 0.04, 0.5, 0.5])
        assert q[0] <= q[1] <= 1.0
        print(f"self-test OK: RR=0.5 CI=[{lo:.3f},{hi:.3f}] fisher_p={p:.4f} bh ok")
        sys.exit(0)
    sys.exit(main(sys.argv[1:]))
