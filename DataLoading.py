import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("D:/Nexthikes/Project3/housing_data.csv")

# Display the first few rows of the dataset
print("Display the first few rows of the dataset:",data.head())

# Display the last few rows of the dataset
print("Display the last few rows of the dataset:",data.tail())

# Summary statistics of the dataset
print("Summary statistics of the dataset:",data.describe())

# Selecting a single column
column = data['LotShape']
print("Selecting a single column:",column)

# Selecting multiple columns
columns = data[['LotConfig', 'Neighborhood']]
print("Selecting multiple columns:",columns)


# Check the data type of the
print("Check the data type of the:",data['LotConfig'].dtype)

# Convert data type if necessary:
data['LotConfig'] = pd.to_numeric(data['LotConfig'], errors='coerce')
print("Convert data type if necessary:",data)

# Selecting rows based on conditions
value = "AllPub"
conditions = data[data['Utilities'] == value]
print("Selecting rows based on conditions:", conditions)
condition = data[data['Utilities'] > value]
print("Selecting rows based on conditions:", condition)


# Handling missing values
data.dropna()  # Drop rows with missing values
data.fillna(value)  # Fill missing values with a specific value

# Removing duplicates
data.drop_duplicates()

# Sorting data
data.sort_values(by='Utilities', ascending=False)
print("Sorting data:",data)

# Grouping data

# Check column names
print("Check column names",data.columns)

# Check for missing values
print("Check for missing values:",data['Neighborhood'].isnull().sum())

# Check column data type
print("Check column data type:",data['Neighborhood'].dtype)

# Display unique values in the 'Neighborhood' column
print("Display unique values in the 'Neighborhood' column:",data['Neighborhood'].unique())

# Convert the 'Neighborhood' column to string if necessary
data['Neighborhood'] = data['Neighborhood'].astype(str)
print("Convert the 'Neighborhood' column to string if necessary:",data)

# Convert incompatible columns
data['Neighborhood'] = pd.to_numeric(data['Neighborhood'], errors='coerce')
print("Convert incompatible columns:",data)

# Group the data by 'Neighborhood' and calculate the mean
grouped_data = data.groupby('Neighborhood').mean()
print("Group the data by 'Neighborhood' and calculate the mean:",grouped_data)


# Histogram
data['MasVnrArea'].hist()
plt.show()

# If the lengths are different, you need to handle the data appropriately
# For example, you can remove rows with missing values in one of the columns
data_cleaned = data.dropna(subset=['MasVnrArea', 'BsmtUnfSF'])

# Plot the scatter plot
plt.scatter(data_cleaned['MasVnrArea'], data_cleaned['BsmtUnfSF'])
plt.xlabel('MasVnrArea')
plt.ylabel('BsmtUnfSF')
plt.title('Scatter plot')
plt.show()