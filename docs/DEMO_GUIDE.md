# Five Minute Demo Guide

The submitted video should show the presenter's face and computer screen.

## Suggested flow

1. **Problem and persona — 30 seconds**  
   Explain that reception staff receive colloquial complaints and need a provisional department without missing red flags.

2. **Architecture — 45 seconds**  
   Show the diagram in `PRODUCT.md`: rules first, then scope guards, retrieval, OpenRouter, validation and final action.

3. **Routine route — 60 seconds**  
   Use: `My shoulder has hurt for three months and throwing makes it worse.`  
   Show Orthopedics, retrieved evidence ID and validated symptom quotations.

4. **Emergency rule — 60 seconds**  
   Use: `My chest feels tight and my left arm suddenly became weak.`  
   Show `EMERGENCY_ESCALATION`, rule hits and `api_called: false`.

5. **Human review — 45 seconds**  
   Use an out-of-scope or administrative complaint. Explain why abstention is a designed safety outcome and why the measured 6.67% rate remains below the 12% target.

6. **Metrics and critique — 60 seconds**  
   Show the Version 1 versus Version 2 table. State 99.17% routine accuracy, 6.67% review, zero dangerous misses and zero false escalations. Immediately state that this is a development regression, not an independent test.

7. **Rough edges — 30 seconds**  
   Mention N048 gait initiation and the two transient neurological emergencies that still depended on the model.

Keep the final video under eight minutes. Do not display the OpenRouter key or Colab Secrets value.
