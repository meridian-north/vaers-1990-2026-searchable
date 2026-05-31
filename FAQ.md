# FAQ

### Does this prove vaccines caused these events?
No. VAERS is a *passive surveillance* system — a report means someone filed a
report, not that the vaccine caused the event. This data is for spotting signals
worth investigating (hypothesis-generating), not for proving cause. Treat every
count as "reports of," not "cases caused by."

### Then why publish counts at all?
Because the signals are real questions, and the public record should be easy to
query and hard to misrepresent — in *both* directions. The same data that stops
someone claiming "X deaths were caused" also stops someone dismissing a genuine
reporting spike. The honest move is to make it searchable and let people check.

### Why are 2021 numbers so high?
Several reasons at once: an unprecedented number of doses administered, intense
public awareness, mandates, and active encouragement to report. A passive system
reflects reporting behavior as well as underlying events. That's exactly why these
are hypothesis-generating, not conclusions.

### Can I compute a *rate* (events per million doses)?
Not from this file alone. VAERS gives you the numerator (reports) but not the
denominator (doses administered or person-time at risk). Rates require joining
external CDC dose-administration data, and even then VAERS under-reporting makes
the result a floor. We don't bake a rate in.

### Is there any personal information in here?
No. The published files are built only from structured, coded fields. CDC's
*original* raw files contain free-text narrative boxes that occasionally include
inadvertent identifiers (a phone number, a ZIP); none of those fields are in this
dataset. See `SOURCE_AND_VERIFICATION.md`.

### What happens when CDC removes or updates the original file?
This is a feature, not a problem. CDC revises and re-posts VAERS regularly, and
reports can be added or deleted. What you have here is a **dated, hash-anchored
snapshot** (1990–2026, processed on a fixed date) plus per-row content hashes
(`gn_sha256`) and a file-level manifest. If CDC's live file later differs from
this snapshot, that divergence is itself observable — and your copy preserves
exactly what the record said on the processing date. A full provenance-stamped
archive of the original raw is retained offline for auditors. In short: a mutable
government source is precisely why a fixed, verifiable snapshot is worth having.

### How do I know you didn't alter the data?
Three ways: (1) check any file against `MANIFEST_SHA256.txt`; (2) re-derive the
dataset yourself from CDC's source using the included method — same input + same
seed → same output; (3) each row carries `gn_sha256`, a content hash tracing it to
its source record. Disagree with a number? Re-run the query and show where it
differs.

### Your post says 513 myocarditis cases but the extract shows 617 — which is it?
Both, measured differently. **617** is all myocarditis/pericarditis reports in
males under 30 in 2021 across *every* vaccine — that's what the bundled `Q04`
extract contains. **513** is the subset following an *mRNA* vaccine
(Pfizer/Moderna). The post says "following mRNA vaccines," so it cites 513; the
extract is all-vaccine, so it shows 617. Filter `gn_mfr_name` to see it yourself.

### Can I trust a single lot's report count?
Read it carefully. A report listing two vaccines is counted against each lot named,
so lot totals can exceed report counts (faithful to the source, not double-counting
in error). And without a denominator — how many doses each lot represented — a high
count alone isn't an anomaly. Lot clustering is a question to investigate, not an
answer.

### Why is the sample so small / why don't my rare-signal searches find much?
The 1,000-row sample is a doorway, not the dataset. Common breakdowns (year, state,
manufacturer) hold up at that scale; rare-signal hunts (a symptom in a narrow
age band, a single lot) collapse to single digits. Use the sample to learn the
query, then run the full file. See `SAMPLE_SEARCHES_EXPLAINED.md`.

### Why Proton Drive instead of Google Drive?
Privacy posture. The dataset is public, but the project's principle is to minimize
third-party tracking of who's reading what. Proton has no API, so it's a manual
upload — that's a deliberate trade.

### Is the method open? Can I extend it?
Yes. The build scripts are included; the format is documented in `README.md` and
the column guide. The same structure (who/what/when/where/how) is source-agnostic,
so other surveillance datasets can be processed into the identical layout.

### Can you add other countries or data sources?
That's the roadmap. The same grammar already maps to other jurisdictions'
adverse-event systems (UK, Australia, Canada, etc.). Those ship in their own
bundles when ready; this one is U.S. VAERS only.

### How current is the data?
It runs through 2026 as of the processing date stamped in the files. VAERS itself
updates continually; re-process from CDC's source when you need a fresher cut.

---

*Have a question that isn't here? That's what the forum thread is for.*
