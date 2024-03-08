import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
data = pd.read_csv("D:/Nexthikes/Project3/housing_data.csv")

# Explore the first few rows of the dataset
print(data.head())

# # Visualize the relationship between square footage and house prices
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='TotalBsmtSF', y='SalePrice', data=data)
# plt.title('Square Footage vs. House Prices')
# plt.xlabel('Square Footage')
# plt.ylabel('House Price')
# plt.show()


# # Compare the distribution of house prices across different neighborhoods
# plt.figure(figsize=(12, 8))
# sns.boxplot(x='Neighborhood', y='SalePrice', data=data)
# plt.title('Neighborhood vs. House Prices')
# plt.xlabel('Neighborhood')
# plt.ylabel('House Price')
# plt.xticks(rotation=45)
# plt.show()

# Compare the average house prices for different property types
# plt.figure(figsize=(10, 6))
# sns.barplot(x='SaleType', y='SalePrice', data=data, estimator=np.mean)
# plt.title('SaleType vs. Average House Prices')
# plt.xlabel('SaleType')
# plt.ylabel('Average House Price')
# plt.show()

# Pairplot to visualize relationships between multiple features and house prices
# sns.pairplot(data[['TotalBsmtSF', 'BedroomAbvGr', 'FullBath', 'SalePrice']])
# plt.suptitle('Pairplot of Numerical Features vs. House Prices', y=1.02)
# plt.show()

# Visualize the correlation matrix
# numeric_data = data.select_dtypes(include=['int', 'float'])
# correlation_matrix = numeric_data.corr()
# plt.figure(figsize=(12, 10))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Correlation Matrix')
# plt.show()

# Select amenities to analyze
amenities = ['SwimmingPool', 'GarageType', 'Fireplaces']

# Visualize impact on house prices
# plt.figure(figsize=(12, 8))
# for amenity in amenities:
#     sns.boxplot(x=amenity, y='SalePrice', data=data)
# plt.title('Impact of Amenities on House Prices')
# plt.xlabel('Amenity')
# plt.ylabel('House Price')
# plt.xticks(rotation=45)
# plt.show()


# Analyze customer feedback (if available)
# For example, if customer feedback is available in the dataset as 'Feedback' column:
feedback_data = data[['PoolArea', 'GarageType', 'Fireplaces', 'SaleCondition']]
print("feedback_data:",feedback_data)

