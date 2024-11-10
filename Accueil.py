import streamlit as st

# st.title("m2-enedis")
st.header("Contexte du projet")

# Disposition des graphiques sur la page : on choisit 2 colonnes
colonnes_contexte = st.columns([1,1])
# Première colonne
with colonnes_contexte[0] :
    st.markdown(
        """
        <style>
        .justified-text {
            text-align: justify;
        }
        </style>
        
        <div class="justified-text">
        En France, la maîtrise de la consommation énergétique est devenue un enjeu majeur, tant pour les ménages que pour les fournisseurs d’énergie. Dans un contexte de hausse des coûts et de transition écologique, vos clients cherchent à mieux comprendre et optimiser leurs usages pour réduire leur facture et leur impact environnemental.
        <br><br>
        Greentech vous propose une solution web innovante pour répondre à ces attentes. Notre interface comprend un <strong style="color:green;">dashboard interactif</strong style="color:green;"> qui permet à vos clients de visualiser comment se positionne leur <strong style="color:green;">consommation énergétique</strong style="color:green;"> en fonction de leur <strong style="color:green;">diagnostic DPE</strong style="color:green;">. Ces données sont également visibles géographiquement sur notre <strong style="color:green;">carte interactive</strong style="color:green;">.
        <br><br>
        En complément, notre <strong style="color:green;">outil de prédiction</strong style="color:green;"> basé sur des algorithmes avancés utilise les données récoltées sur toute la région Bretagne. Grâce à Greentech, offrez à vos clients une expérience enrichie et accompagnez-les vers une <strong style="color:green;">gestion énergétique plus responsable et optimisée</strong style="color:green;">.
        </div>
        """, 
        unsafe_allow_html=True
    )
# Deuxième colonne
with colonnes_contexte[1] :
    # Chargement et affichage de l'image
    st.image("image/image_contexte.png")
