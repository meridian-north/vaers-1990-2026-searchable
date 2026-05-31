#!/usr/bin/env python3
"""
make_reader_sample_csv.py -- build a reader-facing VAERS sample CSV in the
69-column format from the structured master index.

WHY: the full vaers_1990_2026_69col.csv is ~2M rows / ~1.2 GB -- nobody downloads
that to "test" it. This produces a small, complete, deterministic (seed=42)
sample. It reads ONLY the structured master index (no free-text / narrative
fields), so the output carries no personal information.

USAGE:
  python3 make_reader_sample_csv.py --limit 300 --out vaers_sample_300.csv
  python3 make_reader_sample_csv.py --year 2021 --vaccine COVID19 --limit 500 --out covid_2021.csv
  python3 make_reader_sample_csv.py --symptom myocard --out myocarditis.csv
  python3 make_reader_sample_csv.py --id-file cohort_ids.txt --out cohort.csv

Outputs <out>.csv (69 cols) + <out>.sha256 + <out>.manifest.json.
(For sampling directly from the full 69-col CSV instead of the index, see
build_extracts.py -- that's the simpler path when you already have the full file.)
"""
import argparse, csv, hashlib, json, random, sys
from pathlib import Path
from datetime import datetime, timezone

COLUMNS = [
    "gn_id","gn_sha256","gn_produced_at","gn_schema_class","gn_bitnet_signal",
    "gn_chain_ref","gn_source_class","gn_runner_seed","gn_source_jurisdiction",
    "gn_lot_number","gn_mfr_name","gn_vaccine_name","gn_dose_number",
    "gn_report_date","gn_onset_date","gn_state_region","gn_age_years","gn_sex",
    "gn_outcome_died","gn_outcome_serious","gn_outcome_er","gn_symptoms_primary",
    "gn_join_thread","who_reporter_class","who_underlying","what_symptoms_full",
    "what_outcome_lt","what_outcome_hosp_days","what_outcome_disabling",
    "what_outcome_recovered","what_outcome_recovering","when_vax_date",
    "when_received_date","when_days_to_onset","where_admin_site","where_country",
    "why_current_illness","why_medications","why_allergies","why_prior_vaccines",
    "how_vaccines_full","how_study_design","how_survey_instrument","gn_dsf_value",
    "gn_group_inherited","gn_cohort_id","bitnet_t1_ternary","bitnet_t2_ternary",
    "bitnet_t3_ternary","bitnet_rationale","gn_proxy_verdict","gn_retro_scored",
    "gn_milspec_seed","gn_schema_fingerprint","gn_sweep_run_id",
    "gn_chain_block_type","gn_source_provenance","gn_loom_thread_a",
    "gn_loom_thread_b","gn_loom_thread_c","gn_loom_thread_d","gn_empty_a",
    "gn_empty_b","gn_mt_membership","flag_pack","cohort_or_join_thread",
    "beacon_trace","aletheia_methodology","gn_spare",
]
assert len(COLUMNS) == 69, len(COLUMNS)
PRODUCED = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def iso(d):
    if not d:
        return ""
    try:
        return datetime.strptime(d, "%m/%d/%Y").strftime("%Y-%m-%d")
    except ValueError:
        return d


def norm_mfr(m):
    return (m or "").strip().lower().replace("\\", "/")


def pipe(xs):
    return "|".join(x for x in (xs or []) if x not in (None, ""))


def recovered_flag(v):
    return "1" if v == "Y" else ("0" if v == "N" else "")


