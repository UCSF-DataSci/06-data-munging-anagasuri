import pandas as pd
cleanData = pd.read_csv('clean_population_data.csv')

shape = cleanData.shape
print(f"Number of rows and columns in messy dataset: {shape}") 

cleanData.info()
#      Column         Non-Null Count   Dtype  
# ---  ------         --------------   -----  
#  0   income_groups  119874 non-null  object 
#  1   age            119874 non-null  float64
#  2   gender         119874 non-null  float64
#  3   year           119874 non-null  float64
#  4   population     116388 non-null  float64

cleanData.describe() 
#                  age         gender           year    population
# count  119874.000000  119874.000000  119874.000000  1.163880e+05
# mean       49.986903       1.398001    2005.433981  8.881248e+06
# std        28.440609       0.586693      23.997657  7.983333e+06
# min         0.000000       0.000000    1950.000000  2.200000e+01
# 25%        26.000000       1.000000    1987.000000  2.440496e+06
# 50%        50.000000       1.000000    2023.000000  7.151872e+06
# 75%        74.000000       2.000000    2024.000000  1.294492e+07
# max       100.000000       2.000000    2024.000000  3.109804e+07

for column in cleanData.columns:
    uniqueVals = cleanData[column].unique()
    countUniqueVals = len(uniqueVals)
    print(f"Unique values in '{column}': {countUniqueVals}")
# Unique values in 'income_groups': 6
# Unique values in 'age': 101
# Unique values in 'gender': 3
# Unique values in 'year': 75
# Unique values in 'population': 108794