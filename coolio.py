import pandas as pd
import folium
from folium.plugins import HeatMap

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/kthukral/Downloads/drone_flight_dataset_dedrone (1)/2023-05-01_00-00-00_clean.csv')

# Create a map centered around the mean latitude and longitude of all drone points
center_lat = df['DetectionLatitude'].mean()
center_lon = df['DetectionLongitude'].mean()
drone_map = folium.Map(location=[center_lat, center_lon], zoom_start=4)

# Add markers for each drone point
for _, row in df.iterrows():
    folium.Marker(
        location=[row['DetectionLatitude'], row['DetectionLongitude']],
        popup=f"Drone ID: {row['DroneId']}<br>Timestamp: {row['SensorTime']}<br>Altitude: {row['Altitude']}"
    ).add_to(drone_map)

# Create a heatmap to visualize the density of drone points
heat_data = [[row['DetectionLatitude'], row['DetectionLongitude']] for _, row in df.iterrows()]
HeatMap(heat_data).add_to(drone_map)

# Analyze trends of where the drones are flying
print("Trend Analysis:")
print("----------------")

# Count the number of unique drones
num_drones = df['DroneId'].nunique()
print(f"Number of unique drones: {num_drones}")

# Find the most common drone type
most_common_drone = df['DroneType'].mode()[0]
print(f"Most common drone type: {most_common_drone}")

# Find the average altitude of the drones
avg_altitude = df['Altitude'].mean()
print(f"Average altitude: {avg_altitude:.2f} meters")

# Find the drone with the highest altitude
max_altitude_drone = df.loc[df['Altitude'].idxmax(), 'DroneId']
max_altitude = df['Altitude'].max()
print(f"Drone with the highest altitude: {max_altitude_drone} (Altitude: {max_altitude:.2f} meters)")

# Display or save the map
drone_map.save("all_drone_points.html")
print("Map saved as 'all_drone_points.html'")