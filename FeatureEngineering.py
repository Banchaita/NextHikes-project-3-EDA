import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer


# Load the dataset
data = pd.read_csv("D:/Nexthikes/Project3/housing_data.csv")

# Display the first few rows of the dataset
print(data.head())

# Example: Total square footage of the house
data['TotalSF'] = data['TotalBsmtSF'] + data['1stFlrSF'] + data['2ndFlrSF']
print("Total square footage of the house:",data)

# Example: Extracting the age of the house from the 'YearBuilt' feature
current_year = 2024
data['HouseAge'] = current_year - data['YearBuilt']
print("Extracting the age of the house from the 'YearBuilt' featur:",data)

# Example: Binning the 'HouseAge' feature into categories
bins = [0, 10, 20, 30, 40, np.inf]
labels = ['0-10', '11-20', '21-30', '31-40', '40+']
data['HouseAgeGroup'] = pd.cut(data['LotFrontage'], bins=bins, labels=labels)
print("Binning the 'HouseAge' feature into categories:",data)


# Example: One-hot encoding for the 'Neighborhood' feature
neighborhood_dummies = pd.get_dummies(data['Neighborhood'], prefix='Neighborhood')
data = pd.concat([data, neighborhood_dummies], axis=1)

print("One-hot encoding for the 'Neighborhood' feature:",data)

# Example: Interaction feature between 'OverallQual' and 'GrLivArea'
data['OverallQual_GrLivArea'] = data['OverallQual'] * data['GrLivArea']
print("Interaction feature between 'OverallQual' and 'GrLivArea':",data)

# Example: Log transformation of 'SalePrice'
data['LogSalePrice'] = np.log1p(data['SalePrice'])
print("Log transformation of 'SalePrice':",data)

# Split the data into features and target
X = data.drop(columns=['SalePrice'])  # Features
y = data['SalePrice']  # Target
print("Split the data into features and target:", y)



# Feature Aggregation
# Example: Aggregating multiple numerical features
data['TotalSF'] = data['TotalBsmtSF'] + data['1stFlrSF'] + data['2ndFlrSF']
print("Aggregating multiple numerical features:",data)

# Example: Aggregating multiple categorical features
data['AllNeighborhoods'] = data['Neighborhood'] + '_' + data['Condition1'] + '_' + data['Condition2']
print("Aggregating multiple categorical features:",data)

# Display the modified dataset with aggregated features
print("Display the modified dataset with aggregated features:",data.head())


# Perform feature aggregation
data_aggregated = data.groupby('MasVnrArea').agg({'LotFrontage': 'mean', 'LotArea': 'count'})

# Reset index if needed
data_aggregated.reset_index(inplace=True)

# Display the aggregated data
print(data_aggregated)

# Drop rows with missing values for demonstration purposes
data.dropna(inplace=True)

# Separate the target variable if necessary
# For example, if 'SalePrice' is the target variable, you can separate it from the features
numerical_columns = data.select_dtypes(include=['int', 'float']).columns
non_numerical_columns = data.select_dtypes(exclude=['int', 'float']).columns
target = data['SalePrice']
features = data.drop(non_numerical_columns, axis=1)
print(features)

# Initialize the scaler
scaler = StandardScaler()

# Fit and transform the features
scaled_features = scaler.fit_transform(features[numerical_columns])
print("Fit and transform the features:",scaled_features)

pca = PCA(n_components=1)  # Specify the number of components
data_pca = pca.fit_transform(scaled_features)

print("data_pca:",data_pca)

features = data[['YearRemodAdd']]

# Initialize PolynomialFeatures transformer
poly = PolynomialFeatures(degree=2, interaction_only=True)

# Generate polynomial features
data_interactions = poly.fit_transform(features)

print("data_interactions:",data_interactions)

columns_to_encode = ['YearBuilt']
# Initialize the OneHotEncoder
encoder = OneHotEncoder()

# Apply OneHotEncoder to encode the selected column(s)
data_encoded = encoder.fit_transform(data[columns_to_encode])
print("data_encoded:",data_encoded)


# Extract the column(s) you want to impute missing values for
feature_to_impute = 'MasVnrArea'
features_to_impute = data[[feature_to_impute]]

# Initialize the imputer
imputer = SimpleImputer(strategy='mean')

# Fit and transform the data to impute missing values
imputed_values = imputer.fit_transform(features_to_impute)

# Replace the missing values in the DataFrame with the imputed values
data[feature_to_impute] = imputed_values

print("Replace the missing values in the DataFrame with the imputed values:",data)