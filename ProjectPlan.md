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

Since Zillow data is monthly, it will first be converted into yearly averages before merging with the annual unemployment and income datasets. All datasets will be standardized to ensure consistent state naming and time formats prior to merging.

## Kaggle Clause

We are not using Kaggle datasets for this project. Instead, we selected data directly from Zillow Research, the U.S. Bureau of Labor Statistics, and HD Pulse (NIH backed). These sources were chosen because they are credible, well documented, and have clearer provenance and licensing. They also better reflect real world data wrangling because the datasets come from different institutions and require cleaning and integration before analysis.

## Timeline

| Task | Description | When | Responsible |
|---|---|---|---|
| Finalize question and datasets | Confirm project scope and sources | Week 1 | Both |
| Download data | Obtain Zillow, BLS, and income datasets | Week 1 | Both |
| Clean datasets | Standardize columns, state names, and years | Week 2 | Both |
| Aggregate Zillow data | Convert monthly housing data to yearly values | Week 2 | Raghav |
| Merge datasets | Integrate all datasets by state and year | Week 3 | Vedha |
| Exploratory analysis | Create summary statistics and visualizations | Week 3 | Both |
| Interpret findings | Identify trends and relationships | Week 4 | Both |
| Final revision | Update plan and prepare later milestone materials | Week 4 | Both |

## Constraints

This project may face several limitations:

- **Temporal alignment:** Zillow data is monthly while other datasets are annual, requiring aggregation  
- **Data structure differences:** Zillow data is in wide format while other datasets are in long format, requiring transformation  
- **Data completeness:** Some states or years may have missing values, which may affect analysis  
- **Limited time overlap:** Income data is only available for 2019–2023, which restricts the common time window across datasets  

These constraints reflect common challenges in data integration and will be addressed through preprocessing and careful analysis.

## Gaps

At this stage, we still need to:

- Finalize the exact overlapping time period for analysis  
- Confirm the final merged dataset structure  
- Evaluate whether additional variables (e.g., inflation or population) should be included  

As we apply course concepts related to data cleaning, transformation, and integration, our approach may continue to evolve.
