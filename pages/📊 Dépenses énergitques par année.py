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

# Widget de sélection multiple pour la classe DPE
etiquette_dpe_3 = st.multiselect(
"Sélectionnez les classes DPE",
options=["A", "B", "C", "D", "E", "F", "G"],
default=["A", "B", "C", "D", "E", "F", "G"],
label_visibility="hidden"
)

# Filtrer les données en fonction de la sélection
df_filtre_3 = df[df['Etiquette_DPE'].isin(etiquette_dpe_3)]

# Calculer le coût moyen par année de construction pour la classe sélectionnée
df_agg_3 = df_filtre_3.groupby(['Année_construction', 'Etiquette_DPE']).agg({'Coût/m²': 'mean'}).reset_index()

# Créer un histogramme avec Plotly Express
fig_3 = px.line(
    df_agg_3, 
    x="Année_construction", 
    y="Coût/m²",
    color='Etiquette_DPE',
    range_x=[1900,2024], 
    title=f"Dépenses énergétiques par m² (en €) en fonction de l'année de construction",
    labels={"Année_construction": "Année de Construction", "Coût/m²": "Coût/m² moyen"},
    )

# Appliquer les couleurs personnalisées des classes DPE sélectionnées
for trace in fig_3.data:
    # Appliquer la couleur à chaque trace (ligne) basée sur l'étiquette DPE
    trace.line.color = couleurs_DPE[trace.name]

# Afficher le graphique dans la deuxième colonne
st.plotly_chart(fig_3)  

# Convertir le graphique en image PNG
img_bytes_3 = fig_3.to_image(format="png")

# Créer un bouton de téléchargement pour l'image PNG
st.download_button(
    label="Télécharger - Dépense €/m² selon l'année de construction",
    data=img_bytes_3,
    file_name="graphique_Euros par m² selon l'année.png",
    mime="image/png"
)