import pandas as pd
bls = pd.read_csv("data/bls_unemployment.csv", skiprows=5)
bls = bls.rename(columns={
    "Unnamed: 1": "state",
    "Unnamed: 2": "year",
    "Rate": "unemployment_rate"
})
bls = bls[["state", "year", "unemployment_rate"]]
bls = bls.dropna()
bls["year"] = pd.to_numeric(bls["year"], errors="coerce")
bls = bls[(bls["year"] >= 2019) & (bls["year"] <= 2023)]
bls["state"] = bls["state"].str.strip()
bls.to_csv("data/bls_clean.csv", index=False)
print(bls.head())
print("\nSaved cleaned dataset to data/bls_clean.csv")
