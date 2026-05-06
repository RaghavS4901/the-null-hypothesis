Economic Conditions and Housing Prices Across U.S. States

Contributors

* Raghav Singh Bhadoriya
* Vedha Pant

Summary

This project analyzes the relationship between economic conditions and housing prices across U.S. states. The primary objective was to investigate whether unemployment rates and median household income levels are associated with housing prices in different states. Housing affordability and economic inequality continue to be major economic and social issues in the United States, making it valuable to study how labor market and income conditions relate to housing markets.

To answer our research questions, we integrated three datasets from reliable publicly accessible sources. The first dataset was the Zillow Home Value Index (ZHVI), which provides estimated housing values across U.S. states over time. The second dataset came from the U.S. Bureau of Labor Statistics (BLS) Local Area Unemployment Statistics (LAUS) program, which provides unemployment rates and labor force statistics for states. The third dataset was a median household income dataset sourced from HD Pulse, an NIH backed platform using Census ACS estimates.

The project addressed the following research questions:

1. How are housing prices related to unemployment rates across U.S. states?
2. How are housing prices related to median household income across U.S. states?
3. Do states with stronger economic conditions tend to have higher housing values?

The project involved multiple stages of data curation and integration. First, all datasets were downloaded, inspected, and assessed for structural and formatting inconsistencies. The Zillow dataset required the largest transformation because it was originally provided in a wide monthly format. We reshaped it into long format, extracted yearly information, and aggregated monthly observations into yearly averages. The BLS and income datasets also required preprocessing, including removal of metadata rows, renaming of columns, standardization of state names, and conversion of numeric values.

After cleaning, the datasets were integrated using shared keys: state and year. Although the Zillow and BLS datasets covered many years, the final integrated analysis focused on 2023 because the selected income dataset provided the most complete and reliable overlap for that year.

Exploratory analysis and visualization were then performed on the merged dataset. The strongest observed relationship was between median household income and housing values. States with higher income levels generally had substantially higher home values. The computed correlation coefficient between median income and home value was approximately 0.78, indicating a strong positive relationship. In contrast, unemployment rates showed a relatively weak relationship with housing prices.

The project demonstrates how datasets from multiple institutions can be cleaned, transformed, integrated, and analyzed to support broader economic questions. In addition to answering the research questions, the project emphasizes reproducibility, workflow transparency, metadata documentation, and practical data curation techniques.

Data Profile

Dataset 1: Zillow Home Value Index (ZHVI)

Source

Zillow Research Data

Repository Location

data/zillow_home_values.csv

Description

This dataset contains Zillow Home Value Index (ZHVI) estimates across U.S. states. The ZHVI represents the typical home value in a geographic region and is updated monthly. Zillow distributes the dataset in a wide CSV format where each monthly observation appears as a separate column.

Structure

The dataset includes:

* State names
* Region metadata
* Monthly home value observations
* Multiple years of monthly data

Role in Project

This dataset served as the primary dependent variable representing housing prices.

Processing

The dataset required extensive transformation:

* Wide to long reshaping
* Date parsing
* Year extraction
* Monthly to yearly aggregation

The processed dataset was saved as:
data/zillow_home_values_yearly.csv

Ethical and Legal Considerations

The dataset is publicly available through Zillow Research. It contains only aggregated state level statistics and no personally identifiable information (PII).

Dataset 2: BLS Local Area Unemployment Statistics (LAUS)

Source

U.S. Bureau of Labor Statistics

Repository Location

data/bls_unemployment.csv

Description

This dataset contains unemployment statistics from the Local Area Unemployment Statistics (LAUS) program. It includes annual unemployment rates and labor force statistics for U.S. states.

Structure

The dataset includes:

* State names
* Year
* Labor force values
* Employment values
* Unemployment values
* Unemployment rates

Role in Project

This dataset served as the primary labor market indicator used to measure economic conditions.

Processing

The dataset required:

* Removal of metadata rows
* Column renaming
* Filtering relevant variables
* Numeric conversion
* Year filtering

The processed dataset was saved as:
data/bls_clean.csv

