import argparse
import json
from collections import Counter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--golden_set", default="golden_200.json")
    args = parser.parse_args()

    with open(args.golden_set, encoding="utf-8") as f:
        golden = json.load(f)

    with open("primary_eval.json", encoding="utf-8") as f:
        predictions = json.load(f)

    n = min(len(golden), len(predictions))

    correct = 0
    true_escalate = 0
    predicted_escalate = 0
    correct_escalate = 0

    for i in range(n):
        if golden[i]["intent"] == predictions[i]["intent"]:
            correct += 1

        actual = golden[i]["should_escalate"]
        predicted = predictions[i]["should_escalate"]

        if actual:
            true_escalate += 1
        if predicted:
            predicted_escalate += 1
        if actual and predicted:
            correct_escalate += 1

    accuracy = correct / n if n else 0
    precision = correct_escalate / predicted_escalate if predicted_escalate else 0
    recall = correct_escalate / true_escalate if true_escalate else 0

    print("Evaluation Results")
    print("------------------")
    print("Examples:", n)
    print("Intent Accuracy:", round(accuracy, 3))
    print("Escalation Precision:", round(precision, 3))
    print("Escalation Recall:", round(recall, 3))


if __name__ == "__main__":
    main()