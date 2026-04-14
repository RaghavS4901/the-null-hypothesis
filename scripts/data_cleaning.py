import pandas as pd
zillow = pd.read_csv("data/zillow_home_values.csv")
print("Original Zillow dataset preview:")
print(zillow.head())
print("\nColumn names:")
print(zillow.columns.tolist()[:15]) 
zillow = zillow.rename(columns={"RegionName": "state"})
print("\nPreview after renaming RegionName to state:")
print(zillow[["state"]].head())
zillow_long = zillow.melt(
    id_vars=["state"],
    var_name="date",
    value_name="home_value"
)
zillow_long = zillow_long[zillow_long["date"].str.match(r"^\d{4}-\d{2}$", na=False)]
zillow_long["date"] = pd.to_datetime(zillow_long["date"], format="%Y-%m")
zillow_long["year"] = zillow_long["date"].dt.year
zillow_yearly = (
    zillow_long.groupby(["state", "year"], as_index=False)["home_value"]
    .mean()
)
print("\nYearly Zillow data preview:")
print(zillow_yearly.head())
zillow_yearly.to_csv("data/zillow_home_values_yearly.csv", index=False)
print("\nSaved yearly Zillow file to data/zillow_home_values_yearly.csv")
bls = pd.read_excel("data/bls_unemployment.csv")
print("\nBLS Data Preview:")
print(bls.head())
