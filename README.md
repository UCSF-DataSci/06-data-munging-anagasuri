# Data Cleaning Project: Population Dataset

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: [125718]
- **Columns**: [5]

### Column Details
| Column Name      | Data Type   | Non-Null Count | Unique Values |  Mean         |
|------------------|-------------|----------------|---------------|---------------|
| [income_groups]  | [Object]    | [119412]       | [9]           | [0]           |
| [age]            | [float64]   | [119495]       | [102]         | [50.007038]   |
| [gender]         | [float64]   | [119811]       | [4]           | [1.578578]    |
| [year]           | [float64]   | [119516]       | [170]         | [2025.068049] |
| [population]     | [float64]   | [119378]       | [114926]      | [1.112983e+08]|


### Identified Issues

1. **[Inappropriate Datatypes]**
   - Description: [When the messy dataset is generated, its data types are
                  
                  income_group -> object
                  age -> float
                  gender -> float
                  year -> object
                  population -> object
                  
                  year should be converted to int and population should be converted to int.
                  However, when I read the messy dataset into a pandas dataframe, pandas assumed
                  the datatypes of each column and converted year and population's data types to
                  float itself. Therefore, I do not have to perform any coercions.]
   - Affected Column(s): [year and population]
   - Example: [When running 
              
              print("\nMessy dataset info:")
              print(df_messy.info())
              
              from the dirty-data.py script, you get the following output: 
              
              #   Column         Non-Null Count   Dtype  
              ---  ------         --------------   -----  
              0   income_groups  119412 non-null  object 
              1   age            119495 non-null  float64
              2   gender         119811 non-null  float64
              3   year           125718 non-null  object 
              4   population     125718 non-null  object
              
              This shows that year and population are of type object.] 

   - Potential Impact: [If pandas had not automatically converted the data types of year and populatin from object to float, it would not be possible to find their statistical summaries. We cannot find stats such as mean or standard deviation if we are using a column that is of type object and not int/float.]

