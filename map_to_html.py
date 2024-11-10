import pandas as pd
import folium
from folium.plugins import MarkerCluster

data_path = "data/processed/data_map.csv"


df = pd.read_csv(data_path, sep=";")

# Coordonnées de Rennes (Bretagne)
rennes_lat, rennes_lon = 48.1173, -1.6778

# Créer la carte centrée sur Rennes (Bretagne)
carte_bretagne = folium.Map(location=[rennes_lat, rennes_lon], zoom_start=8)

# Coordonnées de Rennes (Bretagne)
rennes_lat, rennes_lon = 48.1173, -1.6778

# Créer la carte centrée sur Rennes (Bretagne)
carte_bretagne = folium.Map(location=[rennes_lat, rennes_lon], zoom_start=8)

# On crée le dictionnaire d'association d'une couleur à chaque étiquette DPE
colors={"A":"darkgreen","B":"green","C":"lightgreen","D":"beige","E":"orange","F":"pink","G":"red"}

# On initialise la fonctionnalité MarkerCluster
marker_cluster = MarkerCluster().add_to(carte_bretagne)

# On ajoute le clustering des marqueurs selon le degré de zoom
for idx, row in df.iterrows():
    if pd.notna(row['lat']) and pd.notna(row['lon']):
        # Create a popup text for each marker
        popup=f"Type de bâtiment: {row['Type_bâtiment']}<br>Surface habitable: {row['Surface_habitable_logement']} m²<br>Étiquette DPE : {row['Etiquette_DPE']}",
        
        # Create a marker for each property and add it to the marker cluster
        folium.Marker(
            location=[row['lat'], row['lon']], icon=folium.Icon(color=colors[row['Etiquette_DPE']], icon='info-sign'),
            popup=popup
        ).add_to(marker_cluster)

# Display the map
#carte_bretagne
carte_bretagne.save('objects/map.html')

