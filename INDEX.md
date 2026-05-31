# Index — what's in this folder

**New here? Read `README.md` first, then open `data/vaers_sample_1000.csv`.**

## Documents
| File | What it is |
|---|---|
| `README.md` | Start here — what this is, how to use it |
| `INDEX.md` | This file |
| `QUERIES.md` | The question pack — 20+ searches as plain-English prompts *and* SQL |
| `SAMPLE_SEARCHES_EXPLAINED.md` | Worked searches on the sample vs the full file, and the fair limits of each |
| `METHOD_AND_LIMITS.md` | What this data can and can't tell you (read before quoting numbers) |
| `SOURCE_AND_VERIFICATION.md` | Where the data comes from (CDC) and how to verify mine against it |
| `FAQ.md` | Common questions, including "what if CDC changes the source file?" |
| `MANIFEST_SHA256.txt` | Checksums for every file here |

## Data
| File | What it is |
|---|---|
| `data/vaers_1990_2026_69col.csv.gz` | The full dataset — ~1,989,028 reports, 69 columns (100 MB gzipped, ~624 MB open) |
| `data/vaers_sample_1000.csv` | 1,000-row taster (same format) — run the queries in seconds |
| `data/vaers_sample_300.csv` | Smaller taster |

## Pre-pulled results (the actual rows behind the headline questions)
| File | What it is |
|---|---|
| `data/extracts/Q04_myocarditis_pericarditis_males_u30.csv` | Every myocarditis/pericarditis report, males under 30 (all vaccines) |
| `data/extracts/R3_deaths_over65.csv` | Death reports, age 65+ |
| `data/extracts/PREG_pregnancy_related.csv` | Pregnancy / fetal-related reports |
| `data/extracts/T1_lot_family.csv` | Reports for a specific lot family (edit the lots to your own) |
| `data/extracts/Q01_report_volume_by_year.csv` | Report counts by year |
| `data/extracts/Q03_mortality_by_manufacturer.csv` | Reports + death-flag counts by manufacturer |
| `data/extracts/Q06_lot_clustering_top.csv` | Top lot numbers by report volume |
| `data/extracts/Q07_reports_by_state.csv` | Reports by U.S. state |

## Tool
| File | What it is |
|---|---|
| `make_reader_sample_csv.py` | Make your own sample by year / vaccine / symptom / ID list (part of the method) |

---

*Public-domain CDC source. PII-free derivative. The method travels with the data.*
