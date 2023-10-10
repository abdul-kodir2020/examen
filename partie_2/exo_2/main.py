import urllib.request
from PipelineData import requestUrl , transform , load , extract_model



data = requestUrl("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


donnees_passager = extract_model(data)


data_cleaned = transform(donnees_passager)
print(data)

load(data_cleaned)

print(donnees_passager)


