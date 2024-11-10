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

st.markdown("Cette page propose une visualisation interactive de différentes données d'intérêt sur la région Bretagne.\n\nDes filtres sont applicables, et il est possible de télécharger les graphiques une fois filtrés.")

# Disposition des graphiques sur la page : on choisit 2 colonnes
colonnes_dashboard = st.columns([1,1])

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

# Graphique n°1 - barres empilées ---------------------------------------------------------------------------------------------------------

# Compter les occurrences de chaque combinaison de 'Département' et 'Etiquette_DPE'
df_counts = df.groupby(['Département', 'Etiquette_DPE']).size().reset_index(name='Effectifs')

# Créer un tableau croisé dynamique pour obtenir les effectifs par département et étiquette DPE
df_pivot = df_counts.pivot_table(index='Département', columns='Etiquette_DPE', values='Effectifs', aggfunc='sum', fill_value=0)

# Ajouter un widget de sélection multiple pour les départements
with colonnes_dashboard[0]:
    departements = df_pivot.index.tolist()
    selected_departements = st.multiselect("Sélectionnez les départements à afficher", options=departements, default=departements)

    # Vérifier que la sélection n'est pas vide pour éviter les erreurs
    if selected_departements:
        # Filtrer les données en fonction des départements sélectionnés
        filtered_df_pivot = df_pivot.loc[selected_departements]      

        # Créer le graphique à barres empilées avec Plotly
        fig_1 = px.bar(
            filtered_df_pivot,
            x=filtered_df_pivot.index,
            y=filtered_df_pivot.columns,
            title="Etiquettes DPE selon les départements de Bretagne",
            labels={'value': 'Total des étiquettes', 'Département': 'Département', 'Etiquette_DPE': 'cliquer pour filtrer<br>les étiquettes DPE'},
            height=400,
            color_discrete_map=couleurs_DPE  # Appliquer les couleurs personnalisées
        )

        # Afficher le graphique dans Streamlit (colonne 0)
        colonnes_dashboard[0].plotly_chart(fig_1)

        # Convertir le graphique en image PNG
        img_bytes_1 = fig_1.to_image(format="png")

        # Créer un bouton de téléchargement pour l'image PNG
        st.download_button(
            label="Télécharger - Etiquettes DPE / département",
            data=img_bytes_1,
            file_name="graphique_dpe.png",
            mime="image/png"
        )

    else:
        st.write("Veuillez sélectionner au moins un département pour afficher le graphique.")