rule clean_bls:
    input:
        "data/bls_unemployment.csv"
    output:
        "data/bls_clean.csv"
    shell:
        "python scripts/clean_bls.py"
rule clean_income:
    input:
        "data/census_income.csv"
    output:
        "data/income_clean.csv"
    shell:
        "python scripts/clean_income.py"
rule zillow:
    input:
        "data/zillow_home_values.csv"
    output:
        "data/zillow_home_values_yearly.csv"
    shell:
        "python scripts/zillow_aggregation.py"
rule merge:
    input:
        "data/bls_clean.csv",
        "data/income_clean.csv",
        "data/zillow_home_values_yearly.csv"
    output:
        "data/final_merged.csv"
    shell:
        "python scripts/merge_data.py"
rule analysis:
    input:
        "data/final_merged.csv"
    output:
        "visualizations/income_vs_housing.png",
        "visualizations/unemployment_vs_housing.png",
        "visualizations/housing_trend.png"
    shell:
        "python scripts/analysis.py"
