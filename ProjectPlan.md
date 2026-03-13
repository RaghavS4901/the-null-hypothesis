# Project Plan

## Overview
The goal of this project is to study how economic conditions relate to housing prices across U.S. states over time. We want to understand whether differences in unemployment rates and median household income are associated with differences in home values.

To answer this question, we will combine three datasets where 2 are from the official government sites. First, we will use Zillow Home Value Index data to measure housing prices at the state level. Second, we will use BLS Local Area Unemployment Statistics to measure annual unemployment rates by state. Third, we will use U.S. Census data to measure median household income by state and year. Because these datasets share state and time information, they can be integrated into one combined dataset.

Our main approach will be to clean each dataset, standardize state names and year values, aggregate Zillow’s monthly data to yearly averages, and merge the data by state and year. After integration, we will perform exploratory data analysis using summary statistics and visualizations to examine patterns between housing prices, unemployment, and income. We may also compare trends across states and over time. The project will show how combining multiple datasets can provide a broader view of economic and housing patterns in the United States.

## Team

**Raghav**
- Find and download datasets
- Clean Zillow and BLS data
- Help write project documentation

**Vedha**
- Clean Census income data
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

### Dataset 1: Zillow Home Value Index
**Source:** Zillow Research Data  
**Description:** This dataset provides home value estimates across states and different monthly timeframes. We will use state level data as our main measure of housing prices. The data is available monthly, so we will aggregate it to yearly averages for integration.  
**Key attributes:** State, date, home value index/value  
**Role in project:** Main housing price outcome variable

### Dataset 2: Local Area Unemployment Statistics
**Source:** U.S. Bureau of Labor Statistics  
**Description:** This dataset provides unemployment rates for U.S. states. We will use annual average unemployment rates by state.  
**Key attributes:** State, year, unemployment rate  
**Role in project:** Economic condition indicator

### Dataset 3: Median Household Income by State
**Source:** U.S. Census Bureau  
**Description:** This dataset provides annual median household income estimates by state.  
**Key attributes:** State, year, median household income  
**Role in project:** Economic condition indicator

### Integration Plan
The datasets will be linked using shared variables: **state** and **year**. Since Zillow data is monthly, it will first be converted into yearly averages before merging with the annual unemployment and income datasets.

## Kaggle Clause

We are not using Kaggle datasets for this project. Instead, we selected data directly from Zillow Research, the U.S. Bureau of Labor Statistics, and the U.S. Census Bureau. These sources were chosen because they are official government figures, well documented, and have clearer provenance and licensing. They also better reflect real world data wrangling because the datasets come from different institutions and require cleaning and integration before analysis.

## Timeline

| Task | Description | When | Responsible |
|---|---|---|---|
| Finalize question and datasets | Confirm project scope and sources | Week 1 | Both |
| Download data | Obtain Zillow, BLS, and Census datasets | Week 1 | Both |
| Clean datasets | Standardize columns, state names, and years | Week 2 | Both |
| Aggregate Zillow data | Convert monthly housing data to yearly values | Week 2 | Raghav |
| Merge datasets | Integrate all datasets by state and year | Week 3 | Vedha |
| Exploratory analysis | Create summary statistics and visualizations | Week 3 | Both |
| Interpret findings | Identify trends and relationships | Week 4 | Both |
| Final revision | Update plan and prepare later milestone materials | Week 4 | Both |

## Constraints

This project may face several limitations. First, the Zillow dataset is monthly while the unemployment and income datasets are annual, so we will need to aggregate housing values to the yearly level. Second, state names or date formats may differ across sources and require standardization before merging. Third, some values may be missing for certain years or states. Finally, while these datasets can show relationships, they do not by themselves prove causation between economic conditions and housing prices.

## Gaps

At this stage, we still need to decide the exact year range for the analysis and confirm which version of the Zillow state-level file is most appropriate. We may also need additional guidance on whether to include more economic indicators later, such as population growth or inflation. As we learn more course methods, our project plan and analysis approach may evolve.
