# Ce script permet de faire une requete NSLOOKUP en boucle en incrémentant de 1 à chaque itération le nom DNS de la requete en l'occurence
# nslookup port001  nslookup port002    nslookup port003    etc...


import os

# Base du nom d'hôte
base_hostname = "porta"

# Boucle pour générer les noms d'hôte de porta001 à porta010
for i in range(1, 30):  # Commence à 1 et s'arrête à 10 inclus
    # Génère le numéro avec le formatage nécessaire pour garder les zéros initiaux
    number_str = f"{i:03}"
    # Construit le nom d'hôte complet
    hostname = f"{base_hostname}{number_str}"
    
    # Exécute la requête nslookup
    response = os.system(f"nslookup {hostname}")
    
    # Vérifie la réponse
    if response == 0:
        print(f"{hostname} is up!")
    else:
        print(f"{hostname} is down!")
