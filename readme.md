Economic Conditions and Housing Prices Across U.S. States

Contributors

* Raghav Singh Bhadoriya
* Vedha Pant

Summary

This project examines how state-level economic conditions relate to housing prices in the United States. Housing affordability is one of the most visible social and policy concerns in recent years, while labor market and income inequality patterns continue to vary significantly across regions. Motivated by these issues, we asked whether differences in unemployment and income are associated with differences in housing values across states. The project combines data curation, integration, quality assessment, and exploratory analysis to produce reproducible evidence addressing these questions.

We integrated three publicly available datasets. First, we used Zillow Home Value Index (ZHVI) state-level data as a proxy for housing price conditions. Second, we used U.S. Bureau of Labor Statistics (BLS) Local Area Unemployment Statistics (LAUS) data for unemployment rates. Third, we used median household income data provided through HD Pulse (NIH-backed, based on Census ACS estimates). These sources are complementary: Zillow contributes the housing outcome variable, while BLS and HD Pulse provide key economic indicators that may explain variation in housing values.

The project addressed three research questions:

1. How are housing prices related to unemployment rates across U.S. states?
2. How are housing prices related to median household income across U.S. states?
3. Do states with stronger economic conditions tend to have higher housing values?

To answer these questions, we implemented a full data pipeline. We began with source profiling to inspect schema, missingness, formatting issues, and temporal coverage. The Zillow dataset required major structural transformation because it is distributed in wide monthly format with many date columns. We reshaped it to long form, parsed dates, extracted year, and aggregated to yearly averages. BLS and HD Pulse income files required removal of metadata rows, renaming columns, filtering to relevant units, handling text-formatted numerics, and standardizing state names.

After cleaning, we merged all datasets using common keys (`state`, `year`). Although Zillow and BLS support a longer time window, the integrated analysis centered on 2023 because the selected income source provided the most complete overlap for that year. We generated descriptive outputs, scatterplots, and correlation measures to evaluate relationships among home value, unemployment rate, and median household income. The strongest relationship was between median income and home value, while unemployment showed a weaker association.

This project contributes in two ways. Substantively, it shows that income differences are strongly aligned with state-level housing value differences in the final integrated dataset. Methodologically, it demonstrates practical data curation decisions required to make heterogeneous public datasets analysis-ready. We include raw and cleaned data files, transformation scripts, a reproducible run-all script, a Snakemake workflow, checksums, metadata, and documentation so another researcher can reproduce the same outputs and inspect each curation step. The resulting repository is designed to emphasize transparency, traceability, and clear links between data quality issues, cleaning operations, and analysis results.

An additional motivation for this work is pedagogical: to demonstrate that data curation is not separate from analysis quality, but a prerequisite for trustworthy interpretation. By documenting each transformation and quality decision, the project creates an auditable path from raw source files to conclusions. This design choice supports both grading requirements and broader reproducibility practice in interdisciplinary data science settings.

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

The dataset is publicly available through Zillow Research. It contains only aggregated state level statistics and no personally identifiable information (PII). Data were used for academic, non-commercial analysis and attributed to Zillow in the References section. Redistribution and downstream use should follow Zillow's published research data terms.

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

The dataset is publicly available through the U.S. Bureau of Labor Statistics and contains only aggregated public statistics. BLS data are U.S. government statistical outputs and were used with attribution. Users reusing this repository should preserve source attribution and consult BLS usage guidance where applicable.

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

The dataset contains only aggregated public statistics and does not contain personally identifiable information. The HD Pulse source (based on Census ACS estimates) was used for educational analysis with citation. Reuse should follow HD Pulse access terms and ACS source usage requirements as stated by the provider.

Data Quality

We performed a structured quality assessment before and after cleaning to evaluate whether the integrated dataset was fit for exploratory economic analysis. Assessment focused on five dimensions: completeness, consistency, structural integrity, validity, and temporal alignment. Because the project combines sources from different institutions with different publication formats, the quality review was essential to avoid silent merge errors and misleading conclusions.

