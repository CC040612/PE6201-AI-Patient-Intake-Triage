# Data Explainer

## Source

`raw/mtsamples_original from Kaggle.csv` is the supplied source dataset. Local validation found 4,999 rows and 40 source specialty labels. The file contains medical transcription narratives rather than reception-ready presenting complaints.

The original Kaggle page and redistribution licence were not independently verified in this project. The file is included for course assessment and reproducibility. Confirm the original source terms before making a public repository.

## Why mapping was required

The source label records a clinical specialty associated with a transcription. It is not automatically the correct walk-in destination. A versioned mapping was therefore created before indexing. `processed/01_specialty_mapping.csv` records every source label, its raw count and the candidate department or exclusion decision.

The implemented Version 2 scope contains four departments:

| Source specialty | Candidate department | V2 retrieval records |
|---|---|---:|
| Dermatology | Dermatology | 2 |
| Neurology | Neurology | 16 |
| Orthopedic | Orthopedics | 11 |
| Urology | Urology | 4 |

The initial mapping considered eight candidate departments. The operational prototype was reduced to four because reviewed evidence was insufficient for reliable development across all eight.

## Cleaning and extraction policy

- Preserve the raw source and source-row identity.
- Group normalized duplicates before selection.
- Extract complaints from identified `CHIEF COMPLAINT`, `HISTORY OF PRESENT ILLNESS` or declared subjective sections.
- Do not replace a missing complaint section with the entire medical record.
- Exclude pediatric, scheduled-procedure and administrative-only encounters from routine adult walk-in training.
- A follow-up with a genuine current symptom may remain.
- Ambiguous multi-symptom records require review rather than forced assignment.
- Keep extraction spans, methods, exclusion reasons and parent group IDs for audit.

## Version 2 retrieval corpus

`processed/v2_retrieval_corpus.csv` contains 33 group-deduplicated development records:

- 10 frozen Version 1 weak examples
- 23 screened, source-traceable Step 3B candidates

The `label_status` field explicitly identifies weak development labels. These records are not independently clinician-approved training examples and must not be described as clinical ground truth.

## Data files

| File | Role |
|---|---|
| `raw/mtsamples_original from Kaggle.csv` | Unmodified supplied source dataset |
| `processed/01_specialty_mapping.csv` | Pre-index specialty-to-department policy |
| `processed/09_audit_summary.json` | Cleaning counts and source audit |
| `processed/v2_retrieval_corpus.csv` | Final 33-record retrieval corpus |
| `manifests/v2_build_summary.json` | Corpus counts, source hashes, configuration and offline checks |

## Privacy and intended use

Only synthetic or de-identified course data should be used. The repository is not approved for real patient information or clinical deployment.
