import subprocess

# Spécifiez les détails de votre connexion ici
lecteur = 'Z:'  # Lettre du lecteur à monter
chemin_partage = r'\\srvinf\logiciels$'
nom_utilisateur = 'ituadg'
mot_de_passe = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Construit la commande pour connecter le lecteur réseau
commande = f'net use {lecteur} {chemin_partage} /user:{nom_utilisateur} {mot_de_passe} /persistent:no'

# Exécute la commande
resultat = subprocess.run(commande, shell=True, capture_output=True, text=True)

# Vérifie si la commande a réussi
if resultat.returncode == 0:
    print(f'Lecteur {lecteur} connecté avec succès à {chemin_partage}.')
else:
    print(f'Échec de la connexion du lecteur {lecteur} à {chemin_partage}.\nErreur : {resultat.stderr}')

# Pour déconnecter le lecteur plus tard, vous pouvez utiliser :
# commande_deconnexion = f'net use {lecteur} /delete'
# subprocess.run(commande_deconnexion, shell=True)
