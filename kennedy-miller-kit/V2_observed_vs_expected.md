---
title: "v2 — Observed vs Expected: the age confound"
parent: "The Kennedy–Toxicology Reports–Miller Removal (six-axis study)"
corpus: meridian-north pharmacovigilance · VAERS 1990–2026 (n=1,989,028)
posture: neutral on safety · strong on method
status: L0 — cleared for outreach · June 2026
caveat: "passive surveillance — no vaccinated denominator — the vaccine schedule is confounded with the background SIDS age peak"
---

# v2 — Observed vs Expected: the age confound

Three independent reviews of the v1 days-to-onset chart, given the figure with no labels and
no framing, converged on the same correct refinement: a temporal cluster is only a hazard
signal if it survives comparison to what you would expect anyway. The sharpest version of
"what you would expect anyway" for infant death is **age**.

## The finding

We binned every infant (<1 yr) death in the corpus by **age at death** (n = 2,941 with age
recorded). The distribution:

| Age | Share of infant deaths | | Age | Share |
|---|---|---|---|---|
| 0–1 mo | 3.0% | | 6–7 mo | 7.4% |
| 1–2 mo | 7.0% | | 7–8 mo | 2.6% |
| **2–3 mo** | **44.0%** | | 8–9 mo | 1.1% |
| 3–4 mo | 19.4% | | 9–10 mo | 2.0% |
| 4–5 mo | 11.1% | | 10–11 mo | 1.0% |
| 5–6 mo | 1.3% | | 11–12 mo | 0.2% |

**85.8%** of these deaths occur before 6 months; **74.5%** fall in the 2–5 month window;
the single peak is **2–3 months (44%)**.

## Why that settles the timing argument — and why it settles nothing about cause

Background SIDS, independent of vaccination, peaks at **2–4 months**, with roughly 80% of
cases by 4 months and ~90–95% before 6 months (NICHD/CDC epidemiology). The US primary
vaccine series is administered at **2, 4, and 6 months**. These two facts mean the
vaccination calendar and the natural SIDS curve **sit on top of each other**: the babies who
die are dying at exactly the ages when (a) SIDS is most common and (b) vaccines are most
often given. A death "shortly after a vaccination" is, to first order, indistinguishable from
"a SIDS-aged death that happened to follow the visit the schedule put there."

This is the **confound**, and it is structural, not incidental. No amount of timing
resolution breaks it, because timing is precisely the axis on which the two explanations
coincide.

It cuts both ways, and the corpus states both edges out loud:

- The age match does **not** exonerate vaccines. A real effect could live inside the same
  window; coincidence of distributions is not proof of innocence.
- The fact that this corpus is *more* peaked at 2–3 months (44%) than background SIDS
  (~22–24%) is **not** a "2× excess." VAERS has no denominator, and the 2-month visit is the
  densest, most-reported vaccination event — so reports concentrate there for reasons of
  ascertainment, not necessarily biology. Reading the 44% as an excess rate is the same
  denominator error in a new costume.

## What an honest "expected" requires

A true observed-vs-expected needs the one quantity VAERS structurally does not contain: a
**vaccinated denominator by exact day of age**, so that deaths after vaccination can be
compared to background mortality *at that age*. The design that reaches the answer without a
population denominator is the **self-controlled case series** — each infant serves as their
own control, comparing risk windows to control windows within the same child, which cancels
fixed confounders like the age gradient. That is the instrument that can adjudicate this
question. Spontaneous-report timing cannot, in either direction.

## Bin-width correction (for completeness)

Dividing each onset bucket by its width gives a per-day rate, addressing the uneven-bin
critique. Infant deaths peak at **day 1 (28.7%/day)**, not day 0 — consistent with an infant
found unresponsive the following morning. All-reports peak at **day 0 (47.2%/day)**, the
same-day minor-reaction reporting signature. The v1 cross-cohort comparison is unchanged,
because every cohort is measured in identical bins. Full table:
`data/onset_perday_normalized_v2.csv`.

## Bottom line

v1 showed the clustering is a property of *reporting*. v2 shows that even the part that looks
most like biology — deaths close to the shot — is fully consistent with *the schedule landing
on the SIDS age window*. Two independent artifacts (reporting behaviour; schedule–age
coincidence) both point the same way, and neither can be promoted to causation from this
data. The question is real; the place to answer it is a denominated cohort or a
self-controlled case series, not the spontaneous-report pile.

*Leads, not verdicts. Not medical advice. The method is open; check it.*
