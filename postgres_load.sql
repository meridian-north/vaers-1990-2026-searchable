-- postgres_load.sql — load the VAERS 69-column file into PostgreSQL, group-by ready.
--
-- Design choice: every column is TEXT. A 2-million-row government CSV has blanks,
-- "UNK", "N/A", mixed-precision ages, etc. Loading as text imports clean every
-- time; you cast in the query where you need a number or a date. No failed COPY,
-- no surprises. Loads in a few seconds on commodity hardware.
--
-- Steps:
--   gunzip -k vaers_1990_2026_69col.csv.gz          # -> vaers_1990_2026_69col.csv
--   psql yourdb -f postgres_load.sql                 # creates table + loads
-- (or run the \copy line interactively in psql from the file's directory)

DROP TABLE IF EXISTS vaers;
CREATE TABLE vaers (
  gn_id                       text,
  gn_sha256                   text,
  gn_produced_at              text,
  gn_schema_class             text,
  gn_bitnet_signal            text,
  gn_chain_ref                text,
  gn_source_class             text,
  gn_runner_seed              text,
  gn_source_jurisdiction      text,
  gn_lot_number               text,
  gn_mfr_name                 text,
  gn_vaccine_name             text,
  gn_dose_number              text,
  gn_report_date              text,
  gn_onset_date               text,
  gn_state_region             text,
  gn_age_years                text,
  gn_sex                      text,
  gn_outcome_died             text,
  gn_outcome_serious          text,
  gn_outcome_er               text,
  gn_symptoms_primary         text,
  gn_join_thread              text,
  who_reporter_class          text,
  who_underlying              text,
  what_symptoms_full          text,
  what_outcome_lt             text,
  what_outcome_hosp_days      text,
  what_outcome_disabling      text,
  what_outcome_recovered      text,
  what_outcome_recovering     text,
  when_vax_date               text,
  when_received_date          text,
  when_days_to_onset          text,
  where_admin_site            text,
  where_country               text,
  why_current_illness         text,
  why_medications             text,
  why_allergies               text,
  why_prior_vaccines          text,
  how_vaccines_full           text,
  how_study_design            text,
  how_survey_instrument       text,
  gn_dsf_value                text,
  gn_group_inherited          text,
  gn_cohort_id                text,
  bitnet_t1_ternary           text,
  bitnet_t2_ternary           text,
  bitnet_t3_ternary           text,
  bitnet_rationale            text,
  gn_proxy_verdict            text,
  gn_retro_scored             text,
  gn_milspec_seed             text,
  gn_schema_fingerprint       text,
  gn_sweep_run_id             text,
  gn_chain_block_type         text,
  gn_source_provenance        text,
  gn_loom_thread_a            text,
  gn_loom_thread_b            text,
  gn_loom_thread_c            text,
  gn_loom_thread_d            text,
  gn_empty_a                  text,
  gn_empty_b                  text,
  gn_mt_membership            text,
  flag_pack                   text,
  cohort_or_join_thread       text,
  beacon_trace                text,
  aletheia_methodology        text,
  gn_spare                    text
);

-- Load (run from the directory holding the uncompressed CSV):
\copy vaers FROM 'vaers_1990_2026_69col.csv' WITH (FORMAT csv, HEADER true)
-- One-liner alternative (server-side, no pre-gunzip; needs file/superuser perms):
-- COPY vaers FROM PROGRAM 'gunzip -c /path/to/vaers_1990_2026_69col.csv.gz' WITH (FORMAT csv, HEADER true);

CREATE INDEX ON vaers (gn_mfr_name);
CREATE INDEX ON vaers (gn_lot_number);
ANALYZE vaers;

-- ---------------------------------------------------------------------------
-- Example group-bys (cast text -> number/date where needed). Dates are ISO.
-- ---------------------------------------------------------------------------

-- Reports by year
-- SELECT left(gn_report_date,4) AS year, count(*) FROM vaers GROUP BY 1 ORDER BY 1;

-- Deaths by manufacturer
-- SELECT gn_mfr_name, count(*) AS reports,
--        count(*) FILTER (WHERE gn_outcome_died='1') AS deaths
-- FROM vaers GROUP BY 1 ORDER BY deaths DESC;

-- Lot clustering: reports per lot (one report can name >1 lot; here counts the row)
-- SELECT gn_lot_number, count(*) AS reports
-- FROM vaers WHERE gn_lot_number <> '' GROUP BY 1 ORDER BY reports DESC LIMIT 100;

-- Myocarditis/pericarditis in males under 30, by year
-- SELECT left(gn_report_date,4) AS year, count(*)
-- FROM vaers
-- WHERE (what_symptoms_full ILIKE '%myocard%' OR what_symptoms_full ILIKE '%pericard%')
--   AND gn_sex='M' AND NULLIF(gn_age_years,'')::numeric < 30
-- GROUP BY 1 ORDER BY 1;

-- Serious-outcome share by year
-- SELECT left(gn_report_date,4) AS year, count(*) AS reports,
--        round(100.0*count(*) FILTER (WHERE gn_outcome_serious='1')/count(*),2) AS pct_serious
-- FROM vaers GROUP BY 1 ORDER BY pct_serious DESC;
