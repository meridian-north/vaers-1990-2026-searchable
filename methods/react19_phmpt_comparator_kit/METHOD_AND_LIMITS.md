# Method and limits — read this before quoting any number

## What was computed

For trial C4591001, each randomized subject's arm comes from **ADSL** (the
subject-level analysis dataset: `arm` = randomized/ITT, `actarm` = as-treated). Each
adverse event comes from **ADAE**. We join AE→subject on **USUBJID** (exact, after
whitespace/case normalization), classify a subject as *serious* if any of their AEs
is flagged `ae_serious` or has an outcome of hospitalized / died / disabled /
life-threatening, and compute, per arm:

> **serious rate = (subjects with ≥1 serious AE) ÷ (randomized subjects in arm)**

and the **rate ratio = vaccine rate ÷ placebo rate**. The denominator is the real
randomized N — this is the feature that makes it a rate, not a floor.

## What it is NOT

- **Not causation.** A rate ratio in a trial describes *association in this trial*.
  It is not proof the vaccine caused (or prevented) any event.
- **Not a safety verdict.** A serious-AE *rate ratio near 1.0* (0.943) is what a
  balanced safety profile looks like at the top line; it is not an endorsement, and
  the sub-analyses are not alarms. We report; we do not adjudicate.
- **Not severity- or causality-graded.** "Serious" is the regulatory seriousness
  flag (hospitalization / death / disability / life-threat / important medical
  event), NOT a clinician's causality assessment. A serious AE in either arm may be
  unrelated to what was injected.
- **Not real-world.** Trial populations are screened and monitored differently than
  the general public; do not generalize the rate to the population.

## Limits that bound EVERY sub-number

1. **Multiple comparisons.** The by-SOC table is ~15 organ systems, plus 4 age
   bands and 2 sexes — roughly **25 unadjusted comparisons**. With that many, some
   rate ratios will land above 1.0 *by chance alone*. No Bonferroni/FDR correction
   is applied. Treat any single elevated cell as a question, not a result.
2. **Small numbers → wide uncertainty.** Several elevated cells rest on tiny counts
   (e.g. a SOC with 18 vs 8 serious subjects; the 0–17 band with single-digit
   events per arm). **No confidence intervals are computed** in this kit — so an
   eye-catching ratio may be statistical noise. Compute CIs before believing any of
   them.
3. **As-treated vs ITT.** Default is `actarm` (as-treated). ITT (`arm`) is provided
   as a sensitivity run; the overall ratio is identical (0.943) but stratified cells
   can differ. Always state which you used.
4. **Serious-flag granularity.** We count *subjects with ≥1 serious AE*, not events,
   and not by preferred term. The same serious subject can appear under multiple
   SOCs, so SOC columns are not mutually exclusive.
5. **Source scope.** Built from the PHMPT court-released SDTM (`ADSL` + `ADAE`).
   Subjects in `SCREEN FAILURE` / `NOT ASSIGNED` are excluded; Phase-1 candidate
   arms (`BNT162b1`, tiny) are kept separate from the Phase-2/3 contrast.

## How to read it honestly

The defensible top-line statement is: *"In C4591001, the proportion of subjects
with at least one serious adverse event was ~1.4–1.5% in both arms, rate ratio 0.94
(vaccine vs placebo), stable across ITT and as-treated."* Everything below that
line — the SOC, age, and sex cells — is **hypothesis-generating**: a list of places
a qualified analyst might look next, each needing confidence intervals, multiple-
comparison adjustment, per-preferred-term detail, and time-to-onset before it could
mean anything. That work is the human's; this kit hands over the re-runnable counts
and stops.

*Leads, not verdicts. No PII (aggregate counts only). Not medical advice.*
