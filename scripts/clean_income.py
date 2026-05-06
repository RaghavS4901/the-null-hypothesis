import pandas as pd
income = pd.read_csv("data/census_income.csv", skiprows=4)
income = income.rename(columns={
    "State": "state",
    "Value (Dollars)": "median_income"
})
income = income[["state", "median_income"]]
income = income[income["state"] != "United States"]
income = income.dropna()
income["year"] = 2023
income["median_income"] = (
    income["median_income"]
    .astype(str)
    .str.replace(",", "", regex=False)
)
income["median_income"] = pd.to_numeric(
    income["median_income"],
    errors="coerce"
)
income["state"] = income["state"].str.strip()
income.to_csv("data/income_clean.csv", index=False)
print(income.head())
print("\nSaved cleaned dataset to data/income_clean.csv")
