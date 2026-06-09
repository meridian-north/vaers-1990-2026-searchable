#!/usr/bin/env python3
"""
federation_query_finder.py
==========================
Find the query that best *demonstrates federation* across the pharmacovigilance
corpus family. All corpora share the universal-69 schema, so one value of one
column can be asked of every system at once. This tool tallies a facet column
per corpus and ranks candidate queries by **coverage** — how many of the
independent systems return a hit — surfacing the strongest "one question, seven
answers" demonstrator.

It emits ONLY aggregate counts per corpus. No record crosses a corpus boundary,
so the federation claim is honored by construction (this is the proof, not a leak).

Usage
-----
    python3 federation_query_finder.py                      # defaults below, facet=gn_symptoms_primary
    python3 federation_query_finder.py --facet gn_mfr_name  # federate on manufacturer
    python3 federation_query_finder.py --facet what_symptoms_full --split   # multi-value field
    python3 federation_query_finder.py --max-rows 150000    # cap per corpus for a fast pass
    python3 federation_query_finder.py --corpora mycfg.json # {"NAME":"path", ...}

Outputs
-------
    federation_certificate.json   the winner + full coverage matrix (the kit artifact)
    federation_top.tsv            ranked demonstrators, tab-separated
"""
import csv, gzip, io, os, sys, re, json, argparse
from collections import defaultdict

# ---- Edit these paths to your 7 corpora (universal-69 CSV or .csv.gz) ----------
DEFAULT_CORPORA = {
    "VAERS":  "data/vaers_69col.csv",
    "CVAR":   "data/cvar_69col.csv",
    "JADER":  "data/jader_69col.csv",
    "PHMPT":  "data/phmpt_ae_69col.csv",
    "TGA":    "data/tga_69col.csv",
    "MHRA":   "data/mhra_69col.csv",
    "VSAFE":  "data/vsafe_69col.csv",
}
SPLIT_RE = re.compile(r"[;|]")           # multi-value field separators
csv.field_size_limit(1 << 24)


def open_any(path):
    if path.endswith(".gz"):
        return io.TextIOWrapper(gzip.open(path, "rb"), encoding="utf-8", errors="replace")
    return open(path, encoding="utf-8", errors="replace")


def norm(v):
    return re.sub(r"\s+", " ", v.strip().upper())


def scan(path, facet, split, max_rows):
    """Return (Counter-like dict of normalized facet -> count, rows_seen)."""
    counts = defaultdict(int)
    rows = 0
    with open_any(path) as fh:
        r = csv.reader(fh)
        try:
            header = next(r)
        except StopIteration:
            return counts, 0
        try:
            ci = header.index(facet)
        except ValueError:
            raise SystemExit(f"  column '{facet}' not in {path}\n  available: {', '.join(header[:25])} ...")
        for row in r:
            rows += 1
            if max_rows and rows > max_rows:
                break
            if ci >= len(row):
                continue
            cell = row[ci]
            if not cell:
                continue
            vals = SPLIT_RE.split(cell) if split else [cell]
            seen = set()
            for v in vals:
                n = norm(v)
                if n and n not in seen:        # count a value once per record
                    seen.add(n)
                    counts[n] += 1
    return counts, rows


def main():
    ap = argparse.ArgumentParser(description="Find the strongest cross-corpus federation query.")
    ap.add_argument("--facet", default="gn_symptoms_primary",
                    help="column to federate on (default: gn_symptoms_primary)")
    ap.add_argument("--split", action="store_true",
                    help="treat the facet cell as a ;/| separated list of values")
    ap.add_argument("--max-rows", type=int, default=0, help="cap rows per corpus (0 = all)")
    ap.add_argument("--top", type=int, default=20, help="how many demonstrators to list")
    ap.add_argument("--min-count", type=int, default=1,
                    help="ignore facet values with fewer than this many hits in a corpus")
    ap.add_argument("--corpora", help="JSON file mapping {name: path}; overrides defaults")
    args = ap.parse_args()

    corpora = DEFAULT_CORPORA
    if args.corpora:
        with open(args.corpora) as fh:
            corpora = json.load(fh)

    matrix = defaultdict(dict)     # value -> {corpus: count}
    totals = {}                    # corpus -> rows scanned
    present = []
    for name, path in corpora.items():
        if not os.path.exists(path):
            print(f"  skip {name}: not found ({path})", file=sys.stderr)
            continue
        counts, rows = scan(path, args.facet, args.split, args.max_rows)
        totals[name] = rows
        present.append(name)
        for v, c in counts.items():
            if c >= args.min_count:
                matrix[v][name] = c
        print(f"  scanned {name:6s} {rows:>10,} rows, {len(counts):>7,} distinct '{args.facet}'", file=sys.stderr)

    n_sys = len(present)
    if n_sys == 0:
        raise SystemExit("No corpora found — edit DEFAULT_CORPORA paths or pass --corpora.")

    # rank: coverage desc, then floor (min count among covered systems) desc, then total desc
    ranked = []
    for v, perc in matrix.items():
        coverage = len(perc)
        floor = min(perc.values())
        total = sum(perc.values())
        ranked.append((coverage, floor, total, v))
    ranked.sort(reverse=True)

    # ---- report ----
    order = present
    print("\n" + "=" * 78)
    print(f"FEDERATION QUERY FINDER  —  facet: {args.facet}   systems: {n_sys}")
    print("=" * 78)
    if ranked:
        cov, floor, total, v = ranked[0]
        print(f"\nStrongest demonstrator: \"{v}\"")
        print(f"  answered by {cov}/{n_sys} systems   (floor {floor:,} per system, {total:,} total hits)")
        print("  per-system counts:")
        for s in order:
            print(f"    {s:6s} {matrix[v].get(s, 0):>10,}")
    print(f"\nTop {args.top} demonstrators (cov = systems answering):")
    print(f"  {'cov':>3} {'floor':>9} {'total':>11}  query")
    for cov, floor, total, v in ranked[: args.top]:
        print(f"  {cov:>3} {floor:>9,} {total:>11,}  {v}")

    # ---- artifacts ----
    cert = {
        "facet": args.facet,
        "split": args.split,
        "systems": order,
        "rows_scanned": totals,
        "max_rows_cap": args.max_rows or None,
        "winner": None,
        "top": [],
    }
    if ranked:
        cov, floor, total, v = ranked[0]
        cert["winner"] = {"query": v, "coverage": cov, "floor": floor, "total": total,
                          "per_system": {s: matrix[v].get(s, 0) for s in order}}
        for cov, floor, total, v in ranked[: args.top]:
            cert["top"].append({"query": v, "coverage": cov, "floor": floor, "total": total,
                                "per_system": {s: matrix[v].get(s, 0) for s in order}})
    with open("federation_certificate.json", "w") as fh:
        json.dump(cert, fh, indent=2)
    with open("federation_top.tsv", "w") as fh:
        fh.write("coverage\tfloor\ttotal\t" + "\t".join(order) + "\tquery\n")
        for cov, floor, total, v in ranked[: args.top]:
            fh.write(f"{cov}\t{floor}\t{total}\t" +
                     "\t".join(str(matrix[v].get(s, 0)) for s in order) + f"\t{v}\n")
    print("\nWrote federation_certificate.json and federation_top.tsv")


if __name__ == "__main__":
    main()
