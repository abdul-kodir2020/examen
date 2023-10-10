import pandas as pd
import urllib.request

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = urllib.request.urlopen(url)

titanic_data = pd.read_csv(data)

print(titanic_data)

# 1.  Combien de femme de moins de 18 ont survécu
mask_female =  titanic_data['Sex'] =='female'
mask_under_18 = titanic_data['Age'] < 18
mask_survived = titanic_data['Survived'] == 1

female_under_18_survived = titanic_data[mask_female & mask_under_18 & mask_survived]
female_under_18_survived_number = len(female_under_18_survived)

print(f"{female_under_18_survived_number} femmes de moins de 18 ans ont survécues.")



#2. Parmi ces femmes (question 1) déterminer la répartition par classe sur le bateau.
female_under_18_survived_repartition_class = female_under_18_survived.groupby('Pclass').size()

print(female_under_18_survived_repartition_class)

#3. Déterminer si le port d’embarquemen a une influence sur la survie (calculer la répartition des morts et des survivants en fonction du port de départ)


port_repartition_dead_and_survived = pd.pivot_table(titanic_data, values='Survived', index='Embarked', aggfunc=['count', 'sum'])
port_repartition_dead_and_survived.columns = ["Number of passengers", 'Number of survivors']

# Calculer le nombre de décès en soustrayant le nombre de survivants du nombre total de passagers
port_repartition_dead_and_survived['Number of deaths'] = port_repartition_dead_and_survived['Number of passengers'] - port_repartition_dead_and_survived['Number of survivors']

# Afficher la répartition des morts et des survivants en fonction du port de départ
print("Répartition des morts et des survivants en fonction du port de départ :")
print(port_repartition_dead_and_survived)



#4. Déterminer la répartition par sexe et par âge des passagers du navire

repartition_par_sexe_age = titanic_data.groupby(['Sex', pd.cut(titanic_data['Age'], bins=[0, 18, 30, 50, 100])]).size().unstack(fill_value=0)

# Renommer les colonnes pour une meilleure lisibilité
repartition_par_sexe_age.columns = ['Moins de 18 ans', '18-29 ans', '30-49 ans', '50 ans et plus']

# Afficher la répartition par sexe et par âge des passagers
print("Répartition par sexe et par âge des passagers du navire :")
print(repartition_par_sexe_age)