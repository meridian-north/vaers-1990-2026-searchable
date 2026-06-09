# Federation query kit — one question, seven systems

This kit answers a single question about the corpus family: **does a federated
query actually work across all the independent systems, or is "federation" just a
word?** It does it by finding the query that the most systems answer at once.

All seven corpora — VAERS (US), CVAR (Canada), JADER (Japan), the Pfizer C4591001
trial (PHMPT/FOIA), TGA (Australia), MHRA (UK), and V-Safe (US active monitoring) —
are projected into one shared 69-column schema. Because the schema is shared, one
value of one column can be asked of every system at the same time. `federation_query_finder.py`
tallies a facet column in each corpus and ranks candidate queries by **coverage** —
how many of the seven independent systems return a hit.

Crucially, it emits **only per-system aggregate counts**. No record crosses a corpus
boundary. So the output *is* the federation proof: the same question, answered
independently by N systems, with nothing but counts shared between them.

## Run it

```bash
# point the seven paths in federation_query_finder.py (or a --corpora JSON) at your
# universal-69 CSVs (.csv or .csv.gz), then:
python3 federation_query_finder.py                       # facet: gn_symptoms_primary
python3 federation_query_finder.py --facet what_symptoms_full --split
python3 federation_query_finder.py --max-rows 100000     # fast representative pass
```

It writes `federation_certificate.json` (winner + full coverage matrix) and
`federation_top.tsv` (ranked demonstrators). Re-run any time with any facet or
query — that is the point: the federation claim is re-checkable on demand, not a
one-time assertion.

## What the run found

See [`FEDERATION_CERTIFICATE.md`](FEDERATION_CERTIFICATE.md). Headline: on the MedDRA
symptom field, **myocarditis, pericarditis, thrombocytopenia, and tinnitus each
appear independently in six of the seven systems** — one query, six national/trial
surveillance systems answering, counts only.

## Two honest notes the kit makes visible

- **V-Safe is the seventh, and it answers 6-of-7 questions with a zero — on purpose.**
  V-Safe is an active-monitoring reactogenicity survey with a *closed* symptom
  checklist; it never coded "myocarditis," so it cannot report it. That zero is a
  blind spot of the instrument, not evidence of absence — and the kit surfaces it
  rather than hiding it.
- **Manufacturer doesn't federate raw.** Federating on `gn_mfr_name` collapses
  because each system spells the maker differently ("PFIZER-BIONTECH" vs
  "PFIZER\WYETH" vs codes). That is exactly why a normalization step (`canon_mfr`)
  exists; without it, a shared *vocabulary* like MedDRA is what makes federation real.

## What this is and isn't

This demonstrates that the federation *mechanism* works — that one query reaches all
the systems and returns comparable, attestable counts. It is **not** a finding about
any vaccine, drug, or symptom. A symptom appearing in six reporting systems is six
systems *recording reports*, not six confirmations of risk: counts are a floor, there
is no denominator here, and no causal claim is implied. Leads, not verdicts.

License: code Apache-2.0, prose CC BY 4.0 (see the parent `methods/` licenses).
