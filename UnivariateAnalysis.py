import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Load the dataset into a DataFrame
data = pd.read_csv("D:/Nexthikes/Project3/housing_data.csv")

# # Plot histogram
plt.hist(data['MasVnrArea'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Variable')
plt.ylabel('BsmtUnfSF')
plt.title('Histogram of Variable')
plt.show()

# Plot KDE plot of house prices
sns.kdeplot(data['WoodDeckSF'], shade=True, color='skyblue')
plt.xlabel('YrSold')
plt.ylabel('SalePrice')
plt.title('Kernel Density Estimation (KDE) Plot of House Prices')
plt.show()

# Plot boxplot of house prices
sns.boxplot(x=data['SalePrice'], color='skyblue')
plt.xlabel('SalePrice')
plt.title('Boxplot of House Prices')
plt.show()


# Plot violin plot of house prices
sns.violinplot(data=data, y='SalePrice', color='skyblue')
plt.ylabel('SalePrice')
plt.title('Violin Plot of House Prices')
plt.show()

# Plot countplot for a categorical variable
sns.countplot(x='GrLivArea', data=data, palette='pastel')
plt.xlabel('GrLivArea')
plt.ylabel('GarageYrBlt')
plt.title('Countplot of Variable')
plt.show()

# Function to compute ECDF
def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data) + 1) / len(data)
    return x, y

print("Function to compute ECDF:",ecdf)

# Compute ECDF of house prices
x, y = ecdf(data['SalePrice'])

# Plot ECDF
plt.plot(x, y, marker='.', linestyle='none', color='skyblue')
plt.xlabel('SalePrice')
plt.ylabel('ECDF')
plt.title('ECDF Plot of House Prices')
plt.show()


# Plot rug plot of house prices
sns.rugplot(data['SalePrice'], height=0.1, color='skyblue')
plt.xlabel('SalePrice')
plt.title('Rug Plot of House Prices')
plt.show()

# Scatter plot of 'OverallQual' vs 'HousePrice'
plt.scatter(data['OverallQual'], data['SalePrice'], color='skyblue')
plt.xlabel('OverallQual')
plt.ylabel('SalePrice')
plt.title('Scatter Plot: Overall Qual vs House Price')
plt.show()

# Pairplot of selected numerical variables
sns.pairplot(data[['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'YrSold', 'SalePrice']])
plt.suptitle('Pairplot of Selected Numerical Variables', y=1.02)
plt.show()

# Compute correlation matrix
correlation_matrix = data[['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'YearBuilt', 'SalePrice']].corr()
print("correlation_matrix:",correlation_matrix)

# Plot heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Selected Numerical Variables')
plt.show()

# Boxplot of 'OverallQual' vs 'HousePrice'
sns.boxplot(x=data['OverallQual'], y=data['SalePrice'], palette='pastel')
plt.xlabel('Overall Quality')
plt.ylabel('SalePrice')
plt.title('Boxplot: Overall Quality vs SalePrice')
plt.show()

# Bar plot of 'OverallQual' vs 'HousePrice'
sns.barplot(x=data['OverallQual'], y=data['SalePrice'], estimator=np.median, palette='pastel')
plt.xlabel('Overall Quality')
plt.ylabel('Median House Price')
plt.title('Bar Plot: Overall Quality vs Median House Price')
plt.show()

# Select only numerical columns
numerical_columns = data.select_dtypes(include=['int', 'float']).columns
print("Select only numerical columns:",numerical_columns)

 # Calculate correlation matrix
correlation_matrix = data[numerical_columns].corr()
print("Calculate correlation matrix:",correlation_matrix)

# Plot correlation matrix as heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()



# Plot pairplot of selected numerical variables
sns.pairplot(data[['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'YearBuilt', 'SalePrice']])
plt.suptitle('Pairplot of Selected Numerical Variables', y=1.02)
plt.show()

# Jointplot of 'GrLivArea' and 'Sale Price'
sns.jointplot(x='GrLivArea', y='SalePrice', data=data, kind='reg', color='skyblue')
plt.xlabel('Above Ground Living Area')
plt.ylabel('SalePrice')
plt.title('Jointplot: GrLivArea vs Sale Price')
plt.show()

# Create PairGrid
g = sns.PairGrid(data[['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'YearBuilt', 'SalePrice']])
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
plt.suptitle('PairGrid of Selected Numerical Variables', y=1.02)
plt.show()

