from ldap3 import Server, Connection, ALL
import getpass
import pandas as pd
import random

class GenerateurMotDePasse:
    def __init__(self):
        self.MAJ = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
        self.normale = 'azertyuiopqsdfghjklmwxcvbn'
        self.special = ',;:!*ù$^.?§/µ%£¨=)+°àç_è-("é&²)'
        self.chiffre = '123456789'

    def generer(self):
        mot_de_passe = random.choice(self.MAJ)
        for i in range(9):
            mot_de_passe += random.choice(self.normale)
        mot_de_passe += random.choice(self.chiffre)
        mot_de_passe += random.choice(self.special)
        return mot_de_passe

def generer_trigram(first_name, last_name, mode):
    if mode == 1:
        return (first_name[0] + last_name[:2]).lower()
    elif mode == 2:
        return (first_name[:2] + last_name[0]).lower()
    elif mode == 3:
        return last_name[:3].lower()
    elif mode == 4:
        return first_name[:3].lower()

def check_tri(conn, account_name):
    try:
        search_base = 'dc=groupe-lepine,dc=com'
        search_filter = f'(sAMAccountName={account_name})'
        conn.search(search_base, search_filter, attributes=['sAMAccountName'])
        return bool(conn.entries)
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False

def creer_utilisateur_AD(conn, prenom, nom, trigramme, mot_de_passe, service, adresse, code_postal, email):
    try:
        user_dn = f"cn={prenom} {nom},ou={service},ou=Genay,ou=LEPINE,dc=groupe-lepine,dc=com"
        attributes = {
            'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
            'cn': f"{prenom} {nom}",
            'givenName': prenom,
            'sn': nom,
            'sAMAccountName': trigramme,
            'userPrincipalName': f"{trigramme}@groupe-lepine.com",
            'streetAddress': adresse,
            'postalCode': code_postal,
            'mail': email
        }
        conn.add(user_dn, attributes=attributes)
        conn.extend.microsoft.modify_password(user_dn, mot_de_passe)
        conn.modify(user_dn, {'userAccountControl': [('MODIFY_REPLACE', 512)]})
        return conn.result
    except Exception as e:
        print(f"Une erreur s'est produite lors de la création de l'utilisateur : {e}")
        return None

def main():
    server_address = 'DCSRV.groupe-lepine.com'
    port = 3268
    domain_name = 'groupe-lepine.com'
    username = input("Saisir votre nom d'utilisateur : ")
    password = getpass.getpass("Saisir le mot de passe : ")
    full_username = f'{username}@{domain_name}'

    # Connexion LDAP
    server = Server(server_address, port=port, get_info=ALL, use_ssl=False)
    conn = Connection(server, user=full_username, password=password)
    if not conn.bind():
        print('Erreur de connexion LDAP.')
        return

    # Lecture du fichier Excel
    input_file_path = "C:/Users/itu/Documents/LAB/Projet_automatisation_creation_profil/profil/modele.xlsx"
    users = pd.read_excel(input_file_path)

    # Extraction des informations des utilisateurs
    prenom = users.iloc[1, 1]
    nom = users.iloc[2, 1]
    fonction = users.iloc[3, 1]
    service = users.iloc[4, 1]
    gestionnaire = users.iloc[5, 1]
    adresse = users.iloc[6, 1]
    code_postal = users.iloc[7, 1]

    # Génération du trigramme et vérification de son unicité
    for mode in range(1, 5):
        trigramme = generer_trigram(prenom, nom, mode)
        if not check_tri(conn, trigramme):
            break

    # Génération du mot de passe
    generateur = GenerateurMotDePasse()
    mot_de_passe_genere = generateur.generer()
    email = prenom[0].lower() + '.' + nom.lower() + "@groupe-lepine.com"

    #Création de l'utilisateur
    print("En cours de création du profil")
    creer_utilisateur_AD(conn, prenom, nom, trigramme, mot_de_passe_genere, service, adresse, code_postal, email)
    print(f"Trigramme: {trigramme}, Mot de passe: {mot_de_passe_genere}, Email: {email}, Fonction: {fonction}, Service: {service}, Gestionnaire: {gestionnaire}, Adresse: {adresse}, Code postal: {code_postal}")

if __name__ == "__main__":
    main()