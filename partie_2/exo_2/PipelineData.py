import numpy as np
import urllib.request
import pandas as pd
import json

# Fonction pour charger les données depuis une URL
def requestUrl(url):
    try:
        urldata =  urllib.request.urlopen(url)
        data = pd.read_csv(urldata)
        return data
    except Exception as e:

        print(f"Erreur de chargement de données : {e}")
        return None

# Fonction pour néttoyer les données
def transform(data):
    # Copiez les données pour éviter de modifier les données originales
    cleaned_data = data.copy()

    # Remplacer les valeurs manquantes par la médiane de la colonne 'Age'
    cleaned_data['Age'].fillna(cleaned_data['Age'].median(), inplace=True)
    cleaned_data['Embarked'].fillna(('C'), inplace=True)

    return cleaned_data


# Fonction pour extraire les données en fonction d'un model prédéfini
def extract_model(data):
    
    selected_columns = ["Sex", "Pclass", "Age", "Survived", "Fare", "Embarked"]
    data_subset = data[selected_columns]
    
    # Renommage la colonne "fare" en "price" et "Pclass" en "Class"
    data_subset.columns = ['sex', 'class', 'age', 'survived', 'price', 'embarked']
    donnees_passager = data_subset.to_dict(orient="records")
    return donnees_passager
    

# Fonction pour convertir les données en json
def load(data):
    with open('passenger.json', 'w') as file:
        json.dump(data,file)        
