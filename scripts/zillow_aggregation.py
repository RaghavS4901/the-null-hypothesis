import pandas as pd
zillow = pd.read_csv("data/zillow_home_values.csv")
zillow = zillow.rename(columns={"RegionName": "state"})
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
zillow_yearly.to_csv("data/zillow_home_values_yearly.csv", index=False)
print(zillow_yearly.head())
print("\nSaved yearly Zillow file to data/zillow_home_values_yearly.csv")
