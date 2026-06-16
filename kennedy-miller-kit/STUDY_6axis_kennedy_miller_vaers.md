---
title: "The Kennedy–Toxicology Reports–Miller Removal: A Six-Axis Corpus Study"
subtitle: "Who / What / Where / When / How / Why — a claim-navigator, not a claim-engine"
corpus: meridian-north pharmacovigilance (VAERS 1990–2026, n=1,989,028)
posture: neutral on vaccine safety · strong on method · method fully open
status: L0 — cleared for outreach · June 2026
license: "Text: CC BY 4.0 · Code: Apache-2.0"
caveat: "passive surveillance — reports are unverified — a report is not causation — reporting rates are not incidence rates"
---

# The Kennedy–Toxicology Reports–Miller Removal

## A six-axis corpus study

This is a navigation aid for a contested record, not a verdict on it. It maps a single
public controversy — Secretary Kennedy's June 11, 2026 letter to the Editor-in-Chief of
*Toxicology Reports* demanding an explanation for the removal of Neil Z. Miller's
vaccine–SIDS paper — across the six axes the Meridian North corpus is built on:
**who, what, where, when, how, why.** Every record it touches is graded, caveated, and
traceable to a primary source. Where the evidence earns a strong statement about *method*,
this study makes one. It makes no statement about whether any vaccine does or does not
cause sudden infant death, because the instruments in play cannot settle that question in
either direction — and saying otherwise would be the exact error at the center of the
dispute.

The whole controversy turns out to be a clean teaching case for one idea: **a temporal
association recorded by a passive system is not a causal finding, and the absence of a
control or denominator is not a detail — it is the whole ballgame.** That idea cuts in
every direction at once. It is why Miller's clustering cannot prove a hazard. It is also
why a two-sentence removal notice that waves at "methodological flaws" without showing the
work is itself a failure of the transparency the same idea demands.

---

## WHO — the actors and their standing

The principals are **Robert F. Kennedy, Jr.**, Secretary of Health and Human Services, who
sent the letter; **Lawrence H. Lash, Ph.D.** (Wayne State University, Pharmacology), the
Editor-in-Chief of *Toxicology Reports* who is its addressee; **Neil Z. Miller**, the
author of the removed paper; and **Elsevier**, the publisher that executed the removal.

In VAERS terms, "who" is also the **reporter class** and the **patient cohort**. The Miller
paper's cohort is infants under one year of age who died; its reports were filed by a
mixture of private clinicians, manufacturers, and members of the public. This matters: VAERS
is a *self-selected* reporter pool. Nobody knows how many vaccinated infants did **not**
generate a report, which is the first reason the system yields rates of *reporting*, never
rates of *occurrence*.

A note on standing the corpus records but does not adjudicate: the Secretary is
simultaneously the head of the department that runs VAERS and a long-time public critic of
vaccine safety practice. That dual role is metadata, not disqualification. His procedural
demand — that a removal state its reasons, name its reviewers, and disclose their conflicts
— is a reasonable one on its own terms regardless of who makes it.

## WHAT — the object of the dispute

The disputed object is one paper: Miller NZ, *"Vaccines and sudden infant death: An analysis
of the VAERS database 1990–2019 and review of the medical literature,"* **Toxicology Reports
8 (2021): 1324–1335**, DOI 10.1016/j.toxrep.2021.06.020, PMID 34258234. The paper analyzed
2,605 infant deaths reported to VAERS and reported that roughly three-quarters clustered
within seven days of vaccination. It read that clustering as a signal of a vaccine–SIDS
association and assembled corroborating literature back to 1946 (Werne & Garrow, JAMA) and
forward to 2014 (Matturri et al., *Current Medicinal Chemistry*).

What is *also* in dispute is a second object: the **removal notice itself**. Kennedy's letter
attacks it as "woefully insufficient" — two sentences where the COPE retraction guidance
(Wager et al., 2009) says a notice "should state the reason(s) for retraction." So the corpus
holds two contested documents, not one: the paper, and the manner of its erasure.

In our schema both are retained. Record **kmv-001** carries `source_class: retracted` — not
deleted, not hidden, indexed with its retraction status attached. *Retracted ≠ deleted.*
The removal notice is **kmv-002**. The reason a corpus keeps a retracted paper visible is
the same reason Kennedy gives for writing: a record that quietly disappears cannot be
audited by anyone.

