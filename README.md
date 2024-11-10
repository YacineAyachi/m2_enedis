# Machine Learning sur les données d'Enedis
- Objectif 1 : prédiction de l'étiquette DPE d'un logement
- Objectif 2 : prédiction de la consommation énergétique d'un logement
- Objectif 3 : déploiement d'une application web Streamlit pour la visualisation et la prédiction

### Contenu du répertoire

```bash
├── data
│   └── processed
│	│   ├── data_classification.csv
│	│   ├── data_map.csv
│	│   ├── data_regression.csv
│	│   └── full_data_bretagne.csv
├── image
│   └── image_contexte.png
├── models
│   ├── rf_tuned_classification.pkl
│	└── rf_tuned_regression.pkl
├── objects
│   ├── OHE_classification.pkl
│   ├── OHE_regression.pkl
│   ├── image.jpg
│   ├── map.html
│   ├── median_imputer_classification.pkl
│	└── median_imputer_regression.pkl
├── pages
│   ├── 2_📚 Affichage et exportation des données.py
│   ├── 3_🌍 Cartographie.py
│   ├── 4_🎯 Prédiction de l\'étiquette DPE.py
│   ├── 5_📈 Prédiction de la consommation en énergie.py
│   ├── 📊 Coût moyen par m² selon les départements.py
│   ├── 📊 Coût par m² selon l\'année de construction.py
│   ├── 📊 Coût par m² selon la surface habitable.py
│	└── 📊 proportion des classes DPE par département.py
├── Accueil.py
├── map_to_html.py
├── pipeline.py
├── preprocessing.ipynb
├── preprocessing_functions.py
├── README.md
└── requirements.txt

```
--
Passons en revue les dossiers intéressants
--
```bash
├── data
│   └── processed
```
Contient les fichiers .csv ayant servis pour l'entraînement et l'évaluation des modèles de Random Forest pour la classification et pour la régression, ainsi que les fichiers permettant la visualisation des données sur l'application web.

--
```bash
├── models
```

Contient les modèles finaux de classification et de régresion au format .pkl pour une exécution simplifiée sur l'application web.

--


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

### Comment utiliser ce projet

