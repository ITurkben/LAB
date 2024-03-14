from openai import OpenAI
import subprocess
import os

machine_1 = "Gl-poste97"
machine_2 = "Gl-poste64"
machine_3 = "Gl-poste24"

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Fonction pour envoyer une question à l'API GPT et obtenir une réponse
def send_to_gpt(question):
    response = client.chat.completions.create(messages=[{"role": "user", "content": question}], model="gpt-3.5-turbo")
    return response.choices[0].message.content

# Exemple d'utilisation de la fonction
question = "donne moi une nouvelle anecdote qui s'est passé dans l'histoire de l'informatique, ou alors apprends moi quelque chose de nouveau en lien avec l'informatique en seulement deux lignes. La réponse ne doit absolument pas contenir de caractère spécial."
reponse = send_to_gpt(question)
print(reponse)


commande_1 = f'msg /server:"{machine_1}" * "{reponse}"'
#commande_2 = f'msg /server:"{machine_2}" * "{reponse}"'
#commande_3 = f'msg /server:"{machine_3}" * "{reponse}"'
#subprocess.run(commande_1, shell=True)
#subprocess.run(commande_2, shell=True)
#subprocess.run(commande_3, shell=True)

