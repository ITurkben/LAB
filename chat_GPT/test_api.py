import os
import openai

# Récupérer la clé API depuis les variables d'environnement
api_key = os.getenv('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("La clé API OpenAI n'est pas définie dans les variables d'environnement.")

# Configuration du client OpenAI avec votre clé API
openai.api_key = api_key

# Faire une requête pour compléter le texte
response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt="Quelle est la capitale de la France?",
    max_tokens=5
)

print(response.choices[0].text.strip())
