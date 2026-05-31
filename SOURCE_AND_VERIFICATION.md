# Source & verification

## Where this data comes from

Everything here is derived from the U.S. **VAERS** (Vaccine Adverse Event
Reporting System), co-run by the CDC and FDA. VAERS data is **public domain** and
published by the government at:

> https://vaers.hhs.gov/data/datasets.html

CDC distributes it as per-year files and as one combined `AllVAERSDataCSVS.zip`.
Our dataset covers **1990–2026**, processed uniformly (fixed seed) into the
69-column structured format you see here.

## Why we don't re-host CDC's raw files

CDC's original files include free-text narrative fields (SYMPTOM_TEXT, LAB_DATA,
HISTORY, etc.) that occasionally contain inadvertent personal identifiers. Our
processed files are built **only from the structured, coded fields**, so they
carry no personal information by construction.

Rather than redistribute CDC's free-text raw (and with it that personal-identifier
surface), we point you to CDC's own authoritative copy and show you how to confirm
our version was derived faithfully. This is deliberate: it's more protective of
the people in the data, and CDC's copy is the real tamper-evidence anchor — you
can re-download it any time and check us against it.

## How to verify this dataset is faithful to the source

1. **Download the source** from the CDC link above (per-year files or the combined
   `AllVAERSDataCSVS.zip`).
2. **Check our processed file's fingerprint.** The SHA256 of
   `vaers_1990_2026_69col.csv.gz` (and every other file) is in
   `MANIFEST_SHA256.txt`. Run `shasum -a 256 <file>` and compare.
3. **Re-derive it yourself (optional).** The method is included
   (`make_reader_sample_csv.py` + the build script): run it against CDC's data and
   you should reproduce the same structured 69-column output. Same input + same
   seed → same result.
4. **Spot-check any row.** Each row carries `gn_sha256`, a content hash of its
   source record, so an individual report can be traced back to the source data.

## Provenance summary

- Source: CDC/FDA VAERS, public domain, 1990–2026.
- Processing: uniform decomposition, fixed seed (reproducible).
- A full, provenance-stamped archive of the original per-year raw files is retained
  offline (with its own manifest of hashes) and can be made available to auditors
  on request — it is intentionally not published here to avoid redistributing the
  free-text identifier surface.

*Public-domain source. PII-free derivative. The method travels with the data, and
the source is one click away — so anyone can check our work.*
