# Version 2 Development Regression Analysis

## Status

The ZIP is complete and contains all 150 regression results. No API or output-validation errors were recorded.

## Main results

| Metric | V1 | V2 | Change |
|---|---:|---:|---:|
| Routine department accuracy | 48.33% (58/120) | 99.17% (119/120) | +50.84 percentage points |
| Overall review rate | 51.33% (77/150) | 6.67% (10/150) | -44.66 percentage points |
| Dangerous misses | 6/20 | 0/20 | -6 cases |
| False emergency escalations | 0/130 | 0/130 | unchanged |

V2 made 126 API calls, accepted 126 validated model outputs, used 147,809 tokens, and reported a total provider cost of $0.0726176. Median API-path latency was 1182.7 ms.

## Department results

| Department | Correct | Accuracy |
|---|---:|---:|
| Dermatology | 30/30 | 100.00% |
| Neurology | 29/30 | 96.67% |
| Orthopedics | 30/30 | 100.00% |
| Urology | 30/30 | 100.00% |

## Follow-up findings

- `N048` was the only routine mismatch. A gradually worsening hesitation before initiating a step was routed to Orthopedics rather than Neurology. This resembles gait initiation failure or freezing, but the orthopedic foot/gait concept and orthopedic retrieval score dominated.
- `N132` and `N135` were correctly escalated by the model, but the deterministic red-flag layer did not fire. They describe transient unilateral arm weakness and transient slurred speech. The rule layer should cover resolved or transient focal neurological symptoms so that these cases do not depend on the model.

## Interpretation boundary

These 150 cases were already inspected during Version 1 development and were used to design Version 2. The result is valid evidence of regression improvement, but it is not an independent or blind estimate of Version 2 accuracy. Report it as a development regression result and evaluate the frozen system on a new independently reviewed test set before making a final performance claim.
