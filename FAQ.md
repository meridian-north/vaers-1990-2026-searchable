# FAQ

Plain answers about what this dataset is, what it can and can't tell you, and
where the project honestly stands. If you only read one line: **these are
reports, not proof of cause; the counts are a floor, not a total; there is no
built-in denominator.** Everything below sits inside that frame.

---

## About the data

**What exactly is in here?**
A clean, searchable copy of public vaccine adverse-event reports, organized so
you can ask plain questions — who, what, when, where, and how (which vaccine,
lot, dose). It's built only from the **structured, coded fields**. The
free-text boxes from the originals — where phone numbers and addresses sometimes
appear — are not included.

**Is there any personal information?**
No. Free-text is excluded entirely, so nothing here points back to a person.
We treat every download link as if it could end up fully public, which is
exactly why the scrub — not the link — is the guarantee.

**Why are "current illness," "other medications," and "allergies" blank?**
Because that information lives in the free-text boxes, which we excluded to
guarantee no PII. The coded symptom terms we *do* carry describe the **reaction**,
not the patient's medical history.

**Could you capture diagnosis codes or prior conditions?**
The structured fields don't carry reliable diagnosis codes for prior
conditions — that history lives in the excluded free-text. Where a source
provides coded diagnoses, we can surface them. But *deriving* prior conditions
from what's coded today would be **inference, not fact**, and we won't present
inference as fact. (This is exactly where a clinician's guidance sharpens the
work.)

**Why so many columns (the ~69-column file)?**
That's simply the coded fields laid out flat so any spreadsheet or tool can read
them — nothing proprietary, nothing you need permission for.

**Is it only VAERS?**
No. The same treatment is applied across **seven systems in five countries** —
five national reporting systems (US VAERS, Australia TGA DAEN, the UK MHRA
Yellow Card, Canada CVAR, Japan JADER), plus the U.S. V-Safe active-monitoring
system and the Pfizer FOIA release (a different kind of source: trial documents,
not a national reporting system). All seven share one 69-column schema, so a
single query reaches every one — see the federation kit under `methods/`.

---

## How to trust it

**How do I know the numbers are real?**
You don't have to take our word. Every file has a SHA-256 fingerprint in a
version-controlled manifest; the full dataset reproduces from a single command;
and the actual reports behind any answer are right there to read. *Hard to
assemble, easy to verify.*

**How do I know the toolmaker is impartial?**
Impartiality is built into the *method*, not asked of the people. We publish
only the coded fields exactly as the agency recorded them, we never touch the
free-text, and every output carries a fingerprint you can reproduce yourself.
We can't put a thumb on the scale without the scale showing it.

---

## Where the project honestly stands

We'd rather show a small thing that works than a big thing that's promised.
**It is not a Rube Goldberg machine.** Here's the candid status:

| Capability | Status |
|---|---|
| Plain-question access to the data | **Working** |
| Provenance / verifiability | **Working** |
| PII scrubbing (coded fields only) | **Working** |
| Reproducibility ("same in, same out") | **Working — earned by repetition** |
| Federated method (one recipe, many agencies) | **Working proofs — 5 national systems, 5 countries, + Pfizer FOIA, published** |
| Bridging unrelated data sources | **Theoretical** |
| HIPAA compliance | **Aspirational — would require formal certification; not claimed** |

**Where the differences matter:**

- *Impartiality* — functional to the core (it's in the method, above).
- *The federation* — early, but with working proofs you can open today.
- *The repetition* — running the same inputs to the same outputs is what earns
  the "mil-spec" label; reproducibility is the feature.
- *Bridging seemingly unrelated sources* — still theoretical; we don't claim it.
- *Expanding the corpus* — more sources means more of the "who," widening the
  5W1H coverage over time.

**The old machinery, in one line each:**

- *Microtheories* — guardrails that keep the analysis on-topic and grounded
  (working, still developing).
- *BitNet* — the local engine that does the hard scoring work, cheaply and
  reproducibly.

---

## The "Why" — what we're building now

The four W's and the How tell you *what was reported*. The **Why** asks: is there
a real signal here worth a clinician's review? That's judgment, not calculation —
so the machine **triages**, and only a human **concludes.**

**What is it costing?** We'll be candid, including the restarts (we rebuilt the
machinery a few times getting it right):

- Deliberating the first ~3,000 reports individually cost **~2 million tokens**
  of local AI work.
- The full individual pass over ~2 million reports — the gold standard — is an
  estimated **~1.3 billion tokens: months** on our hardware. We expect to finish
  by **July**, on our own if we must.
- We also built an affordable shortcut — **cohort distillation** — that
  approximates the full Why for **tens of millions of tokens, in hours**, by
  grouping similar reports, deliberating a sample, and inheriting the verdict
  where the sample clearly agrees.

**Why bother?** Because the four W's are inventory and the Why is triage — a way
to narrow two million reports to the handful worth a clinician's attention. The
machine takes care of the data core so people can spend their time where only
people are any good.

---

*Assembled by GarrisonNode. The method travels with the data.*