The Zillow dataset presented the most significant structural quality challenge. It is provided in a wide monthly format where each month is a separate column, and includes metadata columns not needed for this project. In its raw form, this structure is difficult to merge with annual datasets. Our assessment identified this as a structural incompatibility rather than a data value problem. We also checked date column patterns and confirmed that relevant monthly values were present for the selected analysis years.

The BLS unemployment file introduced parsing and consistency issues. It included metadata/header rows before tabular data, and column labels that required renaming before automated processing. We assessed whether state names and year values were consistently represented and whether unemployment rates could be interpreted as numeric values without loss. Initial ingestion produced mixed types in the year field, which required explicit numeric coercion and filtering to valid year ranges.

The HD Pulse income dataset had similar ingestion quality issues: metadata rows, comma-formatted numbers stored as strings, and inclusion of national aggregate records not compatible with state-level joins. We assessed entity-level consistency by verifying that state names could be standardized and that non-state records were removable without affecting the target population for this project.

Completeness checks were performed after cleaning and before merge. We verified that key fields (`state`, `year`, and numeric indicators) were non-null for records entering the final integration step. Missingness was low after preprocessing and did not materially reduce coverage for the selected overlap year. Consistency checks included whitespace trimming and state name normalization to prevent join key mismatches. Structural checks confirmed one record per state-year in each cleaned dataset for the intended granularity.

Validity checks focused on data types and plausible value ranges. We converted unemployment rate and income values to numeric types and confirmed no non-numeric artifacts remained after conversion. We also manually inspected sample rows from cleaned outputs to verify that transformations preserved semantic meaning (for example, yearly home value means remained in expected magnitude relative to state-level housing markets).

Temporal quality was a major integration concern. Zillow is monthly, while BLS and income are yearly. Without temporal harmonization, any merge would be invalid or would implicitly duplicate records. To address this, Zillow monthly values were aggregated to yearly averages. We then constrained the integrated analysis to a common year (`2023`) where all three sources overlapped with reliable coverage. This improved comparability and reduced the risk of biased inferences caused by uneven time support.

Post-cleaning quality checks showed that the final merged file contains 51 observations (50 states plus District of Columbia) with required variables present and standardized. While this does not eliminate all limitations (for example, single-year scope and ecological interpretation constraints), the curated dataset meets the quality threshold for reproducible exploratory analysis aligned with the project goals.

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

The merged 2023 state-level dataset produced a clear and interpretable set of exploratory findings. The most important result is a strong positive association between median household income and home values. In the `income_vs_housing` scatterplot, points cluster along an upward trend, indicating that states with higher median income generally also report higher Zillow home values. This relationship is supported by the computed Pearson correlation of approximately `0.78`, which is large for a cross-sectional social/economic comparison at state level.

By contrast, unemployment rate has a much weaker relationship with home values in this dataset. The `unemployment_vs_housing` plot shows broad dispersion with only a slight trend, and the corresponding correlation is about `0.20`. This suggests that, for the selected year and aggregation level, unemployment by itself is not a strong linear predictor of variation in state-level home values. In practical terms, labor market stress may still matter, but it likely interacts with other factors such as long-term income base, housing supply constraints, migration, and local policy conditions.

Ranking analysis of the highest-value states also aligns with this pattern. States such as Hawaii, California, Massachusetts, Washington, and Colorado appear among the top home-value observations and tend to have relatively high median income levels in the same year. While this ranking does not establish causality, it is consistent with the broader association shown in the correlation and scatterplot outputs.

Three outputs were generated to support interpretation:

* `visualizations/income_vs_housing.png` (income and home value relationship)
* `visualizations/unemployment_vs_housing.png` (unemployment and home value relationship)
* `visualizations/housing_trend.png` (top states by home value)

These visuals are intended to make the relationships auditable and reproducible rather than relying only on narrative claims. Together with the integrated table (`data/final_merged.csv`), they provide a traceable evidence chain from cleaned data to reported findings.

