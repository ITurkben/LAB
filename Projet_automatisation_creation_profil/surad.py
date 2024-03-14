from pyad import aduser, adcontainer

# Se connecter à l'AD
# Tu dois avoir les droits nécessaires pour effectuer cette action
pyad.set_defaults(ldap_server="nom_du_serveur_AD", username="ton_utilisateur", password="ton_mot_de_passe")

# Spécifier le conteneur où tu veux créer le nouvel utilisateur
# C'est comme une "adresse" dans l'AD où se trouve ton utilisateur
ou = adcontainer.ADContainer.from_dn("ou=MonOU,dc=example,dc=com")

# Créer l'utilisateur
new_user = aduser.ADUser.create("julien.dupont", ou, password="UnSuperMotDePasse")

# Tu peux aussi définir des propriétés supplémentaires
new_user.update_attributes({
  "givenName": "Julien",
  "sn": "Dupont",
  "displayName": "Julien Dupont",
  "mail": "julien.dupont@example.com",
  "userPrincipalName": "julien.dupont@example.com"
})

# Et voilà, l'utilisateur est créé dans l'AD
