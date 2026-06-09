# Supersession Notice — v2 data files (row-embedded caveats)

**Date:** 2026-06-09 · **Authorized by:** jr / John Reed (L4 sovereign) · Garrison Node S216

## What changed and why

The v1 data files in this repository carried their interpretive caveats only in
the README and `METHOD_AND_LIMITS.md`. When a CSV is downloaded, screenshotted,
or quoted on its own — detached from those documents — the caveat is lost, and
the most consequential files (mortality, myocarditis, deaths-over-65) are exactly
the ones most likely to travel alone.

v2 fixes this by embedding the caveat **in every row of every data file**. The
caveat text:

> **passive surveillance — reports are unverified — a report is not causation —
> reporting rates are not incidence rates**

This is the same language as `METHOD_AND_LIMITS.md`, now inseparable from the data.

## v1 is not retracted

v1 files remain valid **as v1**. Their hashes in the original `MANIFEST_SHA256.txt`
still verify; nothing about them was altered. v2 is an **additive re-issue**, not
a correction of error. The two are bound by per-file `*.RETROFIT_RECORD.json`
artifacts that record `source_sha256 → v2_sha256 → caveat_text`, so the chain of
custody from v1 to v2 is itself attestable.

## How v2 was produced (reproducible)

`GN/tools/caveat_retrofit.py` v0.1.0 — deterministic: the same input file and the
same caveat string produce byte-identical output every run (verified). Two modes:

- **69-column strand files** (sample, PREG, Q04, R3, T1): the caveat populates the
  pre-existing empty `gn_empty_a` column. **No schema change** — column count and
  order are unchanged; only an empty cell was filled.
- **Analytic extracts** (Q01, Q03, Q06, Q07): these have their own narrow schemas,
  so the caveat is an **appended `caveat` column**. These v2 files are named
  `*_v2_schema.csv` to make the header change loud, never silent.

## Verification

Each v2 file ships with `<file>.RETROFIT_RECORD.json`. To verify a v2 file:

```
sha256sum <file>_v2.csv     # compare to v2_sha256 in its RETROFIT_RECORD.json
```

The next ceremony attests the retrofit records as chain leaves; `MANIFEST_SHA256.txt`
is re-signed to include the v2 files alongside the originals.

*Garrison Node is the toolmaker, not the decider. We surface the pattern; we never
supply the motive. The caveat now rides with the pattern.*
