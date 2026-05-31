# VAERS query pack — ask the data anything

Every query below comes in two forms:

- **Ask** — a plain-English question you can paste into any AI assistant together
  with the CSV, or just read as "what this finds."
- **Run** — DuckDB SQL against the 69-column file. Use `data/vaers_sample_300.csv`
  for a taste or the full `vaers_1990_2026_69col.csv` for real results.

Setup (once):
```sql
CREATE VIEW v AS SELECT * FROM read_csv_auto('vaers_1990_2026_69col.csv', header=true, all_varchar=true);
-- use TRY_CAST(gn_age_years AS DOUBLE) wherever age math is needed
```

Read **METHOD_AND_LIMITS.md** before quoting any number. Short version: these are
*reports*, not confirmed effects — a report means someone filed it, not that the
vaccine caused it. Counts are a floor (most events are never reported) and there's
no population denominator built in, so these are hypothesis-generating only.

The `extracts/` folder already contains the actual rows for the headline
questions (Q04, deaths 65+, pregnancy, lot family) — open those directly.

---

## Core suite (Q01–Q20)

**Q01 — Report volume by year**
```sql
SELECT gn_report_date[1:4] AS year, COUNT(*) AS reports FROM v GROUP BY 1 ORDER BY 1;
```

**Q02 — Serious outcomes, COVID vs flu**
```sql
SELECT gn_vaccine_name, COUNT(*) AS reports,
       SUM(CASE WHEN gn_outcome_serious='1' THEN 1 ELSE 0 END) AS serious
FROM v WHERE gn_vaccine_name ILIKE '%COVID%' OR gn_vaccine_name ILIKE '%FLU%'
GROUP BY 1 ORDER BY reports DESC;
```

**Q03 — Mortality by manufacturer**
```sql
SELECT gn_mfr_name, COUNT(*) AS reports,
       SUM(CASE WHEN gn_outcome_died='1' THEN 1 ELSE 0 END) AS deaths
FROM v GROUP BY 1 ORDER BY deaths DESC;
```

**Q04 — Myocarditis / pericarditis in young males** (the marquee signal)
Pre-run answer: 2021 spiked to ~239 in 18–24 + 212 under-18 + 62 in 25–29, vs
single digits in prior years.
```sql
SELECT gn_report_date[1:4] AS year, COUNT(*) AS reports
FROM v
WHERE (what_symptoms_full ILIKE '%myocard%' OR what_symptoms_full ILIKE '%pericard%')
  AND gn_sex='M' AND TRY_CAST(gn_age_years AS DOUBLE) < 30
GROUP BY 1 ORDER BY 1;   -- swap the SELECT for "SELECT *" to pull the rows
```

**Q05 — Onset latency**
```sql
SELECT TRY_CAST(when_days_to_onset AS INTEGER) AS days_to_onset, COUNT(*) AS reports
FROM v WHERE when_days_to_onset <> '' GROUP BY 1 ORDER BY 1;
```

**Q06 — Lot clustering**
```sql
SELECT gn_lot_number, gn_mfr_name, COUNT(*) AS reports
FROM v WHERE gn_lot_number <> '' GROUP BY 1,2 ORDER BY reports DESC LIMIT 100;
```

**Q07 — Geographic clustering**
```sql
SELECT gn_state_region, COUNT(*) AS reports FROM v GROUP BY 1 ORDER BY reports DESC;
```

**Q08 — Symptom baseline**
```sql
SELECT gn_symptoms_primary, COUNT(*) AS reports
FROM v WHERE gn_symptoms_primary <> '' GROUP BY 1 ORDER BY reports DESC LIMIT 100;
```

**Q09 — Reporter type**
```sql
SELECT who_reporter_class, COUNT(*) AS reports FROM v GROUP BY 1 ORDER BY reports DESC;
```

**Q10 — 37-year serious-rate rank**
```sql
SELECT gn_report_date[1:4] AS year, COUNT(*) AS reports,
       ROUND(100.0*SUM(CASE WHEN gn_outcome_serious='1' THEN 1 ELSE 0 END)/COUNT(*),2) AS pct_serious
FROM v GROUP BY 1 ORDER BY pct_serious DESC;
```

**Q11 — Dose-number effect**
```sql
SELECT gn_dose_number, COUNT(*) AS reports FROM v GROUP BY 1 ORDER BY reports DESC;
```