Ethical and Legal Considerations

The dataset is publicly available through the U.S. Bureau of Labor Statistics and contains only aggregated public statistics.

Dataset 3: Median Household Income Dataset

Source

HD Pulse (NIH backed platform using Census ACS estimates)

Repository Location

data/census_income.csv

Description

This dataset contains median household income estimates across U.S. states. The dataset was selected because it provided recent and clean state level income information suitable for integration with the Zillow and BLS datasets.

Structure

The dataset includes:

* State names
* FIPS codes
* Median household income values
* Ranking information

Role in Project

This dataset served as the primary income based economic indicator.

Processing

The dataset required:

* Metadata removal
* Column renaming
* Removal of national aggregate rows
* Conversion of comma separated numeric values
* State name standardization

The processed dataset was saved as:
data/income_clean.csv

Ethical and Legal Considerations

The dataset contains only aggregated public statistics and does not contain personally identifiable information.

Data Quality

Several data quality issues were identified throughout the project.

The Zillow dataset presented the largest structural challenge because it was distributed in a wide monthly format. Monthly observations existed as individual columns, making direct integration impossible without transformation. The dataset also contained numerous metadata columns that were not relevant to the analysis.

The BLS dataset contained metadata rows and non standard formatting that initially caused parsing issues during loading. Some column names were unlabeled or inconsistently formatted.

The income dataset also contained metadata rows and comma separated numeric values stored as text strings. Additionally, the dataset included national aggregate rows that were not appropriate for state level analysis.

The following data quality dimensions were assessed:

* Completeness
* Consistency
* Structural consistency
* Validity
* Accuracy

Missing values were limited after preprocessing and did not significantly impact the analysis. State naming conventions were standardized across datasets to improve consistency during integration. Numeric fields were validated and converted into appropriate formats.

Temporal consistency was another important issue. The Zillow dataset used monthly observations while the BLS and income datasets used yearly observations. To address this mismatch, Zillow monthly observations were aggregated into yearly averages.

The final integrated dataset contained 51 observations corresponding to the 50 U.S. states plus the District of Columbia for the overlapping year 2023.

Overall, after cleaning and transformation, the datasets were considered sufficiently high quality for exploratory economic analysis.

Data Cleaning

Multiple cleaning operations were performed throughout the project.

Zillow Dataset Cleaning

The Zillow dataset required the largest transformation effort.

The following operations were performed:

* Renamed RegionName to state
* Selected only relevant date columns
* Converted monthly date strings into datetime values
* Reshaped wide format data into long format using Pandas melt operations
* Extracted year values from dates
* Aggregated monthly observations into yearly averages
* Removed unnecessary metadata columns

The processed output was saved as:
data/zillow_home_values_yearly.csv

BLS Dataset Cleaning

The BLS dataset required preprocessing because the original CSV contained metadata rows and formatting inconsistencies.

The following operations were performed:

* Skipped metadata rows during loading
* Renamed unnamed columns
* Selected relevant variables
* Removed missing values
* Converted years into numeric values
* Filtered overlapping analysis years
* Standardized state names

The processed output was saved as:
data/bls_clean.csv

Income Dataset Cleaning

The income dataset also required preprocessing and standardization.

The following operations were performed:

* Removed metadata rows
* Renamed columns
* Removed national aggregate rows
* Converted comma separated numeric values into numeric types
* Added year information
* Standardized state names

The processed output was saved as:
data/income_clean.csv

Data Integration

After cleaning, the datasets were merged using shared keys:

* state
* year

The integration process was implemented using Pandas merge operations.

The final integrated dataset was saved as:
data/final_merged.csv

Findings

The exploratory analysis produced several notable findings.

The strongest relationship observed was between median household income and housing values. The scatterplot comparing these variables showed a clear positive relationship. States with higher median household income generally had substantially higher home values.

The computed correlation coefficient between median income and home value was approximately:

0.78

This indicates a strong positive relationship between income levels and housing prices.

In contrast, unemployment rates showed a weaker relationship with home values. The correlation coefficient between unemployment rates and housing prices was approximately:

