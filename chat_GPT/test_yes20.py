from openai import OpenAI
import subprocess
import os

# Configuration initiale
machine_1 = "Gl-poste97"
machine_2 = "Gl-poste64"
machine_3 = "Gl-poste24"
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Historique des interactions : liste de dictionnaires avec les rôles 'user' et 'system'
history = []

# Fonction pour envoyer une question à l'API GPT et obtenir une réponse, avec historique
def send_to_gpt(question, history):
    messages = history + [{"role": "user", "content": question}]
    response = client.chat.completions.create(
        messages=messages, 
        model="gpt-3.5-turbo",
        temperature=0.95)
    new_message = {"role": "system", "content": response.choices[0].message.content}
    history.append(new_message)  # Ajouter la réponse récente à l'historique
    return new_message['content']


# Exemple d'utilisation de la fonction avec historique
question = "Partagez avec moi une anecdote fascinante et un fait surprenant lié à l'informatique que je n'ai pas encore entendu. Cela devrait être exprimé en une seule phrase, sans utiliser de caractères spéciaux et différent de tout ce que vous avez mentionné auparavant."
reponse = send_to_gpt(question, history)
print(reponse)

# Envoi de la réponse aux machines
commande_1 = f'msg /server:"{machine_1}" * "{reponse}"'
#commande_2 = f'msg /server:"{machine_2}" * "{reponse}"'
#commande_3 = f'msg /server:"{machine_3}" * "{reponse}"'
subprocess.run(commande_1, shell=True)
#subprocess.run(commande_2, shell=True)
#subprocess.run(commande_3, shell=True)
