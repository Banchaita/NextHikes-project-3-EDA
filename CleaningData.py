import pandas as pd
import numpy as np

# Load the dataset into a DataFrame
data = pd.read_csv("D:/Nexthikes/Project3/housing_data.csv")

# Handling Missing Values
# Identify columns with missing values
missing_values = data.isnull().sum()
print("Columns with missing values:")
print(missing_values[missing_values > 0])

# Impute missing values or delete rows/columns with missing values
# For example, you can impute missing numerical values with the mean or median
data['LotFrontage'].fillna(data['LotFrontage'].median(), inplace=True)
# For categorical variables, you can impute missing values with the mode
data['Alley'].fillna('None', inplace=True)
# Alternatively, you can drop rows with missing values
data.dropna(subset=['GarageType'], inplace=True)

# Removing Duplicates
# Identify and remove duplicate rows
data.drop_duplicates(inplace=True)

# Addressing Anomalies
# Identify and handle any anomalies in the data (e.g., outliers)
# For example, you can filter out outliers based on certain criteria
data = data[data['SalePrice'] < 500000]  # Example: Filter out houses with sale price above $500,000

# After cleaning the dataset, you can save it to a new CSV file if needed
# data.to_csv("cleaned_housing_data.csv", index=False)


# Remove rows with any missing values
data_cleaned = data.dropna()

# Remove columns with any missing values
data_cleaned = data.dropna(axis=1)

# Remove rows with a threshold number of non-null values
data_cleaned = data.dropna(thresh=2)


# Remove duplicate rows based on all columns
data_cleaned = data.drop_duplicates()

# Remove duplicate rows based on specific columns
data_cleaned = data.drop_duplicates(subset=['GrLivArea', 'Electrical'])
print("data_cleaned:",data_cleaned)

# Example: Correcting inconsistent values in a categorical column
data['HeatingQC'] = data['HeatingQC'].replace({'incorrect_value': 'correct_value'})
print("Correcting inconsistent values in a categorical column:",data)


# Example: Applying data transformation (e.g., log transformation) to handle skewness
data['1stFlrSF'] = np.log(data['1stFlrSF'])

print("Applying data transformation:",data)


