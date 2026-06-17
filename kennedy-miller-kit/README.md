# Kennedy–Miller VAERS Review Kit

A six-axis (who/what/where/when/how/why) corpus kit on the June 2026 removal of Neil Z.
Miller's 2021 vaccine–SIDS paper from *Toxicology Reports* and Secretary Kennedy's letter
demanding transparency about that removal. Built on the Meridian North pharmacovigilance
corpus (VAERS 1990–2026, n=1,989,028).

**Posture:** neutral on vaccine safety · strong on method · method fully open.
A claim-navigator, not a claim-engine.

## Contents

| File | What it is |
|------|------------|
| `STUDY_6axis_kennedy_miller_vaers.md` | The six-axis study — the substantive centerpiece |
| `MILLER_STEELMAN.md` | Miller's actual argument from the primary source + fair rebuttal (contested ≠ dismissed) |
| `V2_observed_vs_expected.md` | The age-confound analysis (v2) |
| `DOCTRINE_sensor_sourced_reporting.md` | Forward note: when reports write themselves, the job is truth-of-path + identity |
| `kennedy_miller_vaers_review.html` | Self-contained interactive webform (open in any browser) |
| `OUTREACH_reply_seckennedy.md` | Short/threaded public reply drafts for the @SecKennedy thread |
| `data/case_records_v2.csv` | Case-records corpus, v2 literature-index schema, embedded caveats |
| `data/doo_distribution_sample.csv` | Days-to-onset sample pull, per-bucket, all cohorts |
| `data/doo_summary.csv` | Days-to-onset summary (day 0–2 / 0–3 shares per cohort) |
| `data/suid_crossnational_ok_rows.csv` | kmv-011: US vs Nordic SUID per 100k live births (WHO Mortality DB, the denominated comparison) |
| `MANIFEST_SHA256.txt` | SHA-256 of every file — milspec replayability |

## The one finding (and its limits)

Running Miller's own days-to-onset metric across the full corpus with controls side by side:
the day-0–2 clustering is **stronger in all-infant reports (mostly non-fatal) and across the
entire database than in the infant-death slice** the SIDS argument depends on. Clustering
near the shot date is a property of how a passive system *records* events, not a fingerprint
of harm — exactly what HHS's own VAERS Data Use Guide describes. This **cannot** prove
vaccines cause SIDS; it **also cannot** prove they don't. The instrument can't adjudicate
causation in either direction. That belongs to a denominated cohort / self-controlled design.

## Source-class vocabulary (extended, documented)

Beyond the reference hierarchy (RCT > clinical_trial > observational > preclinical > review >
lore > unknown, plus `retracted`), this corpus adds three document classes, named here so the
extension is loud, not silent: `retraction_notice`, `guidance` (publication-ethics), and
`gov_methodology`, and `official_correspondence`. Retracted records are **retained**, never
deleted.

## Verify

```
sha256sum -c MANIFEST_SHA256.txt        # check every file
```
The webform also includes an in-browser SHA-256 verifier (SubtleCrypto, runs locally).

*Leads, not verdicts. Not medical advice. The method is open; check it.*
