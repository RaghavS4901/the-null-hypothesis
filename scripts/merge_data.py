import pandas as pd
zillow = pd.read_csv("data/zillow_home_values_yearly.csv")
bls = pd.read_csv("data/bls_clean.csv")
income = pd.read_csv("data/income_clean.csv")
zillow["state"] = zillow["state"].str.strip()
bls["state"] = bls["state"].str.strip()
income["state"] = income["state"].str.strip()
zillow["year"] = zillow["year"].astype(int)
bls["year"] = bls["year"].astype(int)
income["year"] = income["year"].astype(int)
merged = pd.merge(
    zillow,
    bls,
    on=["state", "year"],
    how="inner"
)
merged = pd.merge(
    merged,
    income,
    on=["state", "year"],
    how="inner"
)
merged.to_csv("data/final_merged.csv", index=False)
print(merged.head())
print("\nTotal rows:", len(merged))
print("\nSaved final merged dataset.")
