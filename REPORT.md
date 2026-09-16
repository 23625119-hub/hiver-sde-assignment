Hiver SDE Intern Take-Home Assignment Report

1. Problem Framing

The goal is to build a customer-support agent for AppleSupport Twitter/X messages.

A good system should correctly identify the customer's intent, provide a useful response, and escalate unclear requests to a human instead of confidently giving an inappropriate answer.

The project focuses on a small reproducible sample and an automated evaluation harness.

2. System

The pipeline performs four steps:

1. Intent classification.
2. Reply generation.
3. Escalation decision.
4. Evaluation.

The current implementation uses deterministic classification and response templates so that the experiment can be reproduced quickly.

3. Evaluation

The evaluation set contains 200 examples.

The main metrics are:

- Intent accuracy
- Macro-level intent performance
- Escalation precision
- Escalation recall

A separate golden set is used so that evaluation examples are not generated from model predictions.

4. Baselines

Two baselines are considered.

Trivial baseline: Always predict "other".

Simple baseline: Keyword-based intent classification.

The main pipeline is also based on deterministic keyword classification, making it easy to reproduce and inspect.

5. Failure Analysis

Ambiguous messages

Short messages may not provide enough information to identify an intent.

Multiple intents

A customer may mention billing and a technical problem in the same message.

Very short messages

Messages such as "help" contain insufficient context.

Unseen terminology

The classifier may fail when customers use terminology that is not represented by the keyword rules.

Escalation errors

Some unusual requests may be incorrectly auto-handled or escalated.

6. What is misleading about my headline number?

Intent accuracy alone can give an incomplete picture of customer-support quality.

A dataset with many easy examples can produce a high accuracy while hiding poor performance on ambiguous or less frequent intents.

Therefore, intent performance should be considered together with escalation metrics and reply quality.

7. What I Chose NOT to Build

I did not build:

- real-time Twitter integration
- a production web deployment
- complex long-term conversation memory
- a large retrieval infrastructure
- a full enterprise monitoring system

These were intentionally excluded to keep the assignment reproducible within the available time.

8. What I Would Do Next With One More Week

I would improve the system by:

1. Building a stronger intent taxonomy from more historical conversations.
2. Retrieving similar resolved conversations before generating replies.
3. Using an LLM for grounded response generation.
4. Adding confidence-based escalation.
5. Increasing human-reviewed evaluation.
6. Measuring performance across different time periods.

9. Conclusion

The project demonstrates a complete reproducible support-agent workflow from customer message to intent, response, escalation decision, and evaluation.

The main limitation is that the current classifier is intentionally simple. The evaluation framework provides a foundation for replacing it with a stronger LLM or retrieval-based system while keeping the same evaluation process.