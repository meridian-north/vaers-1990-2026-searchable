# Results — C4591001 serious-AE comparator

*As-of 2026-06-08. Source: PHMPT court-released SDTM (`ADSL` + `ADAE`). Aggregate
counts only — no PII. Read `METHOD_AND_LIMITS.md` first; every sub-cell is a
question, not a finding.*

## Overall (as-treated, `actarm`)

| Arm | Randomized N | Subjects w/ serious AE | Serious rate | AE records |
|---|---|---|---|---|
| Placebo | 23,198 | 344 | 1.483% | 37,120 |
| Vaccine (BNT162b2 Ph2/3) | 23,170 | 324 | 1.398% | 37,150 |
| BNT162b1 (Phase-1 candidate) | 84 | 0 | 0% | 252 |
| BNT162b2 (Phase-1) | 72 | 2 | 2.778% | 64 |

**Overall vaccine:placebo serious rate ratio = 0.943.** AE records unmatched to an
arm: **0**.

## Sensitivity — ITT (`arm`) vs as-treated (`actarm`)

| Basis | Placebo N | Vaccine N | Placebo rate | Vaccine rate | Rate ratio |
|---|---|---|---|---|---|
| As-treated (`actarm`) | 23,198 | 23,170 | 1.483% | 1.398% | **0.943** |
| ITT (`arm`) | 23,254 | 23,226 | 1.479% | 1.395% | **0.943** |

The top-line ratio is identical under both — the one robust statement in this kit.

## By MedDRA System Organ Class (vaccine:placebo, as-treated)

*Counts are subjects-with-a-serious-AE-in-that-SOC; SOCs are not mutually exclusive.
Small counts + ~25 unadjusted comparisons → treat each row as a question.*

| SOC | vaccine | placebo | rate ratio |
|---|---|---|---|
| Infections and infestations | 61 | 68 | 0.898 |
| Cardiac disorders | 49 | 47 | 1.044 |
| Neoplasms benign/malignant/unspecified | 44 | 41 | 1.074 |
| Injury, poisoning, procedural | 28 | 34 | 0.825 |
| Nervous system disorders | 29 | 32 | 0.907 |
| Gastrointestinal disorders | 27 | 30 | 0.901 |
| Respiratory, thoracic, mediastinal | 19 | 25 | 0.761 |
| Vascular disorders | 15 | 18 | 0.834 |
| Musculoskeletal & connective tissue | 14 | 16 | 0.876 |
| **Hepatobiliary disorders** | 18 | 8 | **2.253** |
| Psychiatric disorders | 10 | 14 | 0.715 |
| Renal and urinary disorders | 13 | 10 | 1.302 |
| General disorders / administration site | 11 | 7 | 1.573 |
| Metabolism and nutrition disorders | 4 | 12 | 0.334 |
| Pregnancy, puerperium, perinatal | 3 | 9 | 0.334 |

The bolded / >1.0 rows are filed as questions in `QUESTIONS.md` — small N, no CIs,
unadjusted; do not read as signals.

## By age band (as-treated)

| Age | Vaccine rate (N) | Placebo rate (N) | RR |
|---|---|---|---|
| 0–17 | 0.596% (1,509) | 0.332% (1,505) | 1.795 |
| 18–49 | 0.923% (9,971) | 1.049% (10,106) | 0.880 |
| 50–64 | 1.402% (7,135) | 1.509% (7,024) | 0.929 |
| 65+ | 2.700% (4,555) | 2.783% (4,563) | 0.970 |

Older bands balanced; the 0–17 RR rests on single-digit serious counts per arm
(noise-dominated — see limits).

## By sex (as-treated)

| Sex | Vaccine rate (N) | Placebo rate (N) | RR |
|---|---|---|---|
| Male | 1.530% (11,894) | 1.470% (11,704) | 1.041 |
| Female | 1.259% (11,276) | 1.496% (11,494) | 0.842 |

## Statistical rigor — CIs + multiplicity (the gate)

Every 2×2 above was re-run with a **risk-ratio 95% CI** (log method, Haldane
correction for zero cells), a **Fisher exact two-sided p**, and screened across all
**22 comparisons** with **Benjamini-Hochberg FDR** and Bonferroni
(`comparator_stats.py`). A cell is a candidate "signal" only if FDR q < 0.05 **and**
its CI excludes 1.0.

**Result: 0 of 22 comparisons survive.** None.

Key cells with their bounds (sorted by raw p):

| Cell | RR | 95% CI | Fisher p | FDR q | survives? |
|---|---|---|---|---|---|
| Hepatobiliary (the eye-catcher) | 2.253 | [0.98, 5.18] | 0.052 | 0.802 | no |
| Metabolism & nutrition | 0.334 | [0.108, 1.035] | 0.077 | 0.802 | no |
| Sex: Female | 0.842 | [0.675, 1.049] | 0.139 | 0.802 | no |
| Age 0–17 | 1.795 | [0.603, 5.344] | 0.423 | 0.856 | no |
| **OVERALL** | **0.943** | **[0.811, 1.096]** | 0.459 | 0.856 | no |
| Cardiac disorders | 1.044 | [0.70, 1.557] | 0.839 | 0.856 | no |
| Neoplasms | 1.074 | [0.702, 1.644] | 0.746 | 0.856 | no |

Every CI straddles 1.0; every FDR q ≈ 0.80–0.86. The raw ratios in the SOC/age/sex
tables — including the ones above 1.0 — are **noise once uncertainty and multiplicity
are accounted for.** That is the honest read: a balanced overall profile (RR 0.94,
CI 0.81–1.10) and **no sub-group difference that survives correction.** Full
per-cell stats in `data/phmpt_stats.json`.

## Attestation

| Artifact | SHA-256 (first 16) |
|---|---|
| `data/phmpt_comparator_actreated.json` | `39e85aa21eeb3326` |
| `data/phmpt_comparator_ITT.json` | `14135787bd6fd96c` |

Re-run the command in `README.md` against the PHMPT SDTM and you get byte-identical
JSON (deterministic). Full per-file SHAs in `MANIFEST_SHA256.txt`.
