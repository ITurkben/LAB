import pandas as pd

# Noms des feuilles à lire
feuilles = ["en cours", "2023", "2022", "2021", "2020"]
fichier_source = "Copie de offres de prix ORTHO.xlsx"
fichier_destination = "gh_extraite.xlsx"

# Initialisation d'une liste vide pour collecter les données
donnees_collectees = []

for feuille in feuilles:
    # Lire la feuille actuelle
    df = pd.read_excel(fichier_source, sheet_name=feuille, engine='openpyxl', header=4)
    
    # Filtrer les lignes dont le nom de l'établissement contient "CL", "cl", ou "Cl"
    df_filtre = df[df['Etablissement'].str.contains('GH|gh|Gh|GHT', regex=True)]
    
    # Sélectionner uniquement les données nécessaires (remplacer 'B' et 'I' par les noms exacts des colonnes)
    df_selection = df_filtre[['Etablissement', 'Dpt', 'Coordonnées']]
    
    # Ajouter les données filtrées à la liste
    donnees_collectees.append(df_selection)

# Concaténer toutes les données collectées en un seul DataFrame
donnees_finale = pd.concat(donnees_collectees, ignore_index=True)

# Supprimer les doublons basés sur le nom de l'établissement
donnees_finale = donnees_finale.drop_duplicates(subset=['Etablissement'])

# Écrire le DataFrame résultant dans un nouveau fichier Excel
donnees_finale.to_excel(fichier_destination, index=False, engine='openpyxl')
