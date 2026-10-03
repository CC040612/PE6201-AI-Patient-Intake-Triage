# AI Assisted Patient Intake and Triage

PE6201 final project by Tan Jingxuan.

This repository contains a classroom prototype that converts an adult patient's English walk-in complaint and age into one of three actions:

- `EMERGENCY_ESCALATION`
- `ROUTE_DEPARTMENT` for Dermatology, Neurology, Orthopedics or Urology
- `HUMAN_REVIEW`

The system is an educational decision-support prototype. It does not diagnose disease, recommend treatment or establish clinical readiness.

## Final system

Version 2 uses deterministic red-flag rules before model routing, cross-department word and character TF-IDF retrieval, an OpenRouter-hosted language model, and structured evidence validation. The final notebook is [`notebooks/V2_Cross_Department_RAG.ipynb`](notebooks/V2_Cross_Department_RAG.ipynb). Version 1 is retained to reproduce the named baseline and the documented failure analysis.

## Reported results

The fixed 150-case development regression set contains 120 routine cases, 20 emergency cases and 10 review/scope cases.

| Metric | Version 1 RAG | Version 2 regression |
|---|---:|---:|
| Routine department accuracy | 48.33% | 99.17% |
| Overall human-review rate | 51.33% | 6.67% |
| Dangerous misses | 6/20 | 0/20 |
| False emergency escalations | 0/130 | 0/130 |

These 150 cases were inspected after Version 1 and influenced Version 2. The Version 2 result demonstrates correction of known failures and is not an independent estimate of performance on unseen cases.

## Quick start in Google Colab

1. Open `notebooks/V2_Cross_Department_RAG.ipynb` in Colab.
2. Run the complete-code cell.
3. When prompted, upload `evidence/archives/version1_evidence.zip`.
4. In Colab Secrets, create a secret named `API_KEY` containing the course-provided **OpenRouter** key and enable notebook access.
5. Run the initialization and offline-check cells.
6. Run the interactive form and test a routine complaint, an emergency complaint and an out-of-scope complaint.
7. Keep `RUN_PAID_REGRESSION = False` unless intentionally reproducing the paid 150-case regression.
8. Export the generated evidence package from the last cell.

The notebook uses Python's standard library for retrieval and HTTP calls. Colab supplies `IPython`, `ipywidgets` and `google.colab` helpers.

## Local offline verification

The offline corpus build and safety checks do not call the API:

```bash
python scripts/offline_smoke_test.py evidence/archives/version1_evidence.zip
```

This creates a temporary local output folder, verifies the evidence archive, builds the 33-record corpus and runs deterministic checks. Live routing requires a valid OpenRouter key and may incur provider charges.

## Repository map

| Path | Purpose |
|---|---|
| `notebooks/` | Frozen Version 1 and final Version 2 Colab notebooks |
| `src/` | Scan-friendly Version 2 Python source |
| `data/` | Raw source, specialty mapping, final retrieval corpus and data manifest |
| `evals/` | Frozen cases, predictions, metrics, policies and failure analysis |
| `evidence/` | Original evidence archives and a clearly labelled supplementary run |
| `docs/PRODUCT.md` | Persona, inputs, outputs, architecture and metrics |
| `docs/CODE_OVERVIEW.md` | Module structure and important functions |
| `docs/DEMO_GUIDE.md` | Suggested five-minute demonstration flow |
| `report/` | Final project report |
| `SHA256SUMS.txt` | Integrity hashes for checked-in files |

## Documentation

- [Data explainer](data/README.md)
- [Evaluation explainer](evals/README.md)
- [Product documentation](docs/PRODUCT.md)
- [Code overview](docs/CODE_OVERVIEW.md)
- [Demo guide](docs/DEMO_GUIDE.md)

## Security and reproducibility

- No API key is stored in the repository.
- The code reads `API_KEY` from Colab Secrets.
- Reference answers are attached after routing when metrics are computed; they are not passed to `route()`.
- Exact artifact hashes are recorded in `SHA256SUMS.txt` and `submission_manifest.json`.
- Hosted model aliases may change over time, so a future rerun may not be bit-for-bit identical.
