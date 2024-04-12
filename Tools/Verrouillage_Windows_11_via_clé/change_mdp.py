import subprocess

def change_user_password(username, new_password):
    command = f"net user {username} {new_password}"
    subprocess.run(command, shell=True, check=True)

try:
    change_user_password("user", "Lac2024!Mars")
    print("Le mot de passe a été changé avec succès.")
except subprocess.CalledProcessError as e:
    print("Une erreur s'est produite lors de la tentative de changement du mot de passe.")
