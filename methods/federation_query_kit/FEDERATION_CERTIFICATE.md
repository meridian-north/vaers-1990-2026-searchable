# Federation certificate — one query, seven systems

This is the output of `federation_query_finder.py` run across all seven corpora in
the family, on the shared MedDRA symptom field (`gn_symptoms_primary`). It is a
demonstration that a single query reaches every system and returns comparable,
attestable counts — **the federation mechanism, working.** It is not a finding about
any vaccine, drug, or symptom.

## What was queried

Seven independent reporting systems across five countries, **4,724,363 records in
total**, each projected into one shared 69-column schema:

| System | Country | Records scanned |
|---|---|---|
| VAERS | United States | 1,989,028 |
| V-Safe | United States (active monitoring) | 1,606,427 |
| MHRA Yellow Card | United Kingdom | 447,845 |
| TGA DAEN | Australia | 250,903 |
| PHMPT (Pfizer C4591001 trial) | United States (trial) | 231,632 |
| JADER | Japan | 169,027 |
| CVAR | Canada | 29,501 |

Only per-system aggregate counts are produced. No record crosses a corpus boundary —
so the certificate itself honors the federation claim it demonstrates.

## The result

Four serious adverse-event terms each return a hit in **six of the seven systems**
from one query. Myocarditis is the clearest demonstrator:

| Term | Coverage | VAERS | CVAR | JADER | PHMPT | TGA | MHRA | V-Safe | Total |
|---|---|---|---|---|---|---|---|---|---|
| Myocarditis | 6/7 | 507 | 395 | 1,132 | 6 | 858 | 150 | 0 | 3,048 |
| Pericarditis | 6/7 | 232 | 523 | 457 | 6 | 1,404 | 137 | 0 | 2,759 |
| Thrombocytopenia | 6/7 | 165 | 30 | 1,194 | 18 | 146 | 111 | 0 | 1,664 |
| Tinnitus | 6/7 | 5,652 | 80 | 147 | 138 | 590 | 2,508 | 0 | 9,115 |

One question — "myocarditis" — asked once, answered independently by the US, Canada,
Japan, Australia, the UK, and the Pfizer trial. That is what federation means here.

## Why V-Safe is the seventh, and answers with a zero

V-Safe returns 0 on every one of these — **on purpose, and disclosed.** V-Safe is an
active-monitoring reactogenicity survey with a *closed* symptom checklist; it never
coded "myocarditis," so it cannot report it. That zero is a blind spot of the
instrument, not evidence that the event did not occur. The federation makes the blind
spot legible by contrast: six systems answer, one structurally cannot. This is the
`ClosedVocabularyBlindSpotMt` principle — silent is not negative — sitting in the data.

## Two honest reads, for two audiences

- **The mechanism works.** One script reaches seven independent systems in five
  countries and four formats/languages and returns comparable counts. Re-run it; it
  holds.
- **The method names its own limits.** It surfaces nothing where there is nothing
  (V-Safe's disclosed zero), and it does not dress a count up as a risk. A tool that
  says where it cannot see earns the right to say what it can.

## What this is NOT

Not a finding. A term appearing in six reporting systems is six systems *recording
reports*, not six confirmations of risk. These are spontaneous and survey systems:
**counts are a floor, there is no denominator here, and no causal claim is implied.**
The PHMPT column is the one denominator-bearing system, and its counts are small
because it is a bounded trial — read it with that in mind. Leads, not verdicts. Not
medical advice.

## Reproduce it

```bash
# point the 7 paths in federation_query_finder.py at your universal-69 files, then:
python3 federation_query_finder.py --facet gn_symptoms_primary --top 25
```

Re-run with any facet (`what_symptoms_full --split`, `gn_vaccine_name`, …) or any
query, any time. That is the point: the federation claim is re-checkable on demand,
not asserted once. Then ask the question the kit is built to hand back: the integrated
picture is computable across all seven systems without exposing a single person — so
why isn't it?
