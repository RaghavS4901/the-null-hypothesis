# Project Plan

## Overview
The goal of this project is to study how economic conditions relate to housing prices across U.S. states over time. We want to understand whether differences in unemployment rates and median household income are associated with differences in home values.

To answer this question, we will combine three datasets from reliable sources. First, we will use Zillow Home Value Index (ZHVI) data to measure housing prices at the state level. Second, we will use BLS Local Area Unemployment Statistics (LAUS) to measure unemployment rates by state. Third, we will use median household income data from HD Pulse (an NIH backed data platform) to measure income levels by state and year. Because these datasets share state and time information, they can be integrated into one combined dataset.

Our main approach will be to clean each dataset, standardize state names and year values, aggregate Zillow’s monthly data to yearly averages, and merge the data by state and year. After integration, we will perform exploratory data analysis using summary statistics and visualizations to examine patterns between housing prices, unemployment, and income. We may also compare trends across states and over time. The project will show how combining multiple datasets can provide a broader view of economic and housing patterns in the United States.

## Team

**Raghav**
- Find and download datasets  
- Clean Zillow and BLS data  
- Help write project documentation  

**Vedha**
- Clean income dataset  
- Merge datasets and perform analysis  
- Help write project documentation and interpretation  

**Shared responsibilities**
- Decide project scope  
- Review data quality  
- Finalize visuals, findings, and report  

## Research / Business Questions

1. How are housing prices related to unemployment rates across U.S. states?  
2. How are housing prices related to median household income across U.S. states?  
3. Do states with stronger economic conditions tend to have higher home values over time?  

## Datasets

### Dataset 1: Zillow Home Value Index (ZHVI)
**Source:** Zillow Research Data  
**Dataset Name:** ZHVI All Homes (SFR, Condo/Co-op) — State Level  
**Frequency:** Monthly  
**Time Range:** ~2000–present  

**Description:**  
This dataset provides home value estimates across U.S. states over time. It is structured in a wide format with monthly observations.

**Key attributes:**  
- RegionName (state)  
- Date (monthly)  
- Home value index  

**Role in project:**  
Main housing price outcome variable.

**Processing plan:**  
- Convert wide format to long format  
- Extract year from date  
- Aggregate monthly values into yearly averages  

### Dataset 2: Local Area Unemployment Statistics (LAUS)
**Source:** U.S. Bureau of Labor Statistics  
**Dataset Name:** Employment Status of the Civilian Noninstitutional Population — Annual Averages  
**Frequency:** Annual  
**Time Range:** 1976–present  

**Description:**  
This dataset provides unemployment rates across U.S. states. We will use the unemployment rate variable for analysis.

**Key attributes:**  
- State  
- Year  
- Unemployment rate  

**Role in project:**  
Economic condition indicator representing labor market performance.

### Dataset 3: Median Household Income by State
**Source:** HD Pulse (NIH-supported data platform)  
**Dataset Name:** Median Household Income (State Level)  
**Frequency:** Annual  
**Time Range:** 2019–2023  

**Description:**  
This dataset provides recent median household income estimates across U.S. states.

**Key attributes:**  
- State  
- Year  
- Median household income  

**Role in project:**  
Economic condition indicator representing income levels.

**Justification:**  
Recent Census income data was not easily accessible in a clean, downloadable format suitable for integration. HD Pulse provides recent, structured, and credible data supported by the NIH, making it appropriate for this analysis.

## Integration Plan

The datasets will be linked using shared variables:
- **State**
- **Year**

Because Zillow data is monthly, it will first be reshaped from wide to long format and then aggregated to yearly averages. All three datasets will then be standardized to use consistent state name formatting (full name, title case) and a consistent integer year column before merging. The final integrated dataset will have one row per state-year combination with columns for home value index, unemployment rate, and median household income.

## Kaggle Clause

We are not using Kaggle datasets for this project. Instead, we selected data directly from Zillow Research, the U.S. Bureau of Labor Statistics, and HD Pulse (NIH backed). These sources were chosen because they are credible, well documented, and have clearer provenance and licensing. They also better reflect real world data wrangling because the datasets come from different institutions and require cleaning and integration before analysis.

## Timeline

 Task | Description | When | Responsible |
|---|---|---|---|
| Finalize questions and datasets | Confirm project scope and verify dataset access | Week 1 | Both |
| Download and inspect data | Obtain all three datasets; review schemas and formats | Week 1 | Both |
| Clean Zillow dataset | Melt wide to long, extract year, aggregate to yearly averages | Week 2 | Raghav |
| Clean BLS LAUS dataset | Standardize columns, filter to relevant years | Week 2 | Raghav |
| Clean HD Pulse income dataset | Standardize state names and year formats | Week 2 | Raghav |
| Integrate datasets | Merge all three on state and year using Pandas | Week 3 | Vedha |
| Data quality assessment | Check for missing values, outliers, coverage gaps | Week 3 | Vedha |
| Exploratory data analysis | Summary statistics and visualizations | Week 3 | Vedha |
| Automate workflow | Write end-to-end script or Makefile | Week 4 | Both |
| Interpret findings | Identify trends and draft conclusions | Week 4 | Both |
| Write final report and metadata | Finalize documentation, data dictionary, README | Week 4 | Both |
 

## Constraints

This project may face several limitations. The following constraints are grounded in challenges discussed across course modules:

1. Temporal alignment (Data Integration): Zillow data is monthly while BLS and HD Pulse data are annual. This requires aggregation before merging and introduces potential information loss if monthly patterns matter.

2. Schema heterogeneity (Schema-level Integration): The three datasets come from different institutions with different column naming conventions, formats (wide vs. long), and data types, requiring careful schema normalization before integration.

3. Limited temporal coverage  (Data Quality): HD Pulse income data is only available from 2019–2023, which restricts the common overlapping time window across all three datasets to five years. This limits longitudinal analysis.

4. Data completeness (Data Quality): Some state-year combinations may have missing values in one or more datasets. Missing data will be documented and handled using appropriate methods discussed in the data cleaning module.

5. Provenance traceability: HD Pulse aggregates data from the Census Bureau ACS, meaning our dataset is one step removed from the original source. We will document this lineage explicitly in our provenance records

6. Reproducibility (Reproducibility and Transparency): Zillow data requires a manual download from their research portal, which may not be fully automatable. We will document the exact download URL, file name, and date accessed to support reproducibility.


## Gaps

At this stage, we still need to:

- Exact overlapping time period: We need to confirm the final shared time range across all three datasets after cleaning, which will likely be 2019–2023 based on HD Pulse coverage.

- State coverage consistency: We need to verify whether all 50 states (plus D.C.) are present in all three datasets across the overlapping years, and decide how to handle any missing states.

- Additional control variables: We have not yet determined whether variables such as inflation, population size, or regional cost-of-living adjustments should be incorporated. These decisions will be made after initial exploratory analysis.
  
- Confirm the final merged dataset structure  
 

As we apply course concepts related to data cleaning, transformation, and integration, our approach may continue to evolve.
