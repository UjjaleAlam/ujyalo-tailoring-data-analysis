# Pilot Data Analysis: Family Tailoring Business

## Overview
This project is a small pilot data analysis conducted as part of my self-directed learning while transitioning into Information Technology. The analysis uses one month worth of real operational data from a family-run tailoring business to practice data cleaning, descriptive analysis, and interpretation using Python.

The purpose of this project is learning-focused rather than business forecasting or optimization.

---

## Dataset Description
- Source: Manually recorded transaction data from a family tailoring shop
- Time period: One month
- Number of records: 29
- Data format: CSV (cleaned from original Excel records)

The dataset reflects real-world characteristics of small business data, including inconsistent formatting and unstructured fields.

---

## Data Cleaning Approach
The data preparation process included:
- Standardizing column names for consistency
- Identifying missing values and handling them conservatively
- Separating numeric and non-numeric fields where applicable
- Validating payment fields by recalculating totals
- Retaining minor inconsistencies to reflect manual record-keeping limitations

Cleaning and validation steps are implemented in a separate script (`data_cleaning.py`).

---

## Analysis Performed
Exploratory analysis was conducted using Pandas and Matplotlib and focused on basic descriptive insights derived from the available data.

Visualizations Generated

The analysis produced two figures:

-Transaction Distribution: New vs Returning Customers
  A bar chart showing the number of transactions from new customers compared to returning customers over the observed period.

-Product Dominance by Quantity
  A bar chart showing total quantities for each product category (coat, waistcoat, shirt, pant, other), highlighting which services were most frequently ordered.

In addition to the visualizations, total revenue and customer proportions were calculated and printed to the console.

No predictive modeling or long-term trend analysis was attempted due to the limited time span of the data.

---

## Tools Used
- Python
- Pandas
- Matplotlib
- CSV data handling

---

## Limitations
- The dataset covers only one month
- Small sample size
- Data is manually recorded
- Results are exploratory and not intended for generalization

---

## Learning Outcome

This project helped me:

-Work with imperfect, real-world data

-Separate data cleaning and analysis workflows

-Perform basic exploratory data analysis in Python

-Create simple visualizations to summarize transactional patterns

-understand how IT tools can be applied to real-world data, particularly in small business contexts.