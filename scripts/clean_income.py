import pandas as pd
income = pd.read_csv("data/census_income.csv", skiprows=4)
print(income.head(20))
print("\nColumns:\n")
print(income.columns)
