# Methods — what these tools claim, and what they don't

This section is the *method* behind the data in this repository: how we read the
public adverse-event record, what we will and will not say about it, and one
worked kit that shows the discipline in action.

Read it in this order:

1. **[What Audits Don't Do](WHAT_AUDITS_DONT_DO.md)** — the statement of method and
   limits. We claim transparency, not proof: proof of source, of path, and of
   who/what/where/when/how, never a verdict on whether anything is safe or unsafe.
2. **[The Denominator Lesson](THE_DENOMINATOR_LESSON.md)** — the same statistics run
   on data with and without a real denominator, giving opposite verdicts. This is
   why the VAERS data in this repo (no denominator → counts are a floor) is read
   differently from a randomized trial.
3. **[The PHMPT comparator kit](react19_phmpt_comparator_kit/)** — the counterpoint:
   the one place a real denominator exists. A reproducible vaccine-vs-placebo
   serious-AE comparator built from the Pfizer C4591001 court-released (PHMPT/FOIA)
   trial data, with confidence intervals and multiplicity correction. Aggregate
   counts only; no patient rows, no PII.

## How this relates to the VAERS dataset

The repository root holds spontaneous-report data (VAERS): rich, but with **no
denominator** and **no matched comparison group** — counts are a floor, not a rate,
and never a causal claim. The PHMPT kit here is the deliberate contrast: a
randomized trial *does* have a denominator, so it is the only place a real rate
ratio can be computed. Holding the two side by side is the whole point — it shows
exactly where a number can mean something and where it can only describe how the
data was collected.

## License

This methods section is dual-licensed by file type:

- **Text & documentation** (the statement, the denominator lesson, the kit's `.md`
  files) — Creative Commons Attribution 4.0 International (CC BY 4.0).
  See [`LICENSE-text-CC-BY-4.0.md`](LICENSE-text-CC-BY-4.0.md).
- **Code** (the kit's `.py` scorers) — Apache License 2.0.
  See [`LICENSE-Apache-2.0.txt`](LICENSE-Apache-2.0.txt).

Copyright 2026 MerkleTrust LLC. See the repository-level `LICENSING.md` for how this
fits with the dataset's public-domain (CC0) dedication and the repo's code license.

---

*Statements of method, not claims of findings. Leads, not verdicts. Not medical
advice. The method is open — check it.*
