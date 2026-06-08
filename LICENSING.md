# Licensing — how the pieces fit

This repository mixes three kinds of material, each under the license that fits it.
Everything is © 2026 meridian-north except the government-derived data, which is
dedicated to the public domain.

| Material | Where | License |
|---|---|---|
| **Adverse-event data** (the VAERS CSVs, extracts, samples) | repo root `data/` + the Proton full file | **CC0 1.0** / public domain — derived from public-domain CDC/FDA VAERS |
| **Dataset tooling** (query/sample/load scripts) | repo root `*.py`, `*.R`, `*.sql` | **Apache 2.0** (see `LICENSE`) |
| **Methods prose** (the statement, the denominator lesson, kit docs) | `methods/**/*.md` | **CC BY 4.0** (see `methods/LICENSE-text-CC-BY-4.0.md`) |
| **Methods code** (the comparator scorers) | `methods/**/*.py` | **Apache 2.0** (see `methods/LICENSE-Apache-2.0.txt`) |

## Why the data is CC0 and the prose is CC BY

The dataset is a faithful restructuring of public-domain government records — it
carries no new authorship worth restricting, so it is released without conditions
(CC0). The methods prose *is* original authorship, so it is shared under CC BY 4.0:
reuse freely, including commercially, just keep the attribution.

Explicit dedication: the dataset files (the CSVs in this repository and in any
associated Release or mirror) are derived entirely from the U.S. VAERS, a
public-domain dataset published by the CDC and FDA. The derived structured dataset
is released into the public domain under a **Creative Commons Zero (CC0 1.0)**
dedication, to the extent any rights attach to the structuring. You may copy,
modify, and redistribute it for any purpose without permission or attribution.
Source: https://vaers.hhs.gov/data/datasets.html

## Why the methods code is Apache 2.0 rather than MIT

The methods code is meant to be re-run by people on contested ground and built upon
by people who owe us nothing. Apache 2.0 adds, over MIT, an explicit **patent
grant** and a **patent-retaliation clause**: contributors grant users a patent
license to what their contribution practices, and anyone who sues over those patents
loses their own rights to the code. For a tool published precisely so it can be
attacked and extended, that grant is worth the few extra paragraphs over MIT's
brevity.

## One code license across the repo

All code in this repository — the root dataset tooling and the methods scorers — is
under **Apache 2.0**, so the whole repo has a single code-license story: Apache code
+ CC0 data + CC BY prose. Apache was chosen over MIT for its explicit patent grant
and patent-retaliation clause, which matter for a tool published to be re-run and
built upon by people who owe us nothing. meridian-north is the sole copyright holder.
