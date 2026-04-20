# Status Report

## 1. Progress Update on Project Tasks

### Task 1: Finalize Question and Datasets — Completed
The research questions and datasets were finalized in Milestone 2. The goal of this project is to analyze how housing prices are related to economic indicators such as unemployment rates and median household income across U.S. states over time. This focus allows us to explore both cross sectional differences between states and trends over time.

We confirmed the use of three datasets:
- Zillow Home Value Index (ZHVI) for state-level housing prices
- BLS Local Area Unemployment Statistics (LAUS) for annual unemployment rates
- HD Pulse Median Household Income (sourced from U.S. Census Bureau ACS 1-Year Estimates) for income levels

Artifacts:
- ProjectPlan.md

### Task 2: Data Acquisition — Completed
All required datasets have been successfully identified and collected from reliable and authoritative sources. The Zillow dataset provides monthly housing price data at the state level. The BLS dataset provides unemployment rate data across states over multiple years. The income dataset was obtained from HD Pulse, an NIH supported data platform, and contains recent median household income values (2019–2023).

These datasets collectively provide a strong foundation for analyzing relationships between economic conditions and housing prices.

Artifacts:
- data/zillow_home_values.csv
- data/bls_unemployment.xlsx
- data/census_income.csv

### Task 3: Data Cleaning — Mostly Completed
We have completed most of the initial data cleaning process. This included inspecting each dataset to understand its structure, identifying relevant variables, and standardizing column formats. We ensured that state names are consistent across datasets and that columns are clearly labeled for future processing.

We also explored the presence of missing values and inconsistencies. While some datasets contain minor gaps, they are manageable and will be handled during the integration and analysis stages.

These cleaning steps were critical to preparing the datasets for merging and ensuring compatibility across sources.

Artifacts:
- scripts/data_cleaning.py

### Task 4: Aggregate Zillow Data — Completed
The Zillow dataset is originally structured in a wide format with monthly values. To align it with the other datasets, we transformed it into a long format and extracted the year from each observation. We then aggregated monthly home values into yearly averages for each state.

This step ensures that all datasets operate at the same time granularity (yearly), which is necessary for accurate comparison and integration.

Artifacts:
- scripts/zillow_aggregation.py

### Task 5: Merge Datasets — In Progress
Merging of the three cleaned and processed datasets has begun. The merge is performed in Python using Pandas, joining on the shared keys state and year.
The planned merge sequence is:

- Join zillow_yearly with bls_unemployment on ['state', 'year'] using an inner join
- Join the result with census_income on ['state', 'year'] using an inner join

Initial test merges confirm that the datasets align correctly on state names after standardization. The overlapping time window across all three sources is 2019–2023, yielding up to 255 rows (51 states/D.C. × 5 years) in the final merged dataset.

Remaining work: We are currently validating the merged output to confirm:
- No states are dropped due to name mismatches
- Row counts are as expected across all years
- No duplicate rows are introduced by the join

### Task 6: Exploratory Analysis — Started
Initial exploratory analysis has begun. We have started reviewing distributions of housing prices across states and identifying general trends in the data. Preliminary inspection suggests noticeable variation in home values across states, which supports the motivation for further analysis.

More detailed analysis, including visualizations and statistical summaries, will be conducted after completing dataset integration.

### Task 7: Interpretation — Not Started
Interpretation of results will begin after exploratory analysis is completed.

### Task 8: Final Revision — Not Started
Final report preparation and revisions will be completed in later stages of the project.

## 2. Updated Timeline

| Task | Original Timeline | Status | Updated Completion |
|-----|------------------|--------|--------------------|
| Finalize question and datasets | Week 1 | Completed | Week 1 |
| Data acquisition | Week 1 | Completed | Week 1 |
| Data cleaning | Week 2 | Mostly Completed | Week 2 |
| Aggregate Zillow data | Week 2 | Completed | Week 2 |
| Merge datasets | Week 3 | In Progress | Week 3 |
| Exploratory analysis | Week 3 | Started | Week 3 |
| Interpretation | Week 4 | Not Started | Week 4 |
| Final revision | Week 4 | Not Started | Week 4 |

## 3. Changes to Project Plan

There have been no major changes to the overall research questions or project scope. However, several refinements were made as we began working with the data.

First, we confirmed that the Zillow dataset required transformation from monthly to yearly format before it could be integrated with other datasets. This step was not fully detailed in the original plan but became necessary during implementation.

Second, we identified the importance of standardizing state identifiers across datasets. Differences in formatting (such as abbreviations vs full names) required additional preprocessing to ensure consistent merging.

Finally, we updated our income dataset choice. While our original plan referenced Census data, we instead used a recent dataset (2019–2023) from HD Pulse, an NIH backed platform. This decision was made because it provided more accessible and recent data in a clean format suitable for integration.

These changes improved the practicality and feasibility of our project while maintaining alignment with our original objectives.

## 4. Challenges and Solutions

### Challenge 1: Time Granularity Differences
The Zillow dataset is monthly, while the unemployment and income datasets are yearly.

**Solution:**  
We aggregated Zillow data into yearly averages to ensure consistency across datasets.

### Challenge 2: Data Format Differences
The Zillow dataset is in wide format, while other datasets are in long format.

**Solution:**  
We reshaped the Zillow dataset into long format before aggregation and integration.

### Challenge 3: State Name Inconsistencies
Different datasets used different naming conventions for states.

**Solution:**  
We standardized all state identifiers before merging.

### Challenge 4: Access to Recent Income Data
Recent Census income data was not easily accessible in a clean and usable format.

**Solution:**  
We used HD Pulse, an NIH backed platform, to obtain recent median household income data (2019–2023), ensuring both data relevance and credibility.

## 5. Team Contributions

### Raghav
- Defined project direction and research questions  
- Identified and downloaded Zillow and BLS datasets  
- Implemented data cleaning and aggregation scripts  
- Led initial data processing steps  
- Contributed to writing the status report  

### Vedha
- Identified and downloaded income dataset (HD Pulse)  
- Assisted in validating and cleaning datasets  
- Began dataset merging and alignment  
- Contributed to writing the status report and project plan

## 6. Next Steps

The next phase of the project will focus on completing dataset integration and conducting detailed analysis.

Specifically, we will:
1. **Finalize and validate the merged dataset** — confirm row counts, check for unintended data loss
2. **Complete the data quality assessment** — produce a formal quality report documenting completeness, consistency, accuracy, and any anomalies
3. **Complete exploratory data analysis** — produce visualizations including scatter plots (home value vs. unemployment, home value vs. income), time-series plots by state, and summary statistics tables
4. **Interpret findings and draft conclusions** — connect observed patterns back to the three research questions
5. **Write final report and data documentation** — produce `README.md`, a data dictionary for the merged dataset, and all required metadata (cf. Week 15)

These steps will lead into the final stage of the project, where we will present findings and conclusions.
