# Machine Learning sur les données d'Enedis
- Objectif 1 : prédiction de l'étiquette DPE d'un logement
- Objectif 2 : prédiction de la consommation énergétique d'un logement
- Objectif 3 : déploiement d'une application web Streamlit pour la visualisation et la prédiction

### Contenu du répertoire

```bash
├── data
│   ├── processed
│	│   ├── data_classification.csv
│	│   ├── data_map.csv
│	│   ├── data_regression.csv
│	│   └── full_data_bretagne.csv
├── image
│   └── image_contexte.png
├── mapping
│   └── map.html
├── models
│   ├── rf_tuned_classification.pkl
│	└── rf_tuned_regression.pkl
├── objects
│   ├── OHE_classification.pkl
│   ├── OHE_regression.pkl
│   ├── median_imputer_classification.pkl
│	└── median_imputer_regression.pkl
├── pages
│   ├── 2_📚 Affichage et exportation des données.py
│   ├── 3_🌍 Cartographie.py
│   ├── 4_🎯 Prédiction de l\'étiquette DPE.py
│   ├── 5_📈 Prédiction de la consommation en énergie.py
│   ├── 📊 Coût moyen par m² selon les départements.py
│   ├── 📊 Coût par m² selon l'année de construction.py
│   ├── 📊 Coût par m² selon la surface habitable.py
│	├── 📊 proportion des classes DPE par département.py
├── Accueil.py
├── map_to_html.py
├── pipeline.py
├── preprocessing.ipynb
├── preprocessing_functions.py
├── README.md
└── requirements.txt

```
---
Le dossier racine contient un notebook (EDA et modélisation) ainsi que les différents fichiers .py nécessaires au bon développement des modèles. Il contient aussi la page d'accueil de l'interface web, la fonction d'exportation de la cartographie en .html, le fichier d'installation des dépendances nécessaires au bon déploiement de l'interface ainsi que le présent ReadMe.

Enfin, on retrouve deux documents .pdf :
- Documentation technique : inclue la justification de tout le raisonnement et processus allant de l'extraction des données jusqu'au déploiement des modèles.
- Documentation fonctionnelle : inclue la notice d'utilisation de l'interface web Streamlit.

Passons en revue les sous-dossiers du répertoire:

---
```bash
├── data
│   └── processed
```
Contient les fichiers .csv ayant servis pour l'entraînement et l'évaluation des modèles de Random Forest pour la classification et pour la régression, ainsi que les fichiers permettant la visualisation des données sur l'application web.

---
```bash
├── image
```
Contient les images utilisées pour afficher dans l'application web

---
```bash
├── mapping
```
Contient le fichier html de la cartographie des données visualisable sur l'application web.

---
```bash
├── models
```

Contient les modèles finaux de classification et de régresion au format .pkl pour une exécution simplifiée sur l'application web.

---
```bash
├── objects
```
Contient les imputateur de données manquantes ainsi que les encodeurs one-hot ajustés sur les données train pour une utilisation ultérieure sur de nouvelles données. Il y a un imputateur et un encodeur one-hot pour les données de classification et pour celles de régression.

---
```bash
├── pages
```
Contient les pages de l'application web.

### Installer l'application

Dans un terminal :

Clonez le repository (https://github.com/YacineAyachi/m2_enedis):  
`git clone https://github.com/YacineAyachi/m2_enedis.git`

Créez un environnement virtuel:
Si le package `virtualenv` n'est pas encore installé:  
`pip install virtualenv` 

Avec `cd`, allez dans le répertoire où vous souhaitez stocker vos environnements virtuels.
Dans le terminal, créez un environnement virtuel du nom de `env-enedis` :  
`py -m venv env-enedis`
Avec `cd`, allez dans le sous-dossier `Scripts` du dossier que vous venez de créer (`env-enedis`), et activez l'environnement virtuel:  
`activate.bat`
Avec `cd`, retournez dans le répertoire que vous avez précédemment cloné et installer les packages et dépendances nécessaires au bon fonctionnement de l'application web:  
`pip install -r requirements.txt`

Exécutez l'application:  
`streamlit run Accueil.py`


### Ressources

- Une captation vidéo de ~5mn de l'interface web est disponible sur ce lien YouTube : https://www.youtube.com/watch?v=NIyEpbulisQ
- L'application web est accessible via ce lien : https://appapp-4wrognttkv4qrzelkbw8w9.streamlit.app/
