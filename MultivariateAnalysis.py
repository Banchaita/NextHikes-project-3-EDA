import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset into a DataFrame
data = pd.read_csv("D:/Nexthikes/Project3/housing_data.csv")

# Scatter plot: Square footage vs. SalePrice
plt.figure(figsize=(8, 6))
sns.scatterplot(x='TotalBsmtSF', y='SalePrice', data=data)
plt.title('Square Footage vs. Sale Price')
plt.xlabel('Square Footage')
plt.ylabel('Sale Price')
plt.show()

# Pair plot: Pairwise relationships between numerical features and SalePrice
sns.pairplot(data[['SalePrice', 'TotalBsmtSF', 'BedroomAbvGr', 'FullBath']])
plt.show()

# Compute the correlation matrix
correlation_matrix = data[['SalePrice', 'TotalBsmtSF', 'BedroomAbvGr', 'FullBath']].corr()

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()