## WHERE — the mechanism nodes

"Where" in this corpus is not geography; it is **mechanism** — the place in the causal or
procedural machinery where each claim lives. Four nodes carry the entire case:

**Passive surveillance.** VAERS accepts unverified reports from anyone. It has no
denominator and no active follow-up. It is built to *generate hypotheses*, not test them.

**Temporal / stimulated reporting bias.** HHS's own VAERS Data Use Guide (kmv-006) states
plainly that "more serious and unexpected medical events are probably more likely to be
reported than minor ones, especially when they occur soon after vaccination, even if they
may be coincidental and related to other causes." In other words, the system is *designed*
to over-record events close to the shot date. Proximity in time is what gets a report
filed; proximity in time is therefore not evidence of cause.

**Denominator absence.** Without knowing how many vaccinated infants did not die, a count of
deaths-after-vaccination cannot become a *rate*, and without a rate there is nothing to
compare to background infant mortality. Miller's 75%-within-seven-days has no unvaccinated
or unexposed comparison group; the figure describes when reports arrive, not when deaths
occur relative to a baseline.

**Causation inference.** This is the node where the paper's reasoning fails as *method* — and,
symmetrically, where any confident counter-claim of "definitely no association" would also
overreach. Passive data can refute neither hypothesis. It can only say: this instrument
cannot answer this question.

## WHEN — the timeline

The paper was published in 2021. It circulated for roughly five years. On **2026-05-26**
Elsevier retracted/removed it, citing post-publication concerns about research errors and
methodological flaws and a determination that the author's response did not satisfactorily
address them. On **2026-06-11** Secretary Kennedy sent the letter that anchors this study,
requesting a full written record of the decision **by 2026-06-25**.

"When" is also the analytic heart of the data question: **days-to-onset.** The Miller
argument is entirely a statement about *when* deaths are reported relative to *when* the
vaccine was given. The next axis shows what happens when you actually plot that distribution
across the whole corpus rather than within the fatal-infant slice alone.

## HOW — the method, and the sample pull

This is the centerpiece. We ran the same days-to-onset measurement Miller relied on, on the
full Meridian North VAERS corpus (1990–2026, n = 1,989,028 records), and put the fatal-infant
slice **side by side with controls.** The question is not "do infant deaths cluster near the
shot?" — they do. The question is whether that clustering is *specific* to the
vaccine-causes-death hypothesis or whether it is a generic property of the reporting system.
If the same clustering appears in records where a causal hazard window is implausible, the
cluster is an artifact of *reporting*, not a fingerprint of *harm*.

Share of each cohort's reports whose onset falls in the first three days after vaccination:

| Cohort | n (cohort) | n with onset date | Day 0–2 | Day 0–3 |
|---|---|---|---|---|
| Infant <1 yr, **died** (Miller-style slice) | 2,941 | 2,638 | **55.3%** | **64.2%** |
| Infant <1 yr, **all reports** (mostly non-fatal) | 69,911 | 62,365 | **83.5%** | **86.3%** |
| Adult 18–64, **died** (control) | 5,075 | 4,662 | 27.6% | 30.9% |
| **All VAERS reports** 1990–2026 (baseline) | 1,989,028 | 1,647,504 | **71.9%** | **74.6%** |

Read those four rows together and the artifact is unmistakable. The clustering is **not
strongest in the fatal-infant slice** that the SIDS argument depends on — it is *stronger*
in the all-infant population (83.5% in days 0–2), the overwhelming majority of which are
**non-fatal** reports for which no death-hazard window exists at all. It is also strong in
the **entire database** (71.9%), across every age, vaccine, and outcome. A causal hazard
cannot explain why trivial, non-fatal infant reports cluster *harder* against the shot date
than infant deaths do. Reporting behavior can: parents and clinicians file when the shot is
fresh in mind, and attention decays with each passing day.

The adult-death control makes the same point from the other side. Adult deaths are *least*
clustered (27.6% in days 0–2) and carry a long tail (the single largest bucket is 91+ days),
because adult deaths arrive with competing explanations and slower attribution — the
reporting impulse is weaker and more diffuse. Same instrument, same metric, opposite shape,
driven entirely by who tends to file and when.

This is the **denominator lesson** applied live: rigorous arithmetic on a broken comparison
produces a confident wrong answer. Miller's 75% is real arithmetic. It is also, on this
evidence, a measurement of **reporting latency**, not of a biological hazard window. The
honest label for record kmv-008 is therefore *disproportionality / reporting-behavior
diagnostic* — never a safety finding — and that is exactly how the corpus tags it.

A symmetry the method also forces: this same table **cannot** be turned around to prove
vaccines are safe for infants either. It proves only that *this instrument cannot adjudicate
the causal question in either direction.* The place to answer it is a study with a real
denominator and matched ascertainment — a cohort or self-controlled-case-series design — not
the spontaneous-report pile.

## WHY — gaps, incentives, and the transparency question

"Why" is where the corpus refuses to flatten the dispute into one side. Two distinct
"why" questions live here, and they have different answers.

**Why the paper's inference fails.** Because passive surveillance has no denominator and a
built-in temporal bias that the publishing government agency documents in its own data guide.
That is a methodological fact, not a political position, and it is why a clustering result
cannot support a causal claim.

**Why the removal is nonetheless a legitimate target of scrutiny.** Because the *cure* for a
bad inference is a transparent correction, not an opaque erasure. The COPE guidance the
letter cites (kmv-003) says a retraction notice should state its reasons. A two-sentence
removal that asserts "conclusions not supported by the methodology" without publishing the
analysis, without naming the reviewers, and without disclosing their conflicts does not
*demonstrate* the flaw — it asserts it. Kennedy's five questions (how the decision was
reached, who was consulted and their conflicts, whether the corroborating literature was
examined, what the criteria for "implications for medical practice" are and whether they are
applied evenhandedly, and why removal rather than an expression of concern or standard
retraction) are, as *process* questions, well-formed. A reader can hold that Miller's method
was invalid **and** that the removal should have shown its work. Those positions do not
conflict; the same transparency principle generates both.

The deepest "why" the corpus is built to surface is the one neither party should skip:
**absence of evidence is a data point, not a verdict.** The reason there is no clean answer
to "do vaccines cause SIDS" from this data is that the surveillance instrument was never
built to answer it. Naming that blind spot — rather than filling it with whichever
conclusion one prefers — is the entire posture of this corpus. *What audits don't do is more
important than what they do.*

---

## Signal vocabulary applied to this case

Using the corpus's interaction-signal grammar (WARN / CAUTION / WATCH / LOW / LORE), keyed
here to *methodological status* rather than drug interaction:

- **WARN** — kmv-001 (Miller paper): an active, documented method conflict — causal inference
  drawn from denominator-free passive data. Retained, flagged, not deleted.
- **CAUTION** — kmv-002 (removal notice): plausible grounds, but insufficient transparency;
  fails the COPE "state your reasons" standard the corpus and the letter both invoke.
- **WATCH** — kmv-004 (Werne 1946, n=2), kmv-005 (Matturri 2014, single-case neuropath):
  mechanistic hypotheses and historical case reports — hypothesis-generating, not
  hazard-establishing.
- **LOW** — kmv-006 (HHS Data Use Guide): authoritative methodology statement; the keystone
  caveat source, no interpretive conflict.
- **LORE** — the broader "vaccines cause SIDS" claim as it circulates in public discourse:
  recorded, labeled, neither elevated to evidence nor suppressed.

## What this study claims, and what it does not

It claims **transparency, not proof** — proof of source, of path, and of the who/what/where/
when/how/why, each traceable to a primary record and a recomputable hash. It does **not**
claim that vaccines are safe, or unsafe, for infants. Passive and self-reported systems
record temporal association, not causation; no amount of clean processing changes what the
underlying instrument was built to capture. The reproducibility of this method must not be
mistaken for proof of any conclusion about infant safety. Those are two different things, and
the corpus keeps them apart on purpose.

**Sensitive-data note.** This study concerns infant death. It reproduces no personally
identifying information; VAERS IDs and age brackets are the only references used, consistent
with the corpus's sensitive-data discipline. Counts are a floor, not a denominator. If this
topic touches you personally, it is a heavy one — the figures here are about how a reporting
system records events, not a measure of risk to any individual child, and questions about a
specific child's care belong with a trusted clinician.

---

*Leads, not verdicts. Not medical advice. The method is open; check it. Garrison Node is the
toolmaker, not the decider — we surface the pattern; we never supply the motive.*
