# Reading the example searches — what the sample can and can't tell you

The bundle ships a **1,000-row sample** (`data/vaers_sample_1000.csv`) — a random
draw (fixed seed, so it's reproducible) from the full ~1,989,028-row file, with
the same 69 columns. It's there so you can run the questions in `QUERIES.md` and
see the shape of an answer in seconds, without downloading the whole dataset.

But a 1,000-row sample behaves very differently from the full file depending on
what you ask. Reading it fairly means knowing which is which.

## The same searches, sample vs. full

| Search | Sample (1,000 rows) | Full file (~1.99M) | What it tells you |
|---|---|---|---|
| Reports by year (peak) | 2021: **408** | 2021: **768,704** | proportions hold — the 2021 surge shows at both scales |
| Reports by manufacturer | Pfizer **265** / Moderna **234** | Pfizer **501,334** / Moderna **479,775** | common breakdowns are representative |
| Serious-outcome share | **8.7%** (87/1,000) | **~8%** | rate-like summaries on common fields survive sampling |
| Myocarditis/pericarditis, males <30 | **1** | **992** | rare signal — essentially invisible in a sample |
| Deaths, age 65+ | **9** | **15,628** | rare cohort — badly under-powered in a sample |
| Pregnancy-related | **6** | **11,184** | too few in a sample to characterize |
| Specific lot family | **8** | **10,593** | lot-level work needs the full file |

## What this means — read fairly

- **Common breakdowns are trustworthy on the sample.** Year, state, manufacturer,
  sex, and the overall serious-rate come out in roughly the right proportions at
  1,000 rows. Good for "what does this data look like."
- **Rare-signal hunts are not.** Anything specific — a symptom in a narrow age/sex
  band, deaths in one age group, a single lot — collapses to single digits or zero
  in a sample. **One** myocarditis case in the sample versus **992** in the full
  file is not a finding; it's an artifact of sample size. Never estimate a rate or
  claim a signal from the sample.
- That's the honest reason to **download the full processed CSV**: the sample
  teaches you the query; only the full file can answer the questions that matter.

## Limits of the search itself (independent of sample size)

- **Symptom matching is lexical, not clinical.** `%myocard%` matches any coded term
  containing those letters; it finds MedDRA terms by spelling, not by a clinician's
  judgment. Widen or narrow your keywords on purpose.
- **Multi-vaccine reports count against each vaccine/lot named.** A report listing
  two vaccines is counted once per manufacturer and per lot in those breakdowns, so
  manufacturer and lot totals can exceed the number of reports. That's faithful to
  the source, not an error.
- **Blank means "not recorded," not "no."** An empty age, lot, or date is unknown —
  don't read it as zero.

## Limits of VAERS itself (apply at every scale)

See `METHOD_AND_LIMITS.md`. In one line: a report is a *report*, not a confirmed
effect; the counts are a floor (most events are never reported); and there is no
population denominator, so a count is not a rate.

---

*The sample is the doorway. The full processed CSV is the room.*
