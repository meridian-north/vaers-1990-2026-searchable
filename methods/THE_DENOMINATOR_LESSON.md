# The denominator lesson — when our numbers mean something, and when they don't

*A methods disclosure from meridian-north. We publish this because a tool is only
worth trusting if its maker says, out loud, where it stops working. This note is
that statement for our pharmacovigilance kits.*

---

## The one rule

**A comparison is only as good as its denominator and its ascertainment.** Rigorous
statistics applied to a broken comparison do not fix it — they make a wrong answer
look confident. So before any number we publish, we ask: *is there a real
denominator, and were both sides measured the same way?* If yes, the number can
mean something. If no, it can only describe how the data was collected, not what
happened to people.

We ran the **identical** statistical machinery — risk ratios, 95% confidence
intervals, Fisher exact tests, and a Benjamini-Hochberg correction for testing many
things at once — on two kinds of data. It gave opposite verdicts, and the
difference was entirely the denominator. Here is both, in the open.

## Case A — a real denominator: the Pfizer trial (C4591001)

A randomized trial has the thing spontaneous reports never do: a **known
denominator** (how many people were in each arm) and **the same ascertainment on
both sides** (vaccine and placebo subjects were monitored identically). So a
serious-adverse-event rate ratio between the arms is a fair, apples-to-apples
comparison.

We computed it from the court-released (PHMPT/FOIA) trial data: serious-AE rate
about **1.4–1.5% of subjects in both arms, rate ratio 0.94** (vaccine vs placebo),
stable whether analyzed as-randomized or as-treated. We then broke it down by organ
system, age, and sex — **22 comparisons** — and put a confidence interval on every
one and corrected for the multiple looks.

**Result: 0 of 22 comparisons survived.** Every interval crossed 1.0; the
eye-catching cells (a 2.25× ratio in one organ system) collapsed to "could easily be
chance" once their uncertainty and the number of comparisons were accounted for.
The honest read is a **balanced profile with no sub-group signal that survives
correction.** That is a publishable result *because the comparison is valid* — and
we publish it (the PHMPT comparator kit) precisely because it withstands the test.

## Case B — no denominator: cross-country spontaneous reports

Spontaneous-reporting systems — the US VAERS, Canada's CVAR, the UK Yellow Card —
collect reports people choose to file. There is **no denominator** (you never know
how many exposed people *didn't* report), and the systems **ascertain differently**:
some, by design and habit, capture mostly serious events; others capture everything.

We compared the fraction of reports flagged "serious" between VAERS and Canada's
CVAR, with the same CIs and FDR correction. Every cohort came back "significantly
different" — VAERS around 14–23% serious, CVAR around 57–100% serious, a roughly
four- to five-fold gap, p-values near zero.

**And every one of those "significant" results is meaningless as a safety
statement.** The gap is *ascertainment*: CVAR (a Yellow-Card-style system) receives
mostly the serious reports; VAERS receives the trivial alongside the grave. The
statistics correctly detected that the two systems *record* seriousness differently
— which we already knew — and could say nothing about whether anything is actually
more or less dangerous anywhere. No denominator, no rate, no causation. We keep this
kind of cross-system number **internal** (a disproportionality diagnostic), and we
do **not** dress it up as a public safety comparison, because a reader could mistake
an artifact of paperwork for a fact about bodies.

## Why we disclose this

The cheap move is to publish the spontaneous-report table — it has big, alarming-
looking ratios and impeccable statistics, and it would travel. We don't, because it
would mislead, and a tool that will mislead you for attention is not a tool you
should trust with anything that matters.

So here is our standing commitment, and the test you can hold us to:

- **We publish comparisons with a real denominator and matched ascertainment** (the
  trial kit). You can re-run them and attack the method; it holds.
- **We do not publish denominator-free cross-system comparisons as findings.** When
  we use them at all, it is as an internal *disproportionality* diagnostic, labeled
  as reporting-behavior, never as risk.
- **Every number ships with its limits attached** — counts that are a floor, the
  absence of a denominator, the ascertainment differences — and with the method open
  so anyone can check it.

That is the whole posture: we prove the provable, we refuse the verdict, and we tell
you plainly which of our own numbers you should believe and which you shouldn't. The
denominator is the line between them.

*Leads, not verdicts. Not medical advice. The method is open; check it.*
