# Updated Submission - NLP/GenAI Track

## Hypothesis Tested
The QA model performs significantly worse on questions containing negation.

## Measurement
Ran 150 examples with proper normalization (lowercase + removed articles).

Results:
- Simple questions: 0.78 accuracy
- Negation questions: 0.45 accuracy
- Difference: \~33% drop on negation

This confirms the hypothesis with numbers.

## Insights
Model often ignores "not" and picks the wrong entity. This matches what I observed.

## Next
Would create more negation examples for targeted improvement.

Thanks for the feedback - this was very helpful!
