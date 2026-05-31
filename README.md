# VAERS adverse-event reports — open dataset + query kit

A clean, searchable copy of the U.S. VAERS vaccine adverse-event data (1990–2026),
organized so you can ask plain questions of it — *who* was affected, *what*
happened, *when*, *where*, *how* (which vaccine, lot, dose) — and pull the actual
reports behind any answer.

**No personal information.** Built only from the structured, coded fields. The
free-text boxes in CDC's originals (where phone numbers or addresses sometimes
appear) are not included. Nothing here points back to a person.

## Start here

1. Open `data/vaers_sample_1000.csv` — a small taster (any spreadsheet, or the
   queries below).
2. Skim `QUERIES.md` — ready-made questions (myocarditis/pericarditis in young
   males, deaths over 65, lot clustering, pregnancy, and more), each as a
   plain-English prompt *and* runnable SQL.
3. Read `METHOD_AND_LIMITS.md` (what it can/can't tell you) and
   `SAMPLE_SEARCHES_EXPLAINED.md` (worked searches on the sample vs the full file,
   with the fair limits of each) before quoting numbers — these are *reports*, not
   proof of cause; counts are a floor; there's no built-in denominator.
4. Want everything? The full ~2-million-row file `vaers_1990_2026_69col.csv.gz`
   (~95 MB zipped, ~624 MB open) lives in `data/` on the Proton mirror:
   https://drive.proton.me/urls/YB9AKDNCZC#8ZGtNiWl21ds — it's kept out of the
   GitHub repo to stay lightweight. Verify it against the SHA256 in
   `MANIFEST_SHA256.txt` (which is version-controlled here).

## What's in the bundle

```
README.md                    <- you are here
QUERIES.md                   <- the question pack (prompts + SQL)
METHOD_AND_LIMITS.md         <- what it can and can't tell you (read this)
SAMPLE_SEARCHES_EXPLAINED.md <- worked searches: sample vs full, fair limits
make_reader_sample_csv.py    <- make your own sample (by year/vaccine/symptom/id list)
data/
  vaers_sample_1000.csv       <- taster
  vaers_1990_2026_69col.csv.gz   <- full dataset
  extracts/                  <- the actual rows behind the headline questions
    Q04_myocarditis_pericarditis_males_u30.csv
    R3_deaths_over65.csv
    PREG_pregnancy_related.csv
    T1_lot_family.csv
    Q01_report_volume_by_year.csv
    Q03_mortality_by_manufacturer.csv
    Q06_lot_clustering_top.csv
    Q07_reports_by_state.csv
SOURCE_AND_VERIFICATION.md   <- where the data comes from + how to verify it
MANIFEST_SHA256.txt          <- checksums for everything above
```

## The fastest way to test it

```sql
-- DuckDB (pip install duckdb, or the duckdb CLI)
CREATE VIEW v AS SELECT * FROM read_csv_auto('data/vaers_sample_1000.csv', header=true, all_varchar=true);
SELECT gn_report_date[1:4] AS year, COUNT(*) FROM v GROUP BY 1 ORDER BY 1;
```

Or paste the CSV into any AI assistant and ask it the questions in `QUERIES.md`.

---

*Assembled by GarrisonNode. Hard to assemble, easy to verify — the method travels
with the data.*
