import os
os.system("python scripts/clean_bls.py")
os.system("python scripts/clean_income.py")
os.system("python scripts/zillow_aggregation.py")
os.system("python scripts/merge_data.py")
os.system("python scripts/analysis.py")
print("Pipeline executed successfully.")
