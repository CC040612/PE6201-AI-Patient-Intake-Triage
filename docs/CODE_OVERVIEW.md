# Code Overview

## Primary files

- `notebooks/V2_Cross_Department_RAG.ipynb` is the final Colab demonstration and evaluation interface.
- `src/triage_v2.py` is the same core code extracted into a scan-friendly Python module.
- `notebooks/V1_Baseline_and_RAG.ipynb` preserves the named baseline, Version 1 system and original evidence path.

## Version 2 module structure

`src/triage_v2.py` is organized into documented sections:

1. Configuration and supported departments
2. Text normalization and feature extraction
3. Nested evidence-bundle reader
4. Source-traceable corpus construction
5. Balanced cross-department retriever
6. Rule-first emergency and scope guards
7. OpenRouter adapter and structured-output parsing
8. Output and evidence validation
9. Interactive Colab form
10. Metrics, checkpointed regression and evidence export

## Important interfaces

- `EvidenceBundle`: verifies and reads the Version 1 nested evidence archive.
- `build_v2_corpus()`: combines frozen Version 1 seeds with screened Step 3B candidates and preserves weak-label status.
- `BalancedRetriever`: calculates word and character TF-IDF similarities and returns evidence across all supported departments.
- `safety_decision()`: runs emergency rules before the model.
- `scope_decision()`: handles age, language, empty input, administrative encounters and prompt-injection patterns.
- `OpenRouterClient`: sends the validated request to the OpenRouter chat-completions endpoint.
- `validate_model_output()`: checks actions, departments, evidence IDs and exact symptom quotations.
- `V2System.route()`: public routing entry point.
- `run_regression()`: checkpointed paid evaluation; references are attached only after `route()` returns.
- `compute_metrics()`: reports routine accuracy, review, dangerous misses, false escalation, API usage and cost.

## Dependencies

The core retrieval, rule and API implementation uses the Python standard library. The Colab user interface uses `IPython`, `ipywidgets` and `google.colab`, which are available in the standard Colab runtime.

## Secrets

The notebook reads the OpenRouter key from the Colab secret named `API_KEY`. Do not place credentials in the notebook, source files, outputs or Git history.

## Reproducibility boundary

The local source, configuration, evidence corpus and stored outputs are frozen. The external hosted-model alias may change, so a future live rerun may differ. Use saved JSON results for auditing the reported run.
