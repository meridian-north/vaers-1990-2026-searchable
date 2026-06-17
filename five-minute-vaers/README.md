# 5-Minute VAERS — proof of concept

**The data the 30-minute VAERS form asks for already lives in the medical record. One click fills it in.**
Open-source · HIPAA-permitted · synthetic data · no backend.

▶ **Live demo:** https://meridian-north.github.io/vaers-1990-2026-searchable/five-minute-vaers/
(or just open `index.html` in any browser — no server, no build, no install)

## Why this exists

Fewer than **1%** of vaccine adverse events ever get reported to VAERS — largely because the form takes a clinician roughly **30 minutes** of manual re-entry of data the electronic health record *already holds in structured form*. The fix — auto-detect and auto-fill from the EHR — was built and proven in **2011** by an AHRQ-funded project (ESP:VAERS / Lazarus, Harvard Pilgrim) and then shelved. This demo shows how little it takes to do it.

## What this is (and isn't)

- **Is:** a synthetic-data front-end demo. Pick a fictional patient → **Import from record** → the VAERS form fills itself (age, sex, state, vaccine/lot/dose/site/date, history, meds, allergies, prior vaccines) → you add only the **event description, onset date, and outcomes** → **Generate**. A live timer contrasts 30:00 with ~0:30.
- **Isn't:** connected to any real EHR, and it submits nothing. Every patient is fictional (Synthea-style). No real PHI. This generates **no real report**.

## HIPAA permits this

Reporting adverse events to VAERS is a **permitted public-health disclosure** under **45 CFR 164.512(b)**, authorized by **42 U.S.C. 300aa-25** — no patient authorization required. HIPAA is a green light here, not a barrier. (Production deployments still need the standard safeguards: encryption, minimum-necessary, audit logging, a BAA where applicable, and a third-party security/HIPAA audit.)

## Run / fork

Open `index.html`. That's it. Fork it, audit it, improve it. The React 19 port plan is in `HANDOFF_react19_v0.1.md`.

## Status

- **v0.1** — vanilla single-file reference build (this repo).
- **v0.2** (planned) — live SMART-on-FHIR sandbox pull (SMART Health IT / Epic-on-FHIR), gated model-assisted MedDRA coding, and a dose-denominator join to turn counts into rates.

## The challenge

> **Working 5-minute VAERS. Open-source. HIPAA-permitted. Built in a weekend.**
> A 2011 government-funded project already proved auto-filing works, then shelved it. **Why isn't this the national system?**

---

A navigator, not medical advice. Part of the Meridian North / Garrison Node open pharmacovigilance effort —
see the companion corpus: https://meridian-north.github.io/vaers-1990-2026-searchable/kennedy-miller-kit/

License: MIT.
