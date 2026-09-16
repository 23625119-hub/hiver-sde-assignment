import csv
import json
import random

INTENTS = [
    "account_access",
    "billing_payment",
    "technical_issue",
    "product_issue",
    "delivery_order",
    "other",
]


def main():
    with open("data/sample_data.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    random.seed(42)
    sample = random.sample(rows, 50)

    labels = []

    print("50-example annotation set")
    print("Intents:", ", ".join(INTENTS))
    print()

    for i, row in enumerate(sample, 1):
        text = row.get("text", row.get("tweet", ""))
        print(f"{i}. {text}")
        print("Choose:", ", ".join(INTENTS))
        label = input("Label: ").strip()

        while label not in INTENTS:
            print("Invalid label. Choose from the listed intents.")
            label = input("Label: ").strip()

        labels.append({"text": text, "intent": label})

    with open("double_label_set.json", "w", encoding="utf-8") as f:
        json.dump(labels, f, indent=2)

    print("\nSaved 50 labels to double_label_set.json")


if __name__ == "__main__":
    main()