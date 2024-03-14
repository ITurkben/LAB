from ldap3 import Server, Connection, ALL
import getpass
import pandas as pd
import random

server_address = 'DCSRV.groupe-lepine.com'
port = 3268  
domain_name = 'groupe-lepine.com'
username = input("Saisir votre nom d'utilisateur : ")
password = getpass.getpass("Saisir le mot de passe : ")
full_username = f'{username}@{domain_name}'  

input_file_path = "C:/Users/itu/Documents/LAB/Projet_automatisation_creation_profil/profil/modele.xlsx"
output_file_path = "C:/Users/itu/Documents/LAB/Projet_automatisation_creation_profil/profil/output.xlsx"

users = pd.read_excel(input_file_path)

def generate_trigram(first_name, last_name, mode):
    if mode == 1:
        return (first_name[0] + last_name[:2]).lower()
    elif mode == 2:
        return (first_name[:2] + last_name[0]).lower()
    elif mode == 3:
        return last_name[:3].lower()
    elif mode == 4:
        return first_name[:3].lower()


class GenerateurMotDePasse:
    def __init__(self):
        self.MAJ = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
        self.normale = 'azertyuiopqsdfghjklmwxcvbn'
        self.special = ',;:!*ù$^.?§/µ%£¨=)+°àç_è-("é&²)'
        self.chiffre = '123456789'

    def generer_mot_de_passe(self):
        mot_de_passe = random.choice(self.MAJ)
        for i in range(9):
            mot_de_passe += random.choice(self.normale)
        mot_de_passe += random.choice(self.chiffre)
        mot_de_passe += random.choice(self.special)
        return mot_de_passe


def check_tri(server_address, port, full_username, password, account_name):
    """
    Vérifie si un sAMAccountName spécifique existe dans la base de données LDAP.

    :param server_address: Adresse du serveur LDAP.
    :param port: Port du serveur LDAP.
    :param full_username: Nom d'utilisateur complet pour se connecter au serveur LDAP.
    :param password: Mot de passe pour se connecter au serveur LDAP.
    :param account_name: Le sAMAccountName à rechercher.
    :return: True si le compte existe, False sinon.
    """
    # Configuration du serveur LDAP
    server = Server(server_address, port=port, get_info=ALL, use_ssl=False)

    # Configuration de la connexion
    conn = Connection(server, user=full_username, password=password)

    # Tentative de connexion au serveur LDAP
    if not conn.bind():
        print('Erreur de connexion !')
        print(conn.result)
        return False

    # La base de recherche est fixée ici
    search_base = 'dc=groupe-lepine,dc=com'

    # Recherche du sAMAccountName spécifique
    search_filter = f'(sAMAccountName={account_name})'
    conn.search(search_base, search_filter, attributes=['sAMAccountName'])

    # Vérification si le compte existe
    user_exists = bool(conn.entries)

    # Fermeture de la connexion
    conn.unbind()

    return user_exists

prenom = users.iloc[1, 1]
nom = users.iloc[2, 1]

for mode in range(1, 5):
    trigramme = generate_trigram(prenom, nom, mode)
    if not check_tri(server_address, port, full_username, password, trigramme):
        break

generateur = GenerateurMotDePasse()
mot_de_passe_generé = generateur.generer_mot_de_passe()
email = prenom[0].lower()+'.'+nom.lower()+"@groupe-lepine.com"


print(trigramme)
print(mot_de_passe_generé)
print(email)