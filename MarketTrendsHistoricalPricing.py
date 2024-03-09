import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("D:/Nexthikes/Project3/housing_data.csv")

# Assuming the dataset includes a 'YearBuilt' column representing the year each house was built
# If not, you may need to use a different time column
# Convert 'YearBuilt' to datetime if it's not already in datetime format
data['YearBuilt'] = pd.to_datetime(data['YearBuilt'])

# Group the data by year and calculate average house price for each year
average_price_per_year = data.groupby(data['YearBuilt'].dt.year)['SalePrice'].mean()

# # Plot the historical pricing trends over time
plt.figure(figsize=(12, 6))
sns.lineplot(x=average_price_per_year.index, y=average_price_per_year.values)
plt.title('Historical Pricing Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Average Sale Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()



# Inspect the 'MoSold' column
print(data['MoSold'].unique())

# Convert the 'MoSold' column to datetime format
# You may need to handle any unexpected values in the 'MoSold' column
data['MoSold'] = pd.to_datetime(data['MoSold'], errors='coerce')

# Extract the year from the 'MoSold' column
data['YrSold'] = data['MoSold'].dt.year

# Aggregate the data over different time periods (e.g., yearly)
yearly_prices = data.groupby('YrSold')['SalePrice'].mean().reset_index()

# Plot the trend in house prices over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='YrSold', y='SalePrice', data=yearly_prices, marker='o', color='b')
plt.title('Trend in House Prices Over Time')
plt.xlabel('Year Sold')
plt.ylabel('Average House Price')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()