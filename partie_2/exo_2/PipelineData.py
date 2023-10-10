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

def extract_model(data):
    
    selected_columns = ["Sex", "Pclass", "Age", "Survived", "Fare", "Embarked"]
    data_subset = data[selected_columns]
    print(data_subset)
    # Renommage la colonne "fare" en "price" et "Pclass" en "Class"
    data_subset.columns = ['sex', 'class', 'age', 'survived', 'price', 'embarked']
    donnees_passager = data_subset.to_dict(orient="records")
    return donnees_passager
    
def transform(data):
    #Supprimer les lignes avec les valeurs manquantes
    data_cleaned = data
    return data_cleaned

def load(data):
    with open('passenger.json', 'w') as file:
        json.dump(data,file)        


