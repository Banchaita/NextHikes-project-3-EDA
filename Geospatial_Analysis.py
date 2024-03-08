import pandas as pd
import plotly.express as px
import folium


# Load the dataset
data = pd.read_csv("D:/Nexthikes/Project3/housing_data.csv")

# # Create a scatter plot of house prices on a map
# fig = px.scatter_mapbox(data, lat="LotFrontage", lon="LotArea", hover_name="MSZoning",color="SalePrice", zoom=10)
# fig.update_layout(mapbox_style="open-street-map")
# fig.update_layout(title="Distribution of House Prices")
# fig.show()


# Create a Folium map
map = folium.Map(location=[data['LotFrontage'].mean(), data['LotArea'].mean()], zoom_start=10)

# Add markers for each house with popup showing house price
for index, row in data.iterrows():
    folium.Marker([row['LotFrontage'], row['LotArea']], popup=f"${row['SalePrice']}").add_to(map)

# Display the map
map.save('map.html')
