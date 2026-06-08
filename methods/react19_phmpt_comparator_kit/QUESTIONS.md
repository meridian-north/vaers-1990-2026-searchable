# Questions — not findings

*Per the partnership doctrine (THE_WHY): we surface the pattern, file the question
with its sharpeners, and conclude nothing. The cells below are where a vaccine:placebo
serious rate ratio landed above 1.0. With ~25 unadjusted comparisons and small
counts, some elevation is expected by chance. **None of these is a signal.** Each is
a place a qualified analyst might look next — and exactly what they'd need to do to
tell signal from noise.*

## Update — these cells were run through the rigor gate, and none survived

Since first drafting, every cell below was given a 95% CI (Fisher exact p) and
screened across all 22 comparisons with Benjamini-Hochberg FDR (`RESULTS.md` →
"Statistical rigor"). **0 of 22 survive** (q < 0.05 with a CI excluding 1.0). The
headliner, Hepatobiliary RR 2.25, lands at CI [0.98, 5.18], Fisher p 0.052, **FDR q
0.80** — its interval includes 1.0 and it does not survive correction. So the
questions below are preserved as a record of *what we checked and why it was noise*,
not as open signals. They remain re-runnable; if a future, larger dataset moved any
of them, the method would show it. For now: **properly-bounded leads, none
significant.**

## The overall picture first (the anchor)

Overall serious-AE rate ratio is **0.943** (vaccine slightly below placebo), stable
across ITT and as-treated. The questions below are sub-slices of a balanced whole;
read them against that anchor, not in isolation.

## Filed questions (each: question · what it is · what would sharpen)

**Q-HEPATO — Hepatobiliary (RR 2.25; vaccine 18 vs placebo 8).**
*Question:* Why is the serious-hepatobiliary subject count higher in the vaccine arm
in this trial? *What it is:* a 26-subject contrast across ~46k randomized — small N,
no CI, one of ~25 comparisons. *What would sharpen:* exact 95% CI; per-preferred-term
breakdown (which hepatic events); time-to-onset vs dose dates; baseline liver
history from ADSL/medical history; multiplicity adjustment.

**Q-GENDIS — General disorders / administration site (RR 1.57; 11 vs 7).**
*Question:* Is this the expected reactogenicity-at-injection-site difference
surfacing as "serious", or noise? *Sharpen:* split injection-site vs systemic PTs;
CI; it is the most mechanistically expected arm difference — check it is not just
reactogenicity mislabeled serious.

**Q-RENAL — Renal and urinary (RR 1.30; 13 vs 10).** *Question:* real or small-N?
*Sharpen:* CI; PT detail; pre-existing renal history; almost certainly within noise.

**Q-NEO / Q-CARD — Neoplasms (RR 1.07; 44 vs 41) and Cardiac (RR 1.04; 49 vs 47).**
*Question:* These are near-unity on the two most publicly-scrutinized organ systems.
*What it is:* essentially balanced (ratios ~1.0). *Sharpen:* CI (will straddle 1.0);
for cardiac, isolate myo/pericarditis PTs specifically and check time-to-onset;
for neoplasms, latency makes a short-trial signal implausible — note the window.

**Q-PEDS — Age 0–17 (RR 1.80; ~9 vs ~5 serious).** *Question:* elevated ratio in the
youngest band? *What it is:* single-digit counts per arm — the noisiest cell in the
kit. *Sharpen:* CI (very wide); PT detail; this cell cannot support any inference as
counts stand.

## What every one of these shares

- **No confidence intervals** are computed here — compute them first; most will
  straddle 1.0.
- **No multiplicity adjustment** — across 25 comparisons, ~1 false positive at p<0.05
  is expected with nothing going on.
- **Serious flag, not causality** — a serious event in the vaccine arm is not a
  vaccine-caused event.
- **The clinician/epidemiologist owns the why.** This kit measured and caveated; it
  did not conclude.

*Questions, with their sharpeners. Concludes nothing. Not medical advice.*
