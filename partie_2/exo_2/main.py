import urllib.request
from PipelineData import requestUrl , transform , load , extract_model


# Chargement de la donnée
data = requestUrl("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Néttoyage de données
data_cleaned = transform(data)

# Extraire le model
donnees_passager = extract_model(data_cleaned)

# Création du fichier json
load(donnees_passager)