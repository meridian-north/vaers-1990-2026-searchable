# Source and verification

## Where the data comes from

- **Trial:** Pfizer–BioNTech C4591001 (the pivotal Phase 2/3 COVID-19 vaccine trial).
- **Source:** the PHMPT (Public Health and Medical Professionals for Transparency)
  court-released / FOIA SDTM datasets — the same documents the FDA released under
  order. Specifically the `ADSL` (subject-level: arm, demographics) and `ADAE`
  (adverse events) domains, ingested into structured clause envelopes.
- **No PII.** This kit publishes only aggregate counts and rates per arm/SOC/stratum.
  No subject rows, no identifiers leave the host. USUBJID is used only as an internal
  join key and is not published.

## The placebo, explicitly

The comparator arm in C4591001 is labeled **`Placebo`** in both `ADSL.arm` and
`EX.extrt` (exposure) — the trial's saline injection comparator. It is **not** a flu
vaccine and **not** another active vaccine. (EX also carries `exroute`/`exdosfrm`
confirming it was administered as an injection matching the active-arm schedule.)

## How the join works (and how to check it)

Each AE subject (`ADAE.who.trial_subject_id`) is matched to its ADSL arm on
**USUBJID**, normalized by `canon_usubjid` (uppercase, collapse whitespace). In
C4591001 both domains store USUBJID identically (`STUDY SITE SUBJECT`), so the join
is exact. The tool reports **AE-records-unmatched-to-an-arm** as a built-in
completeness check; for this run it was **0** of ~74,000 — every AE was armed.

## Reproduce + verify

```bash
python3 phmpt_arm_join.py \
  --adsl '.../phmpt_pfizer/envelopes_sdtm/adsl/*c4591001*adsl*.jsonl' \
  --ae   '.../phmpt_pfizer/envelopes/*c4591001*adae*.jsonl' \
  --arm-field actarm --out phmpt_comparator_actreated.json   # --arm-field arm for ITT
```

Deterministic (stdlib + DuckDB, no LLM, no randomness) → byte-identical JSON on
re-run. Verify any published number against the JSON, and the JSON against
`MANIFEST_SHA256.txt`.

| Artifact | SHA-256 (first 16) |
|---|---|
| as-treated result | `39e85aa21eeb3326` |
| ITT result | `14135787bd6fd96c` |

## Lineage

Built by meridian-north's pharmacovigilance pipeline (`jsonl_to_parquet` →
`phmpt_arm_join`). Method is open; the SDTM source is public (PHMPT). Hard to
assemble, easy to verify — the method travels with the data.
