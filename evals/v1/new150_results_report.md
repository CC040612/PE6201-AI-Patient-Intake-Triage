# Frozen-system evaluation on 150 new AI-authored cases

Completed: 150/150. References: provisional, not human-reviewed. Independent clinical evaluation: No.

The application is the exact frozen Step 8 source. No new-case outcomes were used to modify it. The case author knew the development process, so this is a separate synthetic evaluation, not an independent test. Repeated symptom families may make cases correlated.

| Metric | Baseline | RAG |
|---|---:|---:|
| reference_emergency_count | 20 | 20 |
| dangerous_misses | 7 | 6 |
| emergency_to_department | 1 | 0 |
| emergency_to_human_review | 6 | 6 |
| false_escalations | 0 | 0 |
| reference_routine_count | 120 | 120 |
| department_accuracy | 0.175 | 0.48333333333333334 |
| routine_routing_coverage | 0.175 | 0.48333333333333334 |
| selective_department_accuracy | 1.0 | 1.0 |
| human_review_rate | 0.76 | 0.5133333333333333 |
| routine_review_rate | 0.825 | 0.5166666666666667 |
| observed_overall_review_at_most_12_percent | False | False |
| observed_routine_review_at_most_12_percent | False | False |
| api_attempts | 0 | 61 |
| validated_llm_outputs | 0 | 60 |
| integration_error_count | 0 | 1 |
| api_path_mean_latency_ms | None | 1472.5451967213114 |
| known_provider_reported_cost | None | 0.0221164 |
| calls_without_cost | 0 | 0 |

The original 12% target is reported on the overall planned mixture, with routine-only review shown separately. Neither rate estimates a real walk-in population. Emergency-to-review counts as a missed escalation. Post-outcome relabeling is prohibited for the primary analysis. Record disputed labels separately; any sensitivity analysis must retain original results. Any partial run is incomplete and cannot establish a full-set result.

The policy requires review for instruction-bearing complaints, but frozen Step 8 has a known compliance gap. Count such deviations rather than silently overriding the system. Model alias/provider behavior can change even when client source is frozen. Preserve the notebook, raw observations and manifests.