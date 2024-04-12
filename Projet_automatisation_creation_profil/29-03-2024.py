from ldap3 import Server, Connection, ALL, NTLM

# Paramètres de connexion
server_address = 'xxx.groupe-lepine.com'
domain = 'groupe-lepine'
username = 'administrateur'  # Assurez-vous que c'est le bon nom d'utilisateur pour l'authentification NTLM
password = 'uo'  # Envisagez d'utiliser une méthode sécurisée pour gérer ce mot de passe
user_dn = f"{domain}\\{username}"  # Format requis par NTLM

# Informations de l'utilisateur à créer
new_user_dn = 'CN=Robert Baratheon,OU=Achats,OU=Genay,OU=LEPINE,DC=groupe-lepine,DC=com'
new_user_password = 'SaturneDemi1846!'  # Assurez-vous que cela respecte la politique de sécurité de votre AD
new_user_attributes = {
    'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
    'cn': 'Robert Baratheon',
    'sn': 'Baratheon',
    'givenName': 'Robert',
    'displayName': 'Robert Baratheon',
    'userPrincipalName': 'rob@groupe-lepine.com',  # Assurez-vous que le UPN est unique
    'mail': 'r.baratheon@groupe-lepine.com',
    'userAccountControl': 512,  # Compte activé
}

# Connexion au serveur AD
server = Server(server_address, get_info=ALL)
conn = Connection(server, user=user_dn, password=password, authentication=NTLM)

if conn.bind():
    print("Connexion et liaison réussies.")
    
    # Création de l'utilisateur
    if conn.add(new_user_dn, attributes=new_user_attributes):
        print("Utilisateur créé avec succès.")
        
        # Définir le mot de passe de l'utilisateur
        if conn.extend.microsoft.modify_password(new_user_dn, new_password=new_user_password):
            print("Mot de passe de l'utilisateur défini avec succès.")
        else:
            print("Échec de la définition du mot de passe de l'utilisateur.")
    else:
        print("Erreur lors de la création de l'utilisateur:", conn.result)

    # Déconnexion
    conn.unbind()
else:
    print("Échec de la connexion. Vérifiez les détails de connexion.")


# From scratch again