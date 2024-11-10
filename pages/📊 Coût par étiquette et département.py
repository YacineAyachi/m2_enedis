import streamlit as st
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")


#chargement des données
nom_fichier = "data/processed/data_classification.csv"
df = pd.read_csv(nom_fichier, sep=";")

# Page setting
st.set_page_config(layout="wide", page_title="Prédiction de la consommation énergétique des logement en Bretagne")


################################################################################
#################### Préparation data pour dashboard ###########################
################################################################################

# Utilisation du code postal pour créer une colonne 'Département'
departements_bretagne = {
    22: "Côtes-d'Armor",
    29: "Finistère",
    35: "Ille-et-Vilaine",
    56: "Morbihan"
}
df['Département'] = df['Code_postal_(brut)'].astype(str).str[:2].astype(int)
df['Département'] = df['Département'].replace(departements_bretagne)

# Nettoyage des codes postaux incohérents (hors Bretagne)
departements_a_garder = ["Côtes-d'Armor", "Finistère", "Ille-et-Vilaine", "Morbihan"]
df = df[df['Département'].isin(departements_a_garder)]

# Filtre sur la surface totale logement (pour retirer les outflyers)
df = df[df['Surface_habitable_logement'] <= 7000]

# Filtre sur l'année de construction (valeurs incohérentes)
df = df[df['Année_construction'] <= 2024]

# Ligne incohérente retirée
df = df[~((df['Coût_total_5_usages'] > 100000) & (df['Type_bâtiment'] == 'maison'))]

# Création d'une variable 'Cout/m²'
df['Coût/m²']=df['Coût_total_5_usages']/df['Surface_habitable_logement']

# Page de data visualisation =================================================================================================================
st.header("Tableau de bord")
st.markdown("Cette page propose une visualisation interactive de différentes données d'intérêt sur la région Bretagne.\n\nDes filtres sont applicables, et il est possible de télécharger les graphiques une fois filtrés.")


# Définir une palette de couleurs personnalisée pour les étiquettes DPE
couleurs_DPE = {
"A": "#5A8C5B",
"B": "#0AAE00",
"C": "#C8D900",
"D": "#FFEF51",
"E": "#FFC54D",
"F": "#FF7A01",
"G": "#FF0028"
}

# Calcul de la moyenne de 'Coût/m²' par 'Etiquette_DPE' et 'Département'
df_agg_4 = df.groupby(['Etiquette_DPE', 'Département']).agg({'Coût/m²': 'mean'}).reset_index()
# Ajouter une colonne de couleurs basée sur 'Etiquette_DPE'
df_agg_4['Couleur'] = df_agg_4['Etiquette_DPE'].map(couleurs_DPE)
# Créer un treemap avec Plotly Express
fig_4 = px.treemap(
    df_agg_4, 
    path=['Etiquette_DPE', 'Département'],  # Catégories principales et sous-catégories
    values='Coût/m²',  # Taille des rectangles basée sur la moyenne du Coût/m²
    title="Coût/m² moyen par Etiquette DPE et Département",
    color='Etiquette_DPE',  # Utilisation de la colonne Etiquette_DPE pour la coloration
    color_discrete_map=couleurs_DPE  # Appliquer le dictionnaire de couleurs personnalisé
    )
# Afficher le graphique dans la deuxième colonne
st.plotly_chart(fig_4)

# Convertir le graphique en image PNG
img_bytes_4 = fig_4.to_image(format="png")

# Créer un bouton de téléchargement pour l'image PNG
st.download_button(
    label="Télécharger - Dépense €/m² moyenne selon DPE",
    data=img_bytes_4,
    file_name="graphique_Euros par m² selon DPE.png",
    mime="image/png"
)