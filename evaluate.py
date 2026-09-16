import argparse
import json
from collections import Counter


def f1_score(p, r):
    if p + r == 0:
        return 0
    return 2 * p * r / (p + r)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--golden_set", default="golden_200.json")
    args = parser.parse_args()

    with open(args.golden_set, encoding="utf-8") as f:
        golden = json.load(f)

    with open("primary_eval.json", encoding="utf-8") as f:
        pred = json.load(f)

    n = min(len(golden), len(pred))

    correct = 0
    actual = Counter()
    predicted = Counter()

    for i in range(n):
        actual[golden[i]["intent"]] += 1
        predicted[pred[i]["intent"]] += 1

        if golden[i]["intent"] == pred[i]["intent"]:
            correct += 1

    accuracy = correct / n if n else 0

    f1_values = []

    for intent in actual:
        tp = sum(
            1
            for i in range(n)
            if golden[i]["intent"] == intent and pred[i]["intent"] == intent
        )

        fp = sum(
            1
            for i in range(n)
            if golden[i]["intent"] != intent and pred[i]["intent"] == intent
        )

        fn = sum(
            1
            for i in range(n)
            if golden[i]["intent"] == intent and pred[i]["intent"] != intent
        )

        precision = tp / (tp + fp) if tp + fp else 0
        recall = tp / (tp + fn) if tp + fn else 0

        f1_values.append(f1_score(precision, recall))

    macro_f1 = sum(f1_values) / len(f1_values)

    true_escalate = sum(1 for i in range(n) if golden[i]["should_escalate"])
    predicted_escalate = sum(1 for i in range(n) if pred[i]["should_escalate"])
    correct_escalate = sum(
        1
        for i in range(n)
        if golden[i]["should_escalate"] and pred[i]["should_escalate"]
    )

    escalation_precision = (
        correct_escalate / predicted_escalate if predicted_escalate else 0
    )

    escalation_recall = correct_escalate / true_escalate if true_escalate else 0

    print("\nEvaluation Results")
    print("==================")
    print("Examples:", n)
    print("Intent Accuracy:", round(accuracy, 3))
    print("Macro F1:", round(macro_f1, 3))
    print("Escalation Precision:", round(escalation_precision, 3))
    print("Escalation Recall:", round(escalation_recall, 3))


if __name__ == "__main__":
    main()