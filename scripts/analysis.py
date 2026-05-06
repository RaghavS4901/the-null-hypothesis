import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/final_merged.csv")
# Plot 1: Income vs Home Value
plt.figure(figsize=(8,6))
plt.scatter(
    df["median_income"],
    df["home_value"]
)
plt.xlabel("Median Income")
plt.ylabel("Home Value")
plt.title("Income vs Home Value")
plt.savefig("visualizations/income_vs_housing.png")
# Plot 2: Unemployment vs Home Value
plt.figure(figsize=(8,6))
plt.scatter(
    df["unemployment_rate"],
    df["home_value"]
)
plt.xlabel("Unemployment Rate")
plt.ylabel("Home Value")
plt.title("Unemployment vs Home Value")

plt.savefig("visualizations/unemployment_vs_housing.png")
# Plot 3: Top States by Home Value
top_states = df.sort_values(
    "home_value",
    ascending=False
).head(10)
plt.figure(figsize=(10,6))
plt.bar(
    top_states["state"],
    top_states["home_value"]
)
plt.xticks(rotation=45)
plt.xlabel("State")
plt.ylabel("Home Value")
plt.title("Top 10 States by Home Value")
plt.tight_layout()
plt.savefig("visualizations/housing_trend.png")
# Correlation matrix
print(df.corr(numeric_only=True))
print("\nAnalysis complete.")
