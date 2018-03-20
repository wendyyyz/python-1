## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
all_ages.head(5)
recent_grads.head(5)

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()
def calculate_major_cat_totals(df):
    cats = df['Major_category'].unique()
    counts_dictionary = dict()

    for c in cats:
        major_df = df[df["Major_category"] == c]
        total = major_df["Total"].sum()
        counts_dictionary[c] = total
    return counts_dictionary

aa_cat_counts = calculate_major_cat_totals(all_ages)
rg_cat_counts = calculate_major_cat_totals(recent_grads)

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0
# job_category = recent_grad["Low_wage_jobs"].unique()
low_wage_jobs = recent_grads["Low_wage_jobs"].sum()

low_wage_proportion = low_wage_jobs / recent_grads["Total"].sum()

'''
for job in job_category:
    job_data = recent_grad[recent_grad["Low_wage_jobs"] == job]
    job_total = job_data["Total"].sum()
'''
    

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for major in majors:
    aa_major = all_ages[all_ages['Major'] == major]
    rg_major = recent_grads[recent_grads['Major'] == major]
    
    aa_unemp_sum = aa_major["Unemployment_rate"].sum()
    rg_unemp_sum = rg_major["Unemployment_rate"].sum()
    
    if aa_unemp_sum > rg_unemp_sum:
        rg_lower_count += 1