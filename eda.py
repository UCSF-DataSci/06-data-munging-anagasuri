# 1. Load the messy dataset ("messy_population_data.csv") using Python with pandas.
# 2. Perform an exploratory data analysis (EDA) to identify data quality issues.
# 3. Document each issue you discover in your `readme.md`, including:
#    - Description of the issue
#    - Column(s) affected
#    - Example of the problematic data
#    - Potential impact on analysis if left uncleaned

# import packages 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# laod messy dataset using pandas
df = pd.read_csv('messy_population_data.csv')

# check characteristics of each column in df 
shape = df.shape
print(f"Number of rows and columns in messy dataset: {shape}") 
# (125718, 5)

df.info()
#   Column         Non-Null Count   Dtype  
# ---  ------         --------------   -----  
#  0   income_groups  119412 non-null  object 
#  1   age            119495 non-null  float64
#  2   gender         119811 non-null  float64
#  3   year           119516 non-null  float64
#  4   population     119378 non-null  float64

df.describe() 
# mean age=50.007038, gender=1.578578, year=2025.068049, population=1.112983e+08

#                  age         gender           year    population
# count  119495.000000  119811.000000  119516.000000  1.193780e+05
# mean       50.007038       1.578578    2025.068049  1.112983e+08
# std        29.154144       0.590559      43.584951  1.265205e+09
# min         0.000000       1.000000    1950.000000  2.100000e+01
# 25%        25.000000       1.000000    1987.000000  2.316023e+06
# 50%        50.000000       2.000000    2025.000000  7.145754e+06
# 75%        75.000000       2.000000    2063.000000  1.466388e+07
# max       100.000000       3.000000    2119.000000  3.293043e+10

# check for unique values in each column
for column in df.columns:
    uniqueVals = df[column].unique()
    countUniqueVals = len(uniqueVals)
    print(f"Unique values in '{column}': {countUniqueVals}")

# Unique values in 'income_groups': 9
# Unique values in 'age': 102
# Unique values in 'gender': 4
# Unique values in 'year': 170
# Unique values in 'population': 114926

# check datatypes of each column
dtypes = df.dtypes
print(f"Data type of each column: {dtypes}") 

# income_groups     object
# age              float64
# gender           float64
# year             float64
# population       float64

# check duplicated values 
for column in df.columns:
    dupVals = df[column].duplicated().sum()
    print(f"Duplicate values in '{column}': {dupVals}")

# Duplicate values in 'income_groups': 125709
# Duplicate values in 'age': 125616
# Duplicate values in 'gender': 125714
# Duplicate values in 'year': 125548
# Duplicate values in 'population': 10792


# check number of missing values in each column 
for column in df.columns:
    nullVals = df[column].isnull().sum()
    print(f"Missing values in '{column}': {nullVals}")

# Missing values in 'income_groups': 6306
# Missing values in 'age': 6223
# Missing values in 'gender': 5907
# Missing values in 'year': 6202
# Missing values in 'population': 6340

# plot boxplot of population to view outliers 
x = sns.boxplot(df['population'])
plt.savefig("boxplot.png")

# Print number of outliers in population column 
Q1 = df['population'].quantile(0.25)
Q3 = df['population'].quantile(0.75)
IQR = Q3 - Q1
print(f"Number of outliers: {IQR}")
# Number of outliers: 12347861.5 

# Check inconsistencies in Income Group Column
IG_unique_values = df['income_groups'].unique()
print(f'Unique values of income groups: {IG_unique_values}') # shows us there are values with an inconsistent suffix _typo 

# Unique values of income groups: 
# ['high_income' 
# nan 
# 'high_income_typo' 
# 'low_income' 
# 'low_income_typo'
# 'lower_middle_income' 
# 'lower_middle_income_typo'
# 'upper_middle_income_typo' 
# 'upper_middle_income']

typo_count = df['income_groups'].str.endswith('_typo').sum() # sums all values with _typo suffix
print(f"Number of values with inconsistent suffix: {typo_count}") # there are 5959 values with the _typo suffix that should be removed
# Number of values with inconsistent suffix: 5959

# Check inconsistencies in Gender Column
Gender_unique_values = df['gender'].unique()
print(f'Unique value of gender: {Gender_unique_values}') # shows us there is a value of 3 when there should only be 1 and 2
# Unique value of gender: [ 1.  3. nan  2.]

count3s = df['gender'].value_counts()[3]
print(f'Number of 3s: {count3s}') 
# Number of 3s: 6286

# Check for future dates
over2024 = (df['year'] > 2024).sum() # gives number of values that are over 2024, showing years that are impossible 
print(f'Years past 2024: {over2024}') 
# Years past 2024: 60211


