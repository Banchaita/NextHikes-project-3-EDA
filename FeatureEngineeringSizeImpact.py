import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("D:/Nexthikes/Project3/housing_data.csv")

# Explore the data
print(data.head())
print(data.info())
print(data.describe())

# Identify correlations
numeric_data = data.select_dtypes(include=['int', 'float'])
correlation_matrix = numeric_data.corr()
print(correlation_matrix)

# Visualize correlations using a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Analyze size vs. price
sns.scatterplot(x='LotArea', y='SalePrice', data=data)
plt.title('Lot Area vs. Sale Price')
plt.xlabel('Lot Area')
plt.ylabel('Sale Price')
plt.show()

# Analyze other features vs. price
# Example: Number of bedrooms vs. Sale Price
sns.boxplot(x='BedroomAbvGr', y='SalePrice', data=data)
plt.title('Number of Bedrooms vs. Sale Price')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Sale Price')
plt.show()


# Scatter plot: Bedrooms vs. SalePrice
plt.figure(figsize=(8, 6))
sns.scatterplot(x='BedroomAbvGr', y='SalePrice', data=data)
plt.title('Number of Bedrooms vs. Sale Price')
plt.xlabel('Bedrooms')
plt.ylabel('Sale Price')
plt.show()


# Pair plot: Pairwise relationships between numerical features and SalePrice
sns.pairplot(data[['SalePrice', 'BedroomAbvGr', 'FullBath', 'GrLivArea']])
plt.show()

# Correlation matrix
correlation_matrix = data[['SalePrice', 'BedroomAbvGr', 'FullBath', 'GrLivArea']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()