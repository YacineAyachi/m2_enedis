import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# # Path to the saved map.html file
# map_path = "objects/map.html"

# # Cache the HTML map file loading function
# @st.cache_data
# def load_map(path):
#     with open(path, "r") as file:
#         return file.read()

# # Affiche un message de chargement
# st.write("Chargement de la carte... ça prend une minute")

# # Une fois que la progression est à 100%, charge la carte
# html_map = load_map(map_path)
# zoom_start = 10

# # Affiche la carte
# st.components.v1.html(html_map, height=600)


# *********** to show only a sample data on the map *************

# data_path = "data/processed/data_map.csv"

# # Load the dataframe
# df = pd.read_csv(data_path, sep=";")

# # Function to get a random sample of the data
# def generate_sample(df, num_points=100):
#     return df.sample(n=num_points, random_state=42)

# # Function to generate a folium map with the sample data
# def create_map(df_sample):
#     # Coordinates of Rennes (Brittany)
#     rennes_lat, rennes_lon = 48.1173, -1.6778

#     # Create the map centered on Rennes
#     carte_bretagne = folium.Map(location=[rennes_lat, rennes_lon], zoom_start=8)

#     marker_data = [
#         [row['lat'], row['lon'], f"Type de bâtiment: {row['Type_bâtiment']}<br>Surface habitable: {row['Surface_habitable_logement']} m²<br>Étiquette DPE : {row['Etiquette_DPE']}"]
#         for _, row in df_sample.iterrows()
#     ]

#     # Add FastMarkerCluster for better performance
#     FastMarkerCluster(marker_data).add_to(carte_bretagne)

#     return carte_bretagne


# # Streamlit interface
# st.title("Carte Interactive avec échantillon de Données")

# # Generate a random sample of the data (e.g., 100 points)
# df_sample = generate_sample(df, num_points=5000)

# # Create the map with the sample data
# carte_bretagne = create_map(df_sample)

# # Display the map in Streamlit
# st.write("Voici un échantillon des données sur la carte :")
# st.components.v1.html(carte_bretagne._repr_html_(), height=600)

# ********************************************************************
data_path = "data/processed/data_map.csv"

# Charger le dataframe
df = pd.read_csv(data_path, sep=";")

# Coordonnées de Rennes (Bretagne)
rennes_lat, rennes_lon = 48.1173, -1.6778

# Créer la carte centrée sur Rennes (Bretagne)
carte_bretagne = folium.Map(location=[rennes_lat, rennes_lon], zoom_start=8)

# Initialize the MarkerCluster object
marker_cluster = MarkerCluster().add_to(carte_bretagne)

# Sample 1000 rows randomly from the DataFrame
sampled_df = df.sample(n=1000, random_state=42)  # n=1000 to select 1000 random rows

# Add the markers with clustering for the sampled data
for idx, row in sampled_df.iterrows():
    if pd.notna(row['lat']) and pd.notna(row['lon']):
        # Create a popup text for each marker
        popup = f"Type de bâtiment: {row['Type_bâtiment']}<br>Surface habitable: {row['Surface_habitable_logement']} m²<br>Étiquette DPE : {row['Etiquette_DPE']}"
        
        # Create a marker for each property and add it to the marker cluster
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=popup
        ).add_to(marker_cluster)

# Display the map
# carte_bretagne
carte_bretagne


# Interface Streamlit
st.title("Carte Interactive avec échantillon de Données")

# Afficher la carte dans Streamlit
st.write("Voici un échantillon des données sur la carte :")
st.components.v1.html(carte_bretagne._repr_html_(), height=600)
