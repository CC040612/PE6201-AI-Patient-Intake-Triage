# Evaluation Explainer

## Evaluation set

`v1/frozen_new150_cases.json` contains the fixed 150-case synthetic set:

- 120 routine department-routing cases, balanced as 30 per implemented department
- 20 emergency challenge cases
- 10 review/scope cases

References were fixed before the original predictions and were not sent to the routing function. They were AI-authored and not independently clinician-reviewed.

## Metrics

- **Routine department accuracy:** correct department among all 120 routine references. `HUMAN_REVIEW` counts as incorrect.
- **Overall review rate:** `HUMAN_REVIEW` among all 150 cases. The predefined maximum was 12%.
- **Dangerous miss:** any reference emergency not returned as `EMERGENCY_ESCALATION`, including review.
- **False escalation:** a non-emergency reference returned as `EMERGENCY_ESCALATION`.
- **Rule-first emergency coverage:** reference emergencies escalated locally without an API call.
- **Action and department agreement:** exact action agreement and, for routed cases, department agreement.

## Frozen results

| Metric | Baseline | Version 1 RAG | Version 2 regression |
|---|---:|---:|---:|
| Routine department accuracy | 17.50% | 48.33% | 99.17% |
| Overall review rate | 76.00% | 51.33% | 6.67% |
| Dangerous misses | 7/20 | 6/20 | 0/20 |
| False escalations | 0/130 | 0/130 | 0/130 |
| Action and department agreement | 28.67% | 54.00% | 99.33% |

Version 2 made 126 API attempts, accepted 126 validated model outputs, used 147,809 provider-reported tokens and cost USD 0.0726176.

## Interpretation boundary

Version 1 failures on these cases were inspected and used to design Version 2. The Version 2 run is therefore a **development regression**, not an independent test. It shows that targeted engineering changes corrected known failure modes. It does not provide an unbiased estimate of generalisation to unseen complaints.

No case was deleted or relabelled after observing Version 2 results.

## Residual failures

- `N048` was routed to Orthopedics instead of Neurology. Generic foot and gait signals outweighed gait-initiation meaning.
- `N132` and `N135` were correctly escalated by the model, but not by deterministic red-flag rules. Thus overall dangerous misses were 0/20 while rule-first emergency coverage was 18/20.

## Files

### Version 1

- `v1/frozen_new150_cases.json`: inputs and provisional references
- `v1/new150_metrics.json`: baseline and Version 1 RAG metrics
- `v1/new150_results.json`: complete stored outputs
- `v1/new150_predictions.csv`: tabular predictions
- `v1/review_policy.md`: review and scoring policy
- `v1/final_run_manifest.json`: frozen run identity

### Version 2

- `v2/v2_regression_results.json`: all 150 Version 2 predictions
- `v2/v2_regression_metrics.json`: aggregate Version 2 metrics
- `v2/v2_candidate_regression_diagnostic.json`: retrieval-only development diagnostic; not RAG accuracy
- `v2/v2_cases_for_followup.csv`: N048, N132 and N135 follow-up ledger
- `v2/V2_REGRESSION_ANALYSIS.md`: detailed result interpretation

## Supplementary functional check

`../evidence/supplementary_not_reported/v1_functional24_evidence.zip` is preserved for transparency but was not used for the report's primary performance claim. It is a narrower functional check created after development and must not replace the fixed 150-case results.
