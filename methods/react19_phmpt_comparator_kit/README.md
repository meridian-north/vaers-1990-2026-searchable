# Pfizer C4591001 — vaccine-vs-placebo serious-AE comparator (open kit)

*A reproducible, denominator-bearing, placebo-controlled read of serious adverse
events in the Pfizer–BioNTech pivotal trial (C4591001), built from the PHMPT
court-released (FOIA) SDTM data. Counts are aggregate; no patient rows, no PII.*

> **This is a methods kit, not a finding, and not medical advice.** It measures a
> rate ratio and hands you the re-runnable method. It concludes nothing. Read
> `METHOD_AND_LIMITS.md` before quoting any number, and `QUESTIONS.md` for what the
> sub-analyses are (questions, not signals).

## Why this one is different from VAERS/openFDA kits

Every spontaneous-reporting kit (VAERS, openFDA/FAERS, the five-country set) has
**no denominator** — counts are a floor, no rate, no causation. C4591001 is a
**randomized trial**: each subject's arm (vaccine vs `Placebo`) and the per-arm N
are in the data. So here, and *only* here, we can compute an actual **rate**
(serious-AE subjects ÷ randomized subjects, per arm) and a controlled
**vaccine:placebo rate ratio**. The placebo arm is the trial's saline comparator —
not a flu shot, not another vaccine.

## Headline (read with the limits)

| Arm | Randomized N | Subjects with ≥1 serious AE | Serious rate |
|---|---|---|---|
| Placebo | 23,198 | 344 | 1.48% |
| Vaccine (BNT162b2 Ph2/3, 30 µg) | 23,170 | 324 | 1.40% |

**Overall vaccine : placebo serious rate ratio = 0.943** (vaccine fractionally
lower), and it is **stable across ITT (`arm`) and as-treated (`actarm`)** — both
0.943. The join is exact: **0 of ~74,000 AE records unmatched** to an arm.

The per-SOC, per-age, and per-sex breakdowns are in `RESULTS.md`. Most SOCs sit at
or below 1.0; a few small-count SOCs sit above 1.0 — those are **questions** (small
N, ~25 unadjusted comparisons), filed in `QUESTIONS.md`, not findings.

## Reproduce it

```bash
# inputs: the PHMPT SDTM envelopes (ADSL = arm assignment, ADAE = adverse events)
python3 phmpt_arm_join.py \
  --adsl '.../phmpt_pfizer/envelopes_sdtm/adsl/*c4591001*adsl*.jsonl' \
  --ae   '.../phmpt_pfizer/envelopes/*c4591001*adae*.jsonl' \
  --arm-field actarm --out phmpt_comparator.json     # add --arm-field arm for ITT
```

Deterministic, stdlib + DuckDB, no LLM. The subject join normalizes USUBJID
(`canon_usubjid`); the unmatched rate is reported as a built-in completeness check.

## What's in the kit

```
README.md                 <- you are here
METHOD_AND_LIMITS.md      <- read before quoting numbers (the guardrails)
RESULTS.md                <- overall + by SOC + by age + by sex + ITT vs as-treated
QUESTIONS.md              <- the >1.0 sub-results, filed as questions + what would sharpen
SOURCE_AND_VERIFICATION.md<- PHMPT FOIA provenance + SHA manifest
data/phmpt_comparator_actreated.json   <- the as-treated result artifact
data/phmpt_comparator_ITT.json         <- the ITT sensitivity artifact
phmpt_arm_join.py         <- the comparator (standalone copy of the pipeline tool)
MANIFEST_SHA256.txt       <- SHA-256 of every file
```

*Assembled by meridian-north. Hard to assemble, easy to verify — the method travels
with the data. Leads, not verdicts; the clinician/epidemiologist owns the why.*
