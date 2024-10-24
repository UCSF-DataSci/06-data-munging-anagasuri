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
   - Description: [When the messy dataset is generated, its data types are:
                  
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
   - Example: [When running: 
              
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

   - Potential Impact: [If pandas had not automatically converted the data types of year and populatin from object to float,
                        it would not be possible to find their statistical summaries. We cannot find stats such as mean or
                        standard deviation if we are using a column that is of type object and not int/float.]

2. **[Duplicate Values]**
   - Description: [Detailed description of the issue]
   - Affected Column(s): [List of columns]
   - Example: [Specific example from the dataset]
   - Potential Impact: [How this could affect analysis if left uncleaned]

3. **[Missing Values]**
   - Description: [Detailed description of the issue]
   - Affected Column(s): [List of columns]
   - Example: [Specific example from the dataset]
   - Potential Impact: [How this could affect analysis if left uncleaned]

4. **[Outliers]**
   - Description: [Detailed description of the issue]
   - Affected Column(s): [List of columns]
   - Example: [Specific example from the dataset]
   - Potential Impact: [How this could affect analysis if left uncleaned]

5. **[Inconsistencies]**
   - Description: [Detailed description of the issue]
   - Affected Column(s): [List of columns]
   - Example: [Specific example from the dataset]
   - Potential Impact: [How this could affect analysis if left uncleaned]

6. **[Impossible Dates]**
   - Description: [Detailed description of the issue]
   - Affected Column(s): [List of columns]
   - Example: [Specific example from the dataset]
   - Potential Impact: [How this could affect analysis if left uncleaned]
[Add more issues as needed]

## 2. Data Cleaning Process

### Issue 1: [Issue Name]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 2: [Next Issue]
- ...


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