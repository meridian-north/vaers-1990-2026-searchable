#!/usr/bin/env python3
"""
phmpt_arm_join.py — PHMPT/C4591001 vaccine-vs-placebo comparator with a real
denominator.

PHMPT is the one corpus in the family that is a randomized trial: ADSL carries each
subject's arm AND the per-arm N (the denominator spontaneous systems lack). This
tool joins the adverse-event envelopes to the ADSL arm assignment on USUBJID and
reports, PER ARM: subjects, subjects with >=1 serious AE, and the serious-AE RATE
(serious_subjects / arm_N) — then the vaccine:placebo rate ratio.

  python3 phmpt_arm_join.py \
      --adsl '~/garrison/pharmacovigilance/phmpt_pfizer/envelopes_sdtm/adsl/*c4591001*adsl*.jsonl' \
      --ae   '~/garrison/pharmacovigilance/phmpt_pfizer/envelopes/*c4591001*adae*.jsonl' \
      --arm-field actarm --out /tmp/phmpt_comparator.json

Reads JSONL envelopes directly (the native form). Deterministic; no LLM.
Leads, not verdicts: a trial rate ratio is descriptive of THIS trial — not
real-world, not cross-bridgeable with spontaneous systems as if equivalent.
Stdlib + _iir_utils.canon_usubjid.
"""
from __future__ import annotations

import argparse
import glob as _glob
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _iir_utils import canon_usubjid
except Exception:                                   # pragma: no cover
    canon_usubjid = lambda s: " ".join(str(s or "").upper().split())

EXCLUDE_ARMS = {"screen failure", "not assigned", "none", "", "unknown"}


def canon_arm(arm: str) -> str:
    """Map an ADSL arm string to a comparison class. Phase-1 candidate arms are
    kept distinct (small; usually excluded from the Ph2/3 contrast)."""
    a = str(arm or "").strip().lower()
    if a in EXCLUDE_ARMS:
        return "excluded"
    if a.startswith("placebo"):
        return "placebo"
    if "bnt162b2" in a and "phase 1" not in a:
        return "vaccine"                            # BNT162b2 Ph2/3 (the authorized one)
    if "bnt162b2" in a:
        return "vaccine_ph1"
    if "bnt162b1" in a:
        return "candidate_bnt162b1"
    return "other"


def _ae_serious(what: dict) -> bool:
    def t(f):
        return str(what.get(f)).strip().lower() == "true"
    return (t("ae_serious") or t("outcome_hospitalized") or t("outcome_died")
            or t("outcome_disabled") or t("outcome_life_threatening"))


def _iter(paths):
    for p in paths:
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except (ValueError, json.JSONDecodeError):
                    continue


def _age_band(yrs) -> str:
    try:
        a = int(float(yrs))
    except (TypeError, ValueError):
        return "unknown"
    for lo, hi, lbl in [(0, 17, "0-17"), (18, 49, "18-49"), (50, 64, "50-64"), (65, 200, "65+")]:
        if lo <= a <= hi:
            return lbl
    return "unknown"


def build_arm_map(adsl_paths, arm_field="actarm"):
    """usubjid → {arm, age_band, sex}, plus per-arm and per-(arm,stratum) N."""
    subj = {}
    for o in _iter(adsl_paths):
        who = (o.get("five_w_one_h", {}) or {}).get("who", {}) or {}
        uid = canon_usubjid(who.get("usubjid"))
        if not uid:
            continue
        arm = who.get(arm_field) or who.get("arm") or who.get("actarm")
        sex = str(who.get("sex") or "").strip().upper()[:1] or "U"
        subj[uid] = {"arm": canon_arm(arm),
                     "age": _age_band(who.get("age_yrs") or who.get("age")),
                     "sex": sex if sex in ("M", "F") else "U"}
    denom = defaultdict(int)
    denom_age = defaultdict(int)                     # (arm, age_band)
    denom_sex = defaultdict(int)                     # (arm, sex)
    for s in subj.values():
        denom[s["arm"]] += 1
        denom_age[(s["arm"], s["age"])] += 1
        denom_sex[(s["arm"], s["sex"])] += 1
    return subj, dict(denom), dict(denom_age), dict(denom_sex)


def _rr(v_rate, p_rate):
    return round(v_rate / p_rate, 3) if (v_rate is not None and p_rate) else None


def comparator(adsl_paths, ae_paths, arm_field="actarm", soc_top=15) -> dict:
    subj, denom, denom_age, denom_sex = build_arm_map(adsl_paths, arm_field)
    serious_subjects = defaultdict(set)             # arm → {uid with >=1 serious AE}
    any_ae_subjects = defaultdict(set)
    ae_total = defaultdict(int)
    ser_soc = defaultdict(set)                       # (arm, soc) → {uid}
    ser_age = defaultdict(set)                       # (arm, age_band) → {uid}
    ser_sex = defaultdict(set)                       # (arm, sex) → {uid}
    unmatched_ae = 0
    for o in _iter(ae_paths):
        w = o.get("five_w_one_h", {}) or {}
        uid = canon_usubjid((w.get("who", {}) or {}).get("trial_subject_id"))
        info = subj.get(uid)
        if info is None:
            unmatched_ae += 1
            continue
        cls = info["arm"]
        ae_total[cls] += 1
        any_ae_subjects[cls].add(uid)
        what = w.get("what", {}) or {}
        if _ae_serious(what):
            serious_subjects[cls].add(uid)
            soc = str(what.get("ae_meddra_soc") or "Unmapped").strip()
            ser_soc[(cls, soc)].add(uid)
            ser_age[(cls, info["age"])].add(uid)
            ser_sex[(cls, info["sex"])].add(uid)

    arms = {}
    for cls, n in sorted(denom.items(), key=lambda kv: -kv[1]):
        if cls == "excluded":
            continue
        ser = len(serious_subjects.get(cls, ()))
        arms[cls] = {
            "subjects_randomized": n,
            "subjects_with_any_ae": len(any_ae_subjects.get(cls, ())),
            "subjects_with_serious_ae": ser,
            "ae_records": ae_total.get(cls, 0),
            "serious_rate_per_subject": round(ser / n, 5) if n else None,
        }
    nv, npl = denom.get("vaccine", 0), denom.get("placebo", 0)
    rr = _rr(arms.get("vaccine", {}).get("serious_rate_per_subject"),
             arms.get("placebo", {}).get("serious_rate_per_subject"))

    # by-SOC serious rate ratio (vaccine vs placebo), top SOCs by combined serious
    socs = {s for (a, s) in ser_soc}
    by_soc = []
    for s in socs:
        vs, ps = len(ser_soc.get(("vaccine", s), ())), len(ser_soc.get(("placebo", s), ()))
        vr = vs / nv if nv else None
        pr = ps / npl if npl else None
        by_soc.append({"soc": s, "vaccine_serious_subj": vs, "placebo_serious_subj": ps,
                       "vaccine_rate": round(vr, 6) if vr is not None else None,
                       "placebo_rate": round(pr, 6) if pr is not None else None,
                       "rate_ratio": _rr(vr, pr)})
    by_soc.sort(key=lambda d: -(d["vaccine_serious_subj"] + d["placebo_serious_subj"]))
    by_soc = by_soc[:soc_top]

    def _strata(ser_map, denom_map, keys):
        out = {}
        for k in keys:
            row = {}
            for arm in ("vaccine", "placebo"):
                d = denom_map.get((arm, k), 0)
                s = len(ser_map.get((arm, k), ()))
                row[arm] = {"n": d, "serious_subj": s,
                            "rate": round(s / d, 5) if d else None}
            row["rate_ratio"] = _rr(row["vaccine"]["rate"], row["placebo"]["rate"])
            out[k] = row
        return out

    by_age = _strata(ser_age, denom_age, ["0-17", "18-49", "50-64", "65+", "unknown"])
    by_sex = _strata(ser_sex, denom_sex, ["M", "F", "U"])

    return {
        "schema": "garrison/phmpt_comparator/v1",
        "trial": "C4591001", "arm_field": arm_field,
        "arms": arms,
        "vaccine_vs_placebo_serious_rate_ratio": rr,
        "by_soc": by_soc,
        "by_age": by_age,
        "by_sex": by_sex,
        "ae_unmatched_to_arm": unmatched_ae,
        "stance": "question_no_conclusion",
        "caveat": "RANDOMIZED trial → real denominator (rate, not a floor), but: "
                  "trial population not real-world; ascertainment differs from "
                  "spontaneous systems (do NOT cross-bridge these rates with "
                  "VAERS/CVAR as equivalent); arm_field=actarm is as-treated. "
                  "Lead, not a verdict; the clinician/epidemiologist owns the why.",
        "what_would_sharpen": [
            "confirm USUBJID join (unmatched rate above)",
            "ITT (arm) vs as-treated (actarm) sensitivity",
            "stratify by age/sex (ADSL carries them)",
            "serious BY MedDRA SOC, not just the serious flag",
        ],
    }


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--adsl", required=True, help="ADSL envelopes jsonl glob")
    ap.add_argument("--ae", required=True, help="AE (adae) envelopes jsonl glob")
    ap.add_argument("--arm-field", default="actarm", choices=["actarm", "arm"])
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    adsl = sorted(_glob.glob(os.path.expanduser(args.adsl)))
    ae = sorted(_glob.glob(os.path.expanduser(args.ae)))
    if not adsl or not ae:
        print(f"error: no files (adsl={len(adsl)} ae={len(ae)})", file=sys.stderr)
        return 1
    rep = comparator(adsl, ae, args.arm_field)
    print(f"\n{'='*60}\n  PHMPT COMPARATOR — {rep['trial']} (arm_field={rep['arm_field']})\n{'='*60}")
    for cls, a in rep["arms"].items():
        rate = a["serious_rate_per_subject"]
        print(f"  {cls:18s} N={a['subjects_randomized']:>6}  serious_subj={a['subjects_with_serious_ae']:>5}"
              f"  rate={rate if rate is not None else 'NA'}  (AE recs {a['ae_records']:,})")
    print(f"\n  vaccine:placebo serious rate ratio (overall) = {rep['vaccine_vs_placebo_serious_rate_ratio']}")
    print(f"  AE unmatched to an arm: {rep['ae_unmatched_to_arm']:,}")
    print(f"\n  --- serious rate ratio BY MedDRA SOC (vaccine:placebo) ---")
    print(f"  {'SOC':40s} {'vacc':>5} {'plac':>5} {'RR':>6}")
    for d in rep["by_soc"]:
        print(f"  {d['soc'][:40]:40s} {d['vaccine_serious_subj']:>5} "
              f"{d['placebo_serious_subj']:>5} {str(d['rate_ratio']):>6}")
    print(f"\n  --- by age (serious rate vacc/plac, RR) ---")
    for k, r in rep["by_age"].items():
        if r["vaccine"]["n"] or r["placebo"]["n"]:
            print(f"  {k:8s} vacc {r['vaccine']['rate']} (n={r['vaccine']['n']})  "
                  f"plac {r['placebo']['rate']} (n={r['placebo']['n']})  RR={r['rate_ratio']}")
    print(f"  --- by sex ---")
    for k, r in rep["by_sex"].items():
        if r["vaccine"]["n"] or r["placebo"]["n"]:
            print(f"  {k:8s} vacc {r['vaccine']['rate']} (n={r['vaccine']['n']})  "
                  f"plac {r['placebo']['rate']} (n={r['placebo']['n']})  RR={r['rate_ratio']}")
    print(f"{'='*60}")
    if args.out:
        Path(args.out).write_text(json.dumps(rep, indent=2))
        print(f"  → {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
