import shutil
import os
import glob

# Les répertoires à copier
directories = [
    "\\\\srvfiler\\commun$\\Logistique\\Logistique\\Informatique\\KeePass",
    "\\\\srvfiler\\commun$\\Logistique\\Logistique\\Informatique\\Procédures",
    "\\\\srvfiler\\commun$\\Logistique\\Logistique\\Informatique\\Supports\\Réseaux",
    "\\\\srvfiler\\commun$\\Logistique\\Logistique\\Informatique\\Supports\\Serveurs",
    "\\\\srvfiler\\donnees$\\gpao\\Data_conditionnement"
]

# Les dossiers où chercher les fichiers .btw
btw_directories = [
    "\\\\srvfiler\\donnees$\\gpao"
]

# Chemin de destination
destination_path = "H:\\Sauvegarde" 

# Copie des répertoires
for directory in directories:
    try:
        destination = os.path.join(destination_path, os.path.basename(directory))
        shutil.copytree(directory, destination)
        print(f"Dossier copié: {directory} -> {destination}")
    except Exception as e:
        print(f"Erreur lors de la copie du dossier {directory}: {e}")

# Recherche et copie des fichiers .btw
for directory in btw_directories:
    for file in glob.glob(os.path.join(directory, "*.btw")):
        try:
            shutil.copy(file, destination_path)
            print(f"Fichier .btw copié: {file}")
        except Exception as e:
            print(f"Erreur lors de la copie du fichier {file}: {e}")
