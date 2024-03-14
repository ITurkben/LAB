import os

chemin_du_repertoire = 'C:\\Utilisateurs\\itu'  # Remplacez par le chemin de votre répertoire

nombre_de_fichiers = 0
nombre_de_dossiers = 0

for racine, dossiers, fichiers in os.walk(chemin_du_repertoire):
    for dossier in dossiers:
        nombre_de_dossiers += 1
    for fichier in fichiers:
        nombre_de_fichiers += 1

print(f"Nombre de dossiers : {nombre_de_dossiers}")
print(f"Nombre de fichiers : {nombre_de_fichiers}")
