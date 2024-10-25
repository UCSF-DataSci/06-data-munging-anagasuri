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
  - Rows affected: [FILL OUT]
  - Data distribution change: [Removing duplicates reduces the size of the dataset. It could change statistical measures such as mean and median becuase extreme values will no longer be disproportionately represented. Categorical variables will be affected as well because the frequency of value will change. This affects the mode of that variable.]

### Issue 2: [Missing Values]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Duplicate Values]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 3: [Outliers]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Duplicate Values]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 4: [Inconsistencies]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Duplicate Values]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 5: [Impossible Dates]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Duplicate Values]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]


## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv (or whatever you named it)
- **Rows**: [Your answer]
- **Columns**: [Your answer]

### Column Details
| Column Name | Data Type | Non-Null Count | #Unique Values |  Mean  |
|-------------|-----------|----------------|----------------|--------|
| [Column 1]  | [Type]    | [Count]        | [#Unique]      | [Mean] |
| ...         | ...       | ...            | ...            | ...    |

### Summary of Changes
- [List major changes made to the dataset]
- [Discuss any significant changes in data distribution]