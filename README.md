# Airbnb NYC — Price Prediction & Strategy Lab

## Présentation

Ce projet vise à aider à la prise de décision d'investissement dans le marché Airbnb de New York, à partir des données de 2019.

L'objectif est d'identifier les quartiers les plus intéressants, d'analyser les prix et l'activité des logements, puis de développer un modèle de Machine Learning capable d'estimer le prix par nuit.

En comparant les prix affichés aux prix prédits, nous cherchons à repérer des opportunités d'investissement potentielles.

Cependant, les prédictions comportent une marge d'erreur et les données ne permettent pas de calculer la rentabilité réelle des investissements.

## Données

- Dataset : `AB_NYC_2019.csv`
- Nettoyage des valeurs manquantes, des doublons et des valeurs aberrantes
- Analyse exploratoire des prix selon les quartiers et les types de logements

## Modélisation

Nous utilisons un **Random Forest Regressor**, avec une validation croisée à 5 plis pour comparer les hyperparamètres.

Configuration retenue :
- `n_estimators=100`
- `max_depth=12`
- `min_samples_leaf=5`

Nous testons également une transformation logarithmique du prix.

## Résultats

Le Random Forest initial obtient sur les données de test :

- MAE : 47,86 $
- RMSE : 86,90 $
- R² : 0,441

Le projet compare également les prix affichés aux prix prédits pour identifier des logements potentiellement sous-évalués. Ces écarts ne constituent toutefois pas une preuve de sous-évaluation, compte tenu des erreurs du modèle.

## Interface

Une interface **Streamlit** permet de saisir les caractéristiques d'un logement et d'obtenir une estimation de son prix par nuit.

Pour lancer l'application :

```bash
python -m streamlit run app.py
```

## Fichiers principaux

- `strategy-lab.ipynb` : nettoyage, analyse et modélisation
- `Data/AB_NYC_2019.csv` : données utilisées
- `model.pkl` : modèle entraîné et colonnes sauvegardées
- `predict.py` : chargement du modèle
- `app.py` : interface Streamlit

## Limites

Les prédictions comportent une marge d'erreur importante, notamment pour les logements les plus chers. Les résultats doivent donc être considérés comme des estimations et non comme des évaluations certaines de la valeur des biens.