**Q12 — Age × manufacturer**
```sql
SELECT gn_mfr_name,
  CASE WHEN TRY_CAST(gn_age_years AS DOUBLE) < 18 THEN 'under_18'
       WHEN TRY_CAST(gn_age_years AS DOUBLE) < 30 THEN '18_29'
       WHEN TRY_CAST(gn_age_years AS DOUBLE) < 65 THEN '30_64'
       WHEN TRY_CAST(gn_age_years AS DOUBLE) >= 65 THEN '65_plus' ELSE 'unknown' END AS age_band,
  COUNT(*) AS reports
FROM v GROUP BY 1,2 ORDER BY 1,2;
```

**Q13 — Time-to-onset shift**
```sql
SELECT gn_report_date[1:4] AS year,
       ROUND(AVG(TRY_CAST(when_days_to_onset AS INTEGER)),1) AS avg_days_to_onset
FROM v WHERE when_days_to_onset <> '' GROUP BY 1 ORDER BY 1;
```

**Q14 — Multi-vaccine co-administration**
```sql
SELECT COUNT(*) AS multivax_reports FROM v WHERE gn_vaccine_name LIKE '%|%';
```

**Q15 — Recovery vs disability**
```sql
SELECT what_outcome_recovered, what_outcome_disabling, COUNT(*) AS reports
FROM v GROUP BY 1,2 ORDER BY reports DESC;
```

**Q16 — Lot × geography concentration**
```sql
SELECT gn_lot_number, gn_state_region, COUNT(*) AS reports
FROM v WHERE gn_lot_number <> '' GROUP BY 1,2 ORDER BY reports DESC LIMIT 200;
```

**Q17 — Sex × outcome**
```sql
SELECT gn_sex, COUNT(*) AS reports,
       SUM(CASE WHEN gn_outcome_died='1' THEN 1 ELSE 0 END) AS deaths,
       SUM(CASE WHEN gn_outcome_serious='1' THEN 1 ELSE 0 END) AS serious
FROM v GROUP BY 1 ORDER BY reports DESC;
```

**Q18 — Reporter type × seriousness**
```sql
SELECT who_reporter_class,
       ROUND(100.0*SUM(CASE WHEN gn_outcome_serious='1' THEN 1 ELSE 0 END)/COUNT(*),2) AS pct_serious
FROM v GROUP BY 1 ORDER BY pct_serious DESC;
```

**Q19 — Repeat-reporter follow-ups** — *needs a field not in the public set;*
runs only in the full substrate. Listed for completeness.

**Q20 — PACVS / Yale post-acute phenotype cluster**
```sql
SELECT gn_report_date[1:4] AS year, COUNT(*) AS reports
FROM v
WHERE what_symptoms_full ILIKE '%fatigue%' OR what_symptoms_full ILIKE '%cognitive%'
   OR what_symptoms_full ILIKE '%tachycard%' OR what_symptoms_full ILIKE '%paraesthesia%'
   OR what_symptoms_full ILIKE '%paresthesia%' OR what_symptoms_full ILIKE '%exercise%'
GROUP BY 1 ORDER BY 1;
```

---

## Targeted add-ons (React19 / TickerForum + pregnancy)

**PREG — Pregnancy-related reports**
```sql
SELECT * FROM v
WHERE what_symptoms_full ILIKE '%pregnan%' OR what_symptoms_full ILIKE '%abortion%'
   OR what_symptoms_full ILIKE '%miscarriage%' OR what_symptoms_full ILIKE '%foetal%'
   OR what_symptoms_full ILIKE '%fetal%' OR what_symptoms_full ILIKE '%stillbirth%';
```

**T1 — Specific lot family** (substitute the lots you're investigating)
```sql
SELECT * FROM v WHERE gn_lot_number IN ('EL3248','EL9261','EL0140','EL9543','EN6201');
```

**R3 — Deaths in the 65+ cohort**
```sql
SELECT * FROM v WHERE gn_outcome_died='1' AND TRY_CAST(gn_age_years AS DOUBLE) >= 65;
```

**Cross-jurisdiction (R1/T3)** — comparing a signal across US / UK / Australia /
Canada needs each country's own file. Those ship separately; this CSV is US VAERS only.

---

*Run any "SELECT *" query and you get the actual report rows, not a summary —
that's the point. Hard to assemble, easy to verify.*
