import argparse
import csv
import json
import os
import random

INTENTS = [
    "account_access",
    "billing_payment",
    "technical_issue",
    "product_issue",
    "delivery_order",
    "other",
]

def classify(text):
    text = text.lower()

    if any(x in text for x in ["password", "login", "account", "sign in"]):
        return "account_access"
    if any(x in text for x in ["payment", "charge", "billing", "refund"]):
        return "billing_payment"
    if any(x in text for x in ["not working", "error", "crash", "bug"]):
        return "technical_issue"
    if any(x in text for x in ["iphone", "ipad", "mac", "product"]):
        return "product_issue"
    if any(x in text for x in ["order", "delivery", "shipping"]):
        return "delivery_order"

    return "other"

def reply(intent):
    replies = {
        "account_access": "Please check your account credentials and try signing in again.",
        "billing_payment": "We can help review the payment or billing issue.",
        "technical_issue": "Please restart the device and try the affected feature again.",
        "product_issue": "Please share the product details so the issue can be investigated.",
        "delivery_order": "Please share the order details so we can check the status.",
        "other": "Please provide more details so our support team can assist you.",
    }
    return replies[intent]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brand", default="AppleSupport")
    parser.add_argument("--sample", action="store_true")
    args = parser.parse_args()

    input_file = "data/sample_data.csv"
    output_file = "primary_eval.json"

    if not os.path.exists(input_file):
        print("sample_data.csv not found")
        return

    results = []

    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            text = row.get("text", row.get("tweet", ""))
            intent = classify(text)
            escalate = intent == "other"

            results.append({
                "text": text,
                "intent": intent,
                "reply": reply(intent),
                "should_escalate": escalate,
                "reason": "Unclear or unsupported request" if escalate else "Routine support request"
            })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Brand: {args.brand}")
    print(f"Processed examples: {len(results)}")
    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    main()