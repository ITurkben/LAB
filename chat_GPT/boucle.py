import subprocess

# Définir le nom du serveur et le message
nom_de_la_machine = "Gl-poste64"  # Remplacez par le nom réel du serveur
message = "On mange ou ?"
ajout = "On mange ou ?"

# Exécuter la commande
for i in range(30):
    commande = f'msg /server:"{nom_de_la_machine}" * "{message}"'
    subprocess.run(commande, shell=True)
    message += ajout
