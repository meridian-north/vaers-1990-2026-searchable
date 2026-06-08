# VAERS adverse-event reports — open dataset + query kit

A clean, searchable copy of the U.S. VAERS vaccine adverse-event data
(1990–2026), organized so you can ask plain questions of it — who was affected,
what happened, when, where, how (which vaccine, lot, dose) — and pull the actual
reports behind any answer.

**No personal information.** Built only from the structured, coded fields. The
free-text boxes in CDC's originals (where phone numbers or addresses sometimes
appear) are not included. Nothing here points back to a person.

> **Part of a five-system, five-country open release (plus a Pfizer FOIA set).**
> This repository is the **VAERS** release — the flagship, with the full query
> kit below. The same PII-free, verifiable treatment is applied to four more
> national reporting systems (Australia, the UK, Canada, Japan), plus the Pfizer
> FOIA release. Those live on the public Proton mirror — see **"The wider
> dataset"** below. One recipe, many agencies.

## Start here

1. Open `data/vaers_sample_1000.csv` — a small taster (any spreadsheet, or the queries below).
2. Skim `QUERIES.md` — ready-made questions (myocarditis/pericarditis in young males, deaths over 65, lot clustering, pregnancy, and more), each as a plain-English prompt and runnable SQL.
3. Read `METHOD_AND_LIMITS.md` (what it can/can't tell you) and `SAMPLE_SEARCHES_EXPLAINED.md` (worked searches on the sample vs the full file, with the fair limits of each) before quoting numbers — these are reports, not proof of cause; counts are a floor; there's no built-in denominator.
4. Want everything? The full ~2-million-row file `vaers_1990_2026_69col.csv.gz` (~95 MB zipped, ~624 MB open) lives in `data/` on the Proton mirror: https://drive.proton.me/urls/YB9AKDNCZC#8ZGtNiWl21ds — it's kept out of the GitHub repo to stay lightweight. Verify it against the SHA256 in `MANIFEST_SHA256.txt` (which is version-controlled here).

## The wider dataset — all six sources

This GitHub repo holds the **VAERS** files. The complete multi-agency dataset —
five national reporting systems across five countries, plus the Pfizer FOIA
release — is on the public Proton mirror, every file SHA-256 verifiable. Each
follows the same rule: **coded fields only, no free-text, no PII.**

- **VAERS** (United States): https://drive.proton.me/urls/YB9AKDNCZC#8ZGtNiWl21ds
- **TGA DAEN** (Australia): https://drive.proton.me/urls/1QHWX9T3Z8#q7z9ZLcwNW6B
- **MHRA Yellow Card** (United Kingdom): https://drive.proton.me/urls/7M6Q2PH4J4#UCIYrZsELiMx
- **Health Canada CVAR** (Canada): https://drive.proton.me/urls/V0X7RAD63W#vwGmI0aKv2it
- **JADER** (Japan): https://drive.proton.me/urls/WCSKTCSP4C#EFTnlzHDIPcC
- **Pfizer (PHMPT FOIA)** — trial documents, not a national reporting system: https://drive.proton.me/urls/N5KV5E8T7R#zr0Z68S5WTGm

Treat every link as public: there's no access gate, by design — the PII scrub is
the guarantee, not the link.

## What's in the bundle

```
README.md                    <- you are here
INDEX.md                     <- one-screen map of everything
QUERIES.md                   <- the question pack (prompts + SQL)
SAMPLE_SEARCHES_EXPLAINED.md <- worked searches: sample vs full, fair limits
METHOD_AND_LIMITS.md         <- what it can and can't tell you (read this)
SOURCE_AND_VERIFICATION.md   <- where the data comes from + how to verify it
FAQ.md                       <- common questions
LICENSE                      <- Apache-2.0 (code); data is CC0 — see LICENSING.md
CITATION.cff                 <- how to cite this dataset
MANIFEST_SHA256.txt          <- SHA256 for every file (incl. the Proton full file)
make_reader_sample_csv.py    <- make your own sample (by year/vaccine/symptom/id list)
data/
  vaers_sample_1000.csv         <- 1,000-row taster
  extracts/                     <- the actual rows behind the headline questions
    Q04_myocarditis_pericarditis_males_u30.csv
    R3_deaths_over65.csv
    PREG_pregnancy_related.csv
    T1_lot_family.csv
    Q01_report_volume_by_year.csv
    Q03_mortality_by_manufacturer.csv
    Q06_lot_clustering_top.csv
    Q07_reports_by_state.csv
  vaers_1990_2026_69col.csv.gz  <- FULL dataset (~95 MB) — on the Proton mirror, not in the GitHub repo
```

*(The five non-VAERS sources above are distributed on the Proton mirror, not in
this GitHub repo, to keep the repo lightweight.)*

## Methods — how we read this data

The [`methods/`](methods/) section is the discipline behind the numbers: a
statement of what these tools claim and don't ([What Audits Don't Do](methods/WHAT_AUDITS_DONT_DO.md)),
why a denominator changes everything ([The Denominator Lesson](methods/THE_DENOMINATOR_LESSON.md)),
and a worked, reproducible vaccine-vs-placebo comparator built from the Pfizer
C4591001 trial data ([the PHMPT kit](methods/react19_phmpt_comparator_kit/)) — the
one place a real denominator exists, set deliberately against this repo's
denominator-free VAERS reports.

## The fastest way to test it

```
-- DuckDB (pip install duckdb, or the duckdb CLI)
CREATE VIEW v AS SELECT * FROM read_csv_auto('data/vaers_sample_1000.csv', header=true, all_varchar=true);
SELECT gn_report_date[1:4] AS year, COUNT(*) FROM v GROUP BY 1 ORDER BY 1;
```

Or paste the CSV into any AI assistant and ask it the questions in `QUERIES.md`.

---

*Assembled by GarrisonNode. Hard to assemble, easy to verify — the method travels
with the data.*