2. **[Duplicate Values]**
   - Description: [All columns have numerous duplicated values.]
   - Affected Column(s): [income_groups, age, gender, year, population]
   - Example: [When looking for the count of duplicates for each column, you get the following output
                  
                  for column in df.columns:
                     dupVals = df[column].duplicated().sum()
                     print(f"Duplicate values in '{column}': {dupVals}")

                  # Duplicate values in 'income_groups': 125709
                  # Duplicate values in 'age': 125616
                  # Duplicate values in 'gender': 125714
                  # Duplicate values in 'year': 125548
                  # Duplicate values in 'population': 10792]
   - Potential Impact: [duplicate values can skew statistical measurement such as mean or standard deviation, in turn, misrepresenting the dataset.]

3. **[Missing Values]**
   - Description: [All columns have multiple missing values, denoted by Nan or the value is actually missing.]
   - Affected Column(s): [income_groups, age, gender, year, population]
   - Example: [When looking for the count of missing values for each column, you get the following output
               
               for column in df.columns:
                  nullVals = df[column].isnull().sum()
                  print(f"Missing values in '{column}': {nullVals}")

               # Missing values in 'income_groups': 6306
               # Missing values in 'age': 6223
               # Missing values in 'gender': 5907
               # Missing values in 'year': 6202
               # Missing values in 'population': 6340]

   - Potential Impact: [Missing values can reduce the amount of valid data to use for analysis which can 
reduce the impact of the results from analysis. It could also cause us to draw innacurate statistical measurements becuase of data distortion.]

4. **[Outliers]**
   - Description: [The population column has many outliers. ]
   - Affected Column(s): [Population]
   - Example: [When looking for the number of outliers in the population column after calculating the IQR
   
               # plot boxplot of population to view outliers 
               x = sns.boxplot(df['population'])
               plt.savefig("boxplot.png")

               # Print number of outliers in population column 
               Q1 = df['population'].quantile(0.25)
               Q3 = df['population'].quantile(0.75)
               IQR = Q3 - Q1
               print(f"Number of outliers: {IQR}") 

               # Number of outliers: 12347861.5 
               
               We can see that there is a very large number of outliers for the population column.]
   - Potential Impact: [If the outliers are left in the dataset, it will skew the results of the analysis.   
If outliers are left in, extreme datapoints can create misleading representation of the data.]

5. **[Inconsistencies]**
   - Description: [There are many naming inconsistences for the income_groups column and a 3rd option in the  
                  gender column when its only valid options for male and female are 1 and 2.]
   - Affected Column(s): [income_groups, gender]
   - Example: [When looking at the unique values of the income_groups and gender columns
               
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
               print(f"Number of values with inconsistent suffix: {typo_count}") 
               # there are 5959 values with the _typo suffix that should be removed
               # Number of values with inconsistent suffix: 5959
               
               # Check inconsistencies in Gender Column
               Gender_unique_values = df['gender'].unique()
               print(f'Unique value of gender: {Gender_unique_values}') # shows us there is a value of 3 when there should only be 1 and 2
               # Unique value of gender: [ 1.  3. nan  2.]

               count3s = df['gender'].value_counts()[3]
               print(f'Number of 3s: {count3s}') 
               # Number of 3s: 6286
               
               From this we can see that there are 5959 values in the income_groups column with the _typo suffix. We can also see that there are 3 different options for gender, not including nan. There are 6286 3s in the gender column.]
   - Potential Impact: [In this case, becuase there is innacurate naming of the values in the column, there would be inaccurate grouping of the values. Lack of standardization would make it harder to model the data as well.]

6. **[Impossible Dates]**
   - Description: [The year column has years that are past 2024 which would be impossible since that data cannot have been collected yet.]
   - Affected Column(s): [year]
   - Example: [year]
   - Potential Impact: [Having values of dates that are past the present date would cause innacurate measurements as that data could not have been collected yet. There would also be issues with data projection since there may be an inaccurate representation of future data.]


## 2. Data Cleaning Process

### Issue 1: [Duplicate Values]
- **Cleaning Method**: [Use .drop_duplicates() to drop duplicate values for specified columns]
- **Implementation**:
  ```python
  df = df.drop_duplicates(subset=['income_groups', 'age', 'gender', 'year', 'population'], keep=False)
  ```
- **Justification**: [Since these values were duplicated and we still have 1 copy of them, dropping the extra would make more sense than replacing them.]
- **Impact**: 
  - Rows affected: [2950 duplicates]
  - Data distribution change: [Removing duplicates reduces the size of the dataset. It could change statistical measures such as mean and median becuase extreme values will no longer be disproportionately represented. Categorical variables will be affected as well because the frequency of value will change. This affects the mode of that variable.]

### Issue 2: [Missing Values]
- **Cleaning Method**: [Firstly, select the columns that have the float data type. Then replace all the missing values with the median of the column. 
For the objec type column, income_group, we fill the missing values with 'unknown' instead of imputing since it is not a category we can assume the values of.]
- **Implementation**:
  ```python
  floatType = df.select_dtypes(include=['float64']).columns 
  df[floatType] = df[floatType].fillna(df[floatType].median()) 

  objectType = df.select_dtypes(include=['object']).columns 
  df[objectType] = df[floatType].fillna('unknown')
  ```
- **Justification**: [This is best way to fill in missing values for float type columns becuase by using the median value, we are not contributing to any data skewing. 
Similarly, when filling in the missing values of the object type column, rather than creating more NA values, we replace missing values with 'unknown' rather than incorrectly
assuming the person's income group.]
- **Impact**: 
  - Rows affected: [30978]
  - Data distribution change: [Float type columns will have more complete data to be analyzed yielding better results.
  Object type columns will have better representation and will make it easier to model and understand.]

### Issue 3: [Outliers]
- **Cleaning Method**: [We calculate the IQR, set the lower and upper bounds of the data, and filter the column for data that is between the upper and lower bounds.]
- **Implementation**:
  ```python
  Q1 = df['population'].quantile(0.25)
  Q3 = df['population'].quantile(0.75)
  IQR = Q3 - Q1

  lowerBound = Q1 - 1.5 * IQR
  upperBound = Q3 + 1.5 * IQR

  df['population'] = df['population'].where((df['population'] >= lowerBound) & (df['population'] <= upperBound), other=None)
  ```
- **Justification**: [Dropping outliers allows better understanding and representation of data. Also, it could account for removing data points collected due to confounding variables increasing the accuracy of the dataset.]
- **Impact**: 
  - Rows affected: [population column affected]
  - Data distribution change: [The distribution of the data will be more normalized as it will not longer be accounting for extreme values which are not useful for analysis.]

### Issue 4: [Inconsistencies]
- **Cleaning Method**: [The income_groups and gender column include values which are inconsistent from the allowed values. Income_groups includes a view values with the suffix _typo which we replace with the accurate naming convenction.
The gender column can only have 1 or 2 for male or female but includes the value 3 which is not consistent with the values of the column. Therefore, this needs to be dropped and replaced with 0
so that it is understood that that information is not known/unavailable.]
- **Implementation**:
  ```python
  df['income_groups'] = df['income_groups'].replace({'high_income_typo':'high_income',
                                                   'lower_middle_income_typo':'lower_middle_income',
                                                   'upper_middle_income_typo':'upper_middle_income'})

  df['gender'] = df['gender'].replace(3.0,0.0) 
  ```
- **Justification**: [Renaming values with _typo allows us to still have a complete dataset but with only valid values.
Similarly, dropping 3s and replacing with 0s allows us to have a complete dataset without losing data but conserving only valid values.]
- **Impact**: 
  - Rows affected: [income groups and gender columns affected]
  - Data distribution change: [The dataset will become more coherent and complete with these changes. This would allow for more understandable data analysis.]

### Issue 5: [Impossible Dates]
- **Cleaning Method**: [Data cannot be collected for years past 2024. Therefore, all data associated with years past 2024 shoudl be dropped.]
- **Implementation**:
  ```python
  df['year'] = df['year'].where(df['year'] <= 2024) 
  df['year'] = df['year'].ffill()
  ```
- **Justification**: [Since it is technically impossible to collect data from the future, we need to drop all rows with years past 2024
so that we have an accurate dataset of data collected from 2024 and before. Instead of filling the now NA rows with ffill() allows us to
have data that is based on the other data that came the row before it.]
- **Impact**: 
  - Rows affected: [63238]
  - Data distribution change: [This will give us a more realistic dataset and help with future projections if we want to see how the analysis can 
  be useful in a diagnostic setting in the future. If we were to have included incorrect dates, we would be misrepresenting the data with any analysis
  or models that came from this dataset.]


## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv (or whatever you named it)
- **Rows**: [119874]
- **Columns**: [5]

### Column Details
| Column Name      | Data Type   | Non-Null Count | Unique Values |  Mean         |
|------------------|-------------|----------------|---------------|---------------|
| [income_groups]  | [Object]    | [119874]       | [6]           | [0]           |
| [age]            | [float64]   | [119874]       | [101]         | [49.986903]   |
| [gender]         | [float64]   | [119874]       | [3]           | [1.398001]    |
| [year]           | [float64]   | [119874]       | [75]          | [2005.433981] |
| [population]     | [float64]   | [116388]       | [108794]      | [8.881248e+06]|

### Summary of Changes
- [Major Changes made: duplicated values were dropped in all columns, naming convention inconsistencies were dealth with through renaming and imputing, 
missing values were imputed by median values if float variable or filled with unknown for object variable, outliers were removed for more accurate analysis,
impossible dates listed from past 2024 were removed and filled with dates of preceding rows for more accurate representation of the data.]
- [The number of unique values decreased for all columns due to removing duplicate values. The means also dropped slightly becuase
incorrect data was either removed or redone. Non-null counts increased siginificantly after missing values were imputed.]