# ### Part 2: Cleaning the Data

# Write a Python script (`clean_data.py`) for cleaning the data and document the steps along the way.  The script `clean_data.py` should be a runnable Python script that takes messy_population_data.csv as input and outputs cleaned_population_data.csv

# 1. For each issue you identified, propose and implement a method to clean or correct the data.
# 2. Use appropriate pandas and numpy functions for cleaning.
# 3. Document each cleaning step with comments in your code.
# 4. Include error handling and logging where appropriate.
# 5. Document your cleaning process in your `readme.md`, including:
#    - The technique used to address each issue
#    - Justification for your approach
#    - The impact of your cleaning on the dataset (e.g., number of rows affected/removed, changes in data distribution)
#    - Any assumptions you made

import pandas as pd

## load messy dataset using pandas
df = pd.read_csv('messy_population_data.csv')
print(df.shape)

## Duplicated Values
df = df.drop_duplicates(subset=['income_groups', 'age', 'gender', 'year', 'population'], keep=False)


## Inconsistencies

# renaming values within the income group to no longer have _typo
df['income_groups'] = df['income_groups'].replace({'high_income_typo':'high_income',
                                                   'lower_middle_income_typo':'lower_middle_income',
                                                   'upper_middle_income_typo':'upper_middle_income'})

# dropping all values that are 3 and replacing with 0
df['gender'] = df['gender'].replace(3.0,0.0) 


## Missing Values
floatType = df.select_dtypes(include=['float64']).columns  # Get float columns
df[floatType] = df[floatType].fillna(df[floatType].median()) # replace all na's with the median of the column 


## Outliers
Q1 = df['population'].quantile(0.25)
Q3 = df['population'].quantile(0.75)
IQR = Q3 - Q1

lowerBound = Q1 - 1.5 * IQR
upperBound = Q3 + 1.5 * IQR

# filtered for values between lower and upper bound of the IQR which was calculated above 
df['population'] = df['population'].where((df['population'] >= lowerBound) & (df['population'] <= upperBound), other=None)


## Impossible Dates 
df['year'] = df['year'].where(df['year'] <= 2024) # drop all years greater than 2024
df['year'] = df['year'].ffill()

## writing to output 
output_file = 'clean_population_data.csv'
df.to_csv(output_file, index=False)
print(f"\nClean dataset saved as '{output_file}'")