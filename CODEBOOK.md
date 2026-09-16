# Codebook

## Intent Definitions

- account_access: Login, password, or account access problems.
- billing_payment: Charges, payments, refunds, or billing issues.
- technical_issue: App errors, crashes, or technical problems.
- product_issue: Problems with an Apple product or product feature.
- delivery_order: Order, shipping, or delivery questions.
- other: Requests that do not clearly fit another intent.

## Escalation

Routine and clearly understood requests are auto-handled.

Unclear, unsupported, or ambiguous requests are escalated to a human.

## Sampling

A 200-example evaluation set was created from the sample data.
The examples were selected using a fixed deterministic process.

## Edge Cases

If a message contains multiple possible intents, the most directly stated
customer problem is selected. If no intent can be identified confidently,
the example is labelled as other.