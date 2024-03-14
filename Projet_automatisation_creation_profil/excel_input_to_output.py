import pandas as pd
import random
import string

# Chemins des fichiers
input_file_path = "C:/Users/itu/Documents/LAB/Projet_automatisation_creation_profil/test.xlsx"
output_file_path = "C:/Users/itu/Documents/LAB/Projet_automatisation_creation_profil/output.xlsx"

# Lire les données depuis le fichier Excel
users = pd.read_excel(input_file_path)

# Fonction pour générer le trigramme
def generate_trigram(first_name, last_name):
    trigram = first_name[0] + last_name[:2]
    return trigram.lower()

# Fonction pour générer un mot de passe
def generate_password(length=12, num_special_chars=2):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length - num_special_chars))
    password += ''.join(random.choice(string.punctuation) for i in range(num_special_chars))
    return password

# Ajouter les nouvelles informations
for index, row in users.iterrows():
    users.at[index, 'Trigram'] = generate_trigram(row['Prénom'], row['Nom'])
    users.at[index, 'MotDePasse'] = generate_password()
    users.at[index, 'Email'] = f"{row['Prénom'][0].lower()}.{row['Nom'].lower()}@groupe-lepine.com"

# Écrire les données dans un nouveau fichier Excel
users.to_excel(output_file_path, index=False)

print(f"Le fichier a été généré : {output_file_path}")
