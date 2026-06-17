# The engine already exists — a short history of ESP and ESP:VAERS

*Why the "5-minute VAERS" isn't a moonshot: the hard part was built, proven, open-sourced, and is running at scale today — just not pointed at vaccine safety. Sourced, neutral on safety, strong on method.*

---

## 1. ESP — an open engine that reads the record and reports to public health

**ESP (Electronic Support for Public Health)** is an open-source software platform that reads near-real-time electronic health record data — diagnoses, lab results, prescriptions, vitals — and **automatically detects and reports** reportable conditions to public health authorities. It was developed at the **Department of Population Medicine, Harvard Pilgrim Health Care Institute** (Harvard Medical School), originally to automate **notifiable-disease reporting** (the legally required reports clinicians are supposed to file for things like measles, chlamydia, or tuberculosis — and mostly don't, because the manual process is slow).

ESP is not a prototype on a shelf. Today it is:

- **Open-source**, free to use under a **BSD-3-Clause** license, with the source on GitLab and an implementation kit. (esphealth.org · gitlab.com/ESP-Project/ESP)
- **Deployed in Massachusetts** in partnership with the state Department of Public Health (the MDPHnet project), **covering more than 60% of the state's population**.
- Part of the **CDC-funded Multi-state EHR-based Network for Disease Surveillance (MENDS)**.

In other words: a maintained, deployed, government-networked engine that already watches millions of people's records and files automated public-health reports. The "machine that reads the record and raises its hand" exists and runs every day.

## 2. ESP:VAERS — pointing that same engine at vaccine safety (2007–2011)

With an **AHRQ grant (R18 HS017045)**, the same team (Lazarus, Klompas, and colleagues) extended ESP to vaccine safety, producing **ESP:VAERS**. The method:

- For **every patient who received a vaccine**, the system automatically watched the next **30 days** of their record — diagnosis codes, lab results, and prescriptions — for values suggestive of an adverse event.
- When the algorithm flagged a plausible event, it **auto-generated a pre-populated electronic VAERS report** and could **securely transmit** it — no 30-minute form, no reliance on a busy clinician remembering to file.

It ran on **real data: about 1.4 million doses of 45 different vaccines given to 376,452 people** at a large Massachusetts ambulatory practice (under IRB and data-use agreements — this individual-level data is **not** public, as it is protected health information).

**What it found, and what it proved:**
- Roughly **2.6% of vaccinations** were followed by a possible adverse event the system could flag.
- It confirmed the long-standing estimate that **fewer than 1%** of vaccine adverse events are ever reported to VAERS today.
- It demonstrated that **automated detection and electronic reporting from the EHR is feasible** — the hard half of the problem.

## 3. What happened — and what didn't

The planned next step was a head-to-head evaluation comparing ESP:VAERS against existing VAERS and the Vaccine Safety Datalink. By the project's **own final report**, that evaluation could not proceed *"due to restructuring at CDC and consequent delays in decision-making."* The vaccine-reporting capability was not carried forward to national adoption.

To be precise and fair: this is the documented record. We make no claim about intent. What is not in dispute is the outcome — **a working, government-funded, automated vaccine-safety reporting system, proven on 1.4 million doses, was not deployed at national scale**, while the underlying engine went on to be open-sourced and deployed for *other* public-health reporting across an entire state.

## 4. Why this matters now

The usual framing — "fixing vaccine-safety reporting is hard" — does not survive contact with this history. The pieces exist:

- **The engine is open-source and running.** ESP covers 60%+ of Massachusetts and is in a CDC surveillance network today. Its maintainers state it *can* detect and report adverse vaccine events to VAERS.
- **The feasibility is proven.** ESP:VAERS showed it works, on real data, in 2011.
- **HIPAA permits it.** Reporting to VAERS is an explicitly permitted public-health disclosure (45 CFR 164.512(b); 42 U.S.C. 300aa-25) — no patient authorization required.
- **Modern standards make it more portable.** What needed custom EHR feeds in 2011 can now ride **FHIR / SMART-on-FHIR**, the vendor-neutral health-data standard built into today's major EHRs.

So the honest ask is not "invent a solution." It is: **connect the engine that already exists, open the loop, and point it at vaccine safety the way it is already pointed at measles and chlamydia.** Our "5-Minute VAERS" demo rebuilds the *visible entry half* of this on open modern standards so anyone can see how little it takes; ESP is the *detection half*, already built and open. Together they are the instrument.

> **The detection engine was built, proven on 1.4 million doses, open-sourced, and is running at scale for other diseases. It was simply never switched on for vaccine safety at national scale. Why not?**

---

*A navigator, not medical advice. The method is open; check it. Part of the Meridian North / Garrison Node open pharmacovigilance effort.*

**Sources:** AHRQ ESP:VAERS project page and final report (Lazarus, 2011) · "Automated Detection and Reporting of Vaccine Adverse Events: ESP-VAERS" · ESP / ESPHealth (esphealth.org · gitlab.com/ESP-Project/ESP) · MDPHnet / CDC MENDS · "Harnessing electronic health records for public health surveillance."