0.20

This suggests that unemployment rates alone may not strongly explain variation in housing prices at the state level in this dataset.

The top states by housing value included:

* Hawaii
* California
* Massachusetts
* Washington
* Colorado

These states also tend to have relatively high income levels, further supporting the positive relationship between income and home values.

The following visualizations were generated:

* visualizations/income_vs_housing.png
* visualizations/unemployment_vs_housing.png
* visualizations/housing_trend.png

The analysis suggests that household income is more strongly associated with housing prices than unemployment rates within the integrated dataset.

Future Work

Several improvements and extensions could strengthen this project in the future.

First, the project could incorporate additional years of income data. While the Zillow and BLS datasets contained many years of observations, the selected income dataset limited the final integrated analysis primarily to 2023. Expanding temporal coverage would support stronger longitudinal analysis and trend modeling.

Second, additional economic variables could be integrated into the project, including:

* Inflation rates
* Mortgage interest rates
* Population growth
* GDP per capita
* Rental prices
* Cost of living indexes

Third, more advanced statistical methods could be applied. The current project primarily focused on exploratory analysis and correlations. Future versions could incorporate:

* Linear regression
* Multiple regression
* Time series forecasting
* Clustering
* Geographic analysis

Fourth, the project could be extended beyond state level analysis into county level or metropolitan area analysis, allowing more granular comparisons.

Fifth, workflow automation could be expanded through additional automated acquisition scripts and more advanced Snakemake pipelines.

The project also highlighted the importance of metadata, reproducibility, and FAIR principles. Future work could incorporate more advanced metadata standards and persistent identifiers.

Challenges

Several technical and organizational challenges were encountered throughout the project.

The largest challenge involved integrating datasets from multiple institutions with very different formats and structures. The Zillow dataset used monthly wide format data while the BLS and income datasets used yearly long format data. This required significant preprocessing before integration.

Another challenge involved inconsistent naming conventions across datasets. State names required standardization to avoid merge mismatches.

The BLS and income datasets also contained metadata rows and formatting inconsistencies that initially caused parsing errors during loading. Several debugging iterations were required before the datasets could be processed correctly.

Dataset availability presented another challenge. Finding recent state level income data in a clean and easily accessible format proved difficult. The HD Pulse dataset was ultimately selected because it provided recent and structured data suitable for integration.

Workflow reproducibility was another important consideration. To improve reproducibility and transparency, the project includes:

* cleaning scripts
* integration scripts
* visualization scripts
* a run all workflow script
* a Snakemake workflow
* metadata files
* a data dictionary
* dependency specifications

Time management was also challenging because the project required data cleaning, transformation, integration, analysis, visualization, and documentation within a limited time frame.

Despite these challenges, the project successfully integrated multiple datasets and produced meaningful exploratory findings.

Reproducing

Requirements

Install required packages:

pip install -r requirements.txt

Running the Workflow

Option 1: Run Entire Workflow

python scripts/run_all.py

Option 2: Run Snakemake Workflow

snakemake --cores 1

Workflow Steps

The workflow performs:

1. Cleaning of BLS dataset
2. Cleaning of income dataset
3. Zillow yearly aggregation
4. Dataset integration
5. Exploratory analysis and visualization generation

Outputs

Generated outputs include:

* cleaned datasets
* integrated dataset
* visualizations
* correlation analysis

Visualizations are saved in:
visualizations/

Final integrated dataset:
data/final_merged.csv

Repository Structure

data/
scripts/
visualizations/
metadata/
ProjectPlan.md
StatusReport.md
README.md
requirements.txt
Snakefile

References

1. Zillow Research Data: https://www.zillow.com/research/data/
2. U.S. Bureau of Labor Statistics (LAUS): https://www.bls.gov/lau/
3. HD Pulse: https://hdpulse.nimhd.nih.gov/
4. Pandas Documentation: https://pandas.pydata.org/
5. Matplotlib Documentation: https://matplotlib.org/
6. Snakemake Documentation: https://snakemake.readthedocs.io/
