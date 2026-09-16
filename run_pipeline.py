import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--brand", default="AppleSupport")
parser.add_argument("--sample", action="store_true")
args = parser.parse_args()

print("Customer Support Pipeline")
print("Brand:", args.brand)
print("Sample mode:", args.sample)

try:
    df = pd.read_csv("data/sample_data.csv")
    print("Total rows:", len(df))
except FileNotFoundError:
    print("No dataset found yet.")

print("Pipeline completed.")