def row_from_index(r):
    eid = r.get("envelope_id", "")
    src_sha = hashlib.sha256(
        json.dumps(r, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    dose = (r.get("vax_dose_series") or [""])
    symptoms = r.get("symptom_terms") or []
    out = {c: "" for c in COLUMNS}
    out.update({
        "gn_id": eid, "gn_sha256": src_sha, "gn_produced_at": PRODUCED,
        "gn_schema_class": "clause_envelope_v1", "gn_source_class": "vaers",
        "gn_runner_seed": "42", "gn_source_jurisdiction": "US",
        "gn_lot_number": pipe(r.get("vax_lots")),
        "gn_mfr_name": "|".join(norm_mfr(m) for m in (r.get("vax_manus") or [])),
        "gn_vaccine_name": pipe(r.get("vax_types")),
        "gn_dose_number": dose[0] if dose else "",
        "gn_report_date": iso(r.get("recvdate")), "gn_onset_date": iso(r.get("onset_date")),
        "gn_state_region": r.get("state") or "", "gn_age_years": r.get("age_yrs") or "",
        "gn_sex": r.get("sex") or "",
        "gn_outcome_died": "1" if r.get("died") else "0",
        "gn_outcome_serious": "1" if (r.get("hospital") or r.get("l_threat")) else "0",
        "gn_outcome_er": "1" if r.get("er_visit") else "0",
        "gn_symptoms_primary": symptoms[0] if symptoms else "", "gn_join_thread": eid,
        "who_reporter_class": r.get("reporter_class") or "",
        "what_symptoms_full": pipe(symptoms),
        "what_outcome_lt": "1" if r.get("l_threat") else "0",
        "what_outcome_disabling": "1" if r.get("disable") else "0",
        "what_outcome_recovered": recovered_flag(r.get("recovered")),
        "when_vax_date": iso(r.get("vax_date")), "when_received_date": iso(r.get("recvdate")),
        "when_days_to_onset": r.get("numdays") or "",
        "where_admin_site": r.get("v_adminby") or "", "where_country": "US",
        "how_vaccines_full": pipe(r.get("vax_names")),
        "gn_retro_scored": "0", "gn_milspec_seed": "42", "gn_source_provenance": "TRIBE-1 CDC",
    })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", default=str(Path.home() /
        "garrison/pharmacovigilance/vaers/index/vaers_envelopes_master_index.jsonl"))
    ap.add_argument("--out", default="vaers_reader_sample.csv")
    ap.add_argument("--limit", type=int, default=250)
    ap.add_argument("--year", type=int)
    ap.add_argument("--vaccine")
    ap.add_argument("--symptom")
    ap.add_argument("--id-file")
    ap.add_argument("--seed", type=int, default=42)
    a = ap.parse_args()

    ids = {ln.strip() for ln in open(a.id_file)} if a.id_file else None
    idx = Path(a.index)
    if not idx.exists():
        sys.exit(f"master index not found: {idx}")

    matches = []
    with open(idx, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if a.year and r.get("source_year") != a.year:
                continue
            if a.vaccine and not any(a.vaccine.lower() in (t or "").lower()
                                     for t in (r.get("vax_types") or [])):
                continue
            if a.symptom and not any(a.symptom.lower() in (s or "").lower()
                                     for s in (r.get("symptom_terms") or [])):
                continue
            if ids is not None and not (r.get("envelope_id") in ids or r.get("vaers_id") in ids):
                continue
            matches.append(r)

    if ids is None and len(matches) > a.limit:
        random.Random(a.seed).shuffle(matches)
        matches = matches[:a.limit]
        matches.sort(key=lambda r: r.get("envelope_id", ""))

    out = Path(a.out)
    with open(out, "w", newline="", encoding="utf-8") as o:
        w = csv.DictWriter(o, fieldnames=COLUMNS)
        w.writeheader()
        for r in matches:
            w.writerow(row_from_index(r))

    file_sha = hashlib.sha256(out.read_bytes()).hexdigest()
    out.with_suffix(out.suffix + ".sha256").write_text(f"{file_sha}  {out.name}\n")
    out.with_name(out.stem + ".manifest.json").write_text(json.dumps({
        "schema": "garrison/reader_sample_manifest/v1", "produced_at": PRODUCED,
        "source": "vaers master index (structured, no personal information)",
        "rows": len(matches), "columns": 69, "runner_seed": a.seed,
        "filters": {"year": a.year, "vaccine": a.vaccine, "symptom": a.symptom,
                     "id_file": a.id_file, "limit": a.limit},
        "bitnet_scored": False, "csv_sha256": file_sha,
    }, indent=2))
    print(f"wrote {len(matches)} rows -> {out}\nsha256 {file_sha}")


if __name__ == "__main__":
    main()
