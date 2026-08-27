#Customer Personality Analysis – Data Cleaning Project
Internship Task 1 

Objective
Clean and prepare the raw Customer Personality Analysis dataset (marketing campaign data) to make it accurate, consistent, and ready for further analysis — using Python.

Tools Used
Python 
VS Code
GitHub for version control and submission

What I Did
1.Loaded the raw dataset — customer demographic and campaign response data (income, education, marital status, birth year, purchase behavior, etc.)
2.Handled missing values — identified and treated null entries (e.g., missing income values)
3.Fixed data types — converted date fields (dt_customer) into proper datetime format for accurate analysis
4.Created new features — derived useful columns like age from year_birth to support further analysis
5.Standardized categorical values — cleaned inconsistent entries in education and marital_status columns
6.Removed outliers/duplicates — checked for and removed any anomalies affecting analysis accuracy
7.Exported the cleaned dataset — saved the final clean file as marketing_campaign_cleaned.csv

Repository Structure
File
Description
data_cleaning.py
Python script containing all cleaning steps
marketing_campaign_cleaned.csv
Final cleaned dataset (2236 rows)
marketing_campaign-selected-columns.csv
Intermediate/selected column file
README.md
Project overview and documentation

 Outcome
 A clean, structured dataset (2236 records) free of missing values and inconsistencies — ready for exploratory data analysis, segmentation, or machine learning tasks.
A clean, structured dataset (2236 records) free of missing values and inconsistencies — ready for exploratory data analysis, segmentation, or machine learning tasks
