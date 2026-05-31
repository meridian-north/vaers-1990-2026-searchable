# How this was built, and what it can and can't tell you

Read this before quoting any number from the data. It's short on purpose.

## What VAERS is

VAERS is the U.S. Vaccine Adverse Event Reporting System, run jointly by CDC and
FDA. **Anyone** can file a report — a doctor, a patient, a family member, a
manufacturer. A report says only that someone experienced a health event after a
vaccine and chose to report it. **It does not mean the vaccine caused the event.**

That makes this data good for one job: spotting *signals* worth investigating
(hypothesis-generating). It cannot, by itself, prove or disprove that a vaccine
caused anything (hypothesis-testing). Treat every count here as "reports of," not
"cases caused by."

## Two limits that never go away

- **Counts are a floor, not a ceiling.** Most real adverse events are never
  reported — published work has estimated under 1% capture in some settings. So a
  number here is the minimum that got written down, not the true total. We do not
  estimate the unreported fraction.
- **There's no denominator.** This data tells you how many reports came in, not
  how many people got the vaccine. Without the population (or person-time) at
  risk, you can't turn a count into a true rate from this file alone. Where CDC
  dose-administration data is available it can be joined separately; this bundle
  does not bake in a rate.

## How the file was made

- Built from CDC's public VAERS files, 1990–2026, processed the same way for every
  year (reproducible, fixed seed).
- **Only structured, coded fields are included.** The original CDC files have
  free-text narrative boxes where people occasionally typed phone numbers,
  addresses, or names. **None of those free-text fields are in this file** — so
  there is nothing that identifies a person. Columns like "current illness,"
  "other medications," and "allergies" are intentionally blank here for that
  reason.
- Each row carries a checksum, and the bundle includes an unmodified copy of CDC's
  original file (with its own checksum) so you can confirm nothing was altered.

## Verifying it yourself

1. Check `MANIFEST_SHA256.txt` against the files you downloaded.
2. Compare against the `original_cdc_mirror/` copy of CDC's source.
3. Re-run any query in `QUERIES.md` and you get the actual rows — not our summary.

## One report, many lenses

The same report reads differently depending on who's asking — a clinician sees a
possible adverse-event signal, a researcher sees an epidemiology data point, a
family sees a safety signal for a household decision, a lawyer sees evidence with
a chain of custody. The data is the same; the question you bring is what changes.

*Hard to assemble. Easy to verify. The method travels with the data.*
