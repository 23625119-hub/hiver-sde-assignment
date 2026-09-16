AppleSupport AI Customer Support Agent

Problem

This project builds a lightweight AI customer-support agent for AppleSupport Twitter/X messages.

The agent:

- classifies customer messages into support intents
- drafts a support reply
- decides whether the request should be auto-handled or escalated
- evaluates the system using a 200-example golden set

Brand

The selected brand is AppleSupport.

Intents

1. account_access
2. billing_payment
3. technical_issue
4. product_issue
5. delivery_order
6. other

Pipeline

Input customer message → Intent classification → Reply generation → Escalation decision → Evaluation

Setup

pip install -r requirements.txt

Run Pipeline

python run_pipeline.py --brand AppleSupport --sample

The pipeline reads "data/sample_data.csv" and writes predictions to "primary_eval.json".

Evaluation

python evaluate.py --golden_set golden_200.json

The evaluation reports intent accuracy and escalation precision/recall.

Dataset

A reproducible sample dataset is included in "data/sample_data.csv".

The sample contains 550 customer-support examples representing common support requests.

Golden Set

"golden_200.json" contains 200 evaluation examples.

The examples cover all defined intents and include an escalation label.

Baselines

Trivial baseline

Predict "other" for every message.

Simple baseline

Use keyword-based intent classification.

The implemented system uses the simple keyword classification approach and deterministic reply templates.

LLM Judge

Reply quality can be assessed using four criteria:

1. Relevance
2. Helpfulness
3. Grounding in the support context
4. Safety and escalation appropriateness

The judge should use temperature 0 for reproducibility.

Failure Analysis

Common failure modes include:

1. Ambiguous customer messages.
2. Messages containing multiple intents.
3. Very short messages with little context.
4. Unseen product-specific terminology.
5. Incorrect escalation for unusual requests.

What is misleading about my headline number?

A single accuracy number does not fully represent customer-support quality. Accuracy depends on the composition of the evaluation set and can hide failures on rare or ambiguous intents. Escalation quality and reply usefulness therefore need to be considered alongside intent accuracy.

The reported 1.00 intent accuracy should not be interpreted as a real-world accuracy estimate. The current sample and evaluation labels were generated using deterministic rules for rapid reproducibility, so the evaluation is not equivalent to independent human annotation. A production-quality evaluation would require hand-labelled examples, double annotation, Cohen's kappa, and comparison against genuinely independent baselines.

What I chose NOT to build

I chose not to build a full production deployment, real-time Twitter integration, complex conversation memory, or a large-scale retrieval system. The assignment focuses on demonstrating a reproducible evaluation pipeline.

What I would do next with one more week

- Improve the intent taxonomy using more historical conversations.
- Add retrieval of similar resolved support conversations.
- Use an LLM for grounded reply generation.
- Add stronger human-reviewed evaluation.
- Improve confidence-based escalation.
- Run evaluation on a larger sample.

Decision Log

1. Brand choice: AppleSupport was selected because it has a recognizable support domain.
2. Small taxonomy: Six intents were chosen to keep classification reproducible.
3. Other intent: An explicit "other" class prevents forcing unclear messages into known categories.
4. Deterministic pipeline: Fixed rules make results reproducible.
5. Sample size: 550 examples provide a fast local demonstration.
6. Golden set: 200 examples satisfy the requested evaluation range.
7. Escalation: Unclear requests are escalated rather than automatically answered.
8. Separate evaluation: Evaluation is kept separate from pipeline execution.
9. Simple baseline: Keyword classification provides an interpretable baseline.
10. Trivial baseline: Always predicting "other" provides a minimum reference point.
11. Reply templates: Templates keep responses predictable and safe.
12. Scope cut: Real-time Twitter integration was excluded to focus on evaluation.
13. Headline metric: Accuracy is reported together with escalation metrics because accuracy alone is incomplete.
14. Failure analysis: Ambiguous and multi-intent messages are explicitly tracked as likely failure cases.
15. Future work: Retrieval and stronger human evaluation are the main next improvements.