The findings should be interpreted within scope limits. First, the final integrated analysis is cross-sectional (primarily 2023) and therefore cannot identify temporal dynamics or causal pathways. Second, state-level aggregation can mask substantial within-state variation (for example, urban-rural differences). Third, correlation captures linear association, not mechanism. Even with these limits, the results are useful for hypothesis generation and for demonstrating the value of a transparent curation pipeline.

In summary, the project provides evidence that income differences are strongly aligned with state-level housing value differences, while unemployment has a weaker standalone relationship in the final dataset. This supports the working hypothesis that longer-run economic capacity (as proxied by median income) is more tightly connected to housing valuation patterns than short-run labor market variation when examined at annual state resolution.

A final practical finding concerns curation itself: transparent preprocessing materially improved interpretability. Early exploratory plots generated before strict cleaning were noisier and less reliable due to formatting inconsistencies and key mismatches. After normalization and integration checks, the analytic outputs became more stable and easier to explain. This reinforces that careful data preparation is not only a technical requirement but an empirical requirement for defensible findings.

Overall, the reported numeric results and visual patterns are internally consistent and aligned with the project's research questions, providing a coherent exploratory answer based on the integrated evidence.

Future Work

Several extensions would make this project analytically stronger and more useful as a long-term curation asset. The most important next step is to expand temporal coverage for the income source so that all three indicators can be analyzed across multiple years. Zillow and BLS already support broader year ranges, and adding consistent multi-year income observations would enable trend analysis, lag testing, and robustness checks that are not possible with a primarily single-year integration.

A second priority is variable expansion. Housing values are influenced by many structural factors not included in the current version. Future integration could add mortgage rates, inflation, housing supply indicators (building permits, vacancy rates, housing starts), rent levels, cost-of-living indices, population growth, and migration. These additions would support richer explanatory models and help reduce omitted-variable bias in downstream analysis.

Methodologically, the current work is intentionally exploratory. A future version should progress from descriptive correlations to formal modeling. Candidate approaches include multivariate linear regression, regularized regression, mixed-effects models, and panel methods if multi-year alignment is achieved. For predictive tasks, cross-validated machine learning baselines could be added, but interpretability should remain central so findings can be communicated clearly to non-technical stakeholders.

Granularity is another major improvement area. State-level analysis is useful for a first pass, but it can hide substantial intra-state heterogeneity. Moving to county or metro-level units would allow more precise comparisons and may reveal relationships that are diluted at state aggregation. This would also support geospatial visualizations and regional clustering analyses, including comparisons by Census region or urbanization level.

From a curation perspective, automation can be strengthened. Future workflow versions should include programmatic data acquisition for all sources, explicit checksum verification as a required pipeline stage, automated schema validation, and machine-readable data contracts for cleaned outputs. These additions would reduce manual intervention and improve reproducibility for graders and external users.

Metadata and FAIR compliance can also be improved. We currently provide baseline project metadata and a data dictionary, but future releases could adopt fuller Schema.org or DataCite records, include explicit versioned provenance for each derived file, and publish an archival release with a persistent identifier (for example, Zenodo sandbox). This would improve discoverability and long-term usability.

Finally, there are practical lessons that inform future team workflows. Early source vetting should include licensing checks, coverage diagnostics, and schema compatibility scoring to reduce late-stage dataset substitution. Team roles for profiling, cleaning, modeling, and documentation should be assigned earlier with milestone checklists tied to rubric categories (reproducibility, transparency, compliance, FAIR). Building these practices into project management would reduce last-minute risk and improve consistency across deliverables.

Future dissemination could also be improved through communication-oriented artifacts. Examples include an executive summary for non-technical audiences, a compact methodology diagram of the pipeline, and a dashboard-style notebook that links each figure to its generating script and inputs. These additions would make the project easier to evaluate, reuse, and extend by instructors, peers, and external collaborators while keeping the reproducible core unchanged.

As a final extension, releasing periodic versioned snapshots (data, code, metadata, and results together) would support longitudinal maintenance and clearer comparison of methodological improvements over time.

Challenges

The project involved both technical and coordination challenges that directly affected data curation decisions. The most significant technical challenge was format heterogeneity across sources. Zillow data were delivered in wide monthly format, while BLS and income sources were effectively annual tables. This mismatch meant integration was not possible until we designed and validated a temporal harmonization strategy. The transformation from monthly to yearly values introduced additional checks to ensure aggregation logic was correct and reproducible.

A second challenge was schema inconsistency and non-data rows in source files. BLS and income files contained metadata/header rows and columns requiring renaming before robust parsing. Early script versions failed on type conversion and column selection because initial assumptions about layout were too strict. We addressed this with explicit skip-row settings, selective column extraction, and defensive conversion steps (`errors="coerce"` and post-conversion filtering), but this required multiple debugging iterations.

Entity normalization was another recurring challenge. State names looked similar across datasets but were not always formatted identically (extra spaces, ordering differences, and inclusion of national rows). Even small inconsistencies can silently break merges. We implemented state name trimming and explicit filtering of non-state aggregates, then validated merge counts to ensure expected coverage. This work was not conceptually difficult, but it was operationally critical because key-based integration is highly sensitive to naming mismatches.

Dataset selection for income presented a project management challenge. We changed income source during development to improve recency and usability, which was a reasonable curation decision but required updates across documentation, references, and processing scripts. Ensuring consistency between code, report narrative, and provenance documentation took additional effort, especially near deadline. This highlighted the need for tighter change tracking whenever source substitutions occur.

Reproducibility introduced its own challenges. Running the full pipeline reliably required making script dependencies explicit, ensuring output paths were stable, and avoiding hidden notebook/manual steps. We addressed this by providing both a run-all script and a Snakemake workflow, but validating that both produce expected artifacts still required iterative testing. Environment differences (for example, plotting cache warnings in restricted environments) also reminded us that reproducibility depends on runtime context, not only code correctness.

Time and coordination pressure were also substantial. The project combined acquisition, profiling, cleaning, integration, analysis, visualization, metadata creation, and report writing. Balancing these tasks while maintaining quality across all rubric dimensions was difficult. Documentation often lagged implementation, and catching up required dedicated effort late in the cycle.

Despite these challenges, the team developed a functioning end-to-end pipeline and documented key curation decisions. The main lesson is that data curation projects benefit from early standardization checks, strict provenance tracking, and continuous documentation updates rather than end-of-project consolidation.

Another challenge was balancing rubric completeness with technical focus. Because the assignment evaluates reproducibility, transparency, licensing, metadata, and narrative quality simultaneously, it was necessary to allocate time across many deliverables rather than only coding tasks. This occasionally slowed analysis progress but improved overall project robustness. The experience emphasized that successful curation projects require both engineering discipline and documentation discipline from the start.

Compliance and Licensing

Software in this repository is released under the MIT License (`LICENSE`). Data files originate from external providers and may be subject to source-specific terms. Zillow Research data were used with attribution for academic analysis and should be reused according to Zillow's published research-data terms. BLS LAUS data are public U.S. government statistics; attribution is retained and users should follow BLS usage/citation guidance. HD Pulse (NIH-backed, using ACS estimates) was used with citation for educational analysis; reuse should follow HD Pulse and underlying ACS source terms. This repository does not include personally identifiable information and uses aggregated state-level indicators only.

Reproducing

Requirements

Install required packages:

pip install -r requirements.txt

Running the Workflow

Option 1: Run Entire Workflow

python scripts/run_all.py

Option 2: Run Snakemake Workflow

snakemake --cores 1

Verify file integrity (SHA-256 checksums):

python scripts/verify_checksums.py

Workflow Steps

The workflow performs:

1. Cleaning of BLS dataset
2. Cleaning of income dataset
3. Zillow yearly aggregation
4. Dataset integration
5. Exploratory analysis and visualization generation
6. Optional checksum verification against `checksums.txt`

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
