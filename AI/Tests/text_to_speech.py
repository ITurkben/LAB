import requests

# Vos en-têtes de requête
headers = {
    "Authorization": "Bearer ",
    "Content-Type": "application/json"
}

# Le corps de votre requête
body = {
    "model": "tts-1-hd",
    "input": "L'intelligence artificielle, ou IA, est un domaine fascinant et en pleine évolution qui touche presque tous les aspects de notre vie quotidienne. À ses débuts, l'IA était perçue comme une quête pour créer des machines pouvant imiter l'intelligence humaine, mais aujourd'hui, elle englobe bien plus. L'IA nous aide à résoudre des problèmes complexes, à analyser d'immenses quantités de données et à créer de nouvelles façons d'interagir avec le monde. De la reconnaissance vocale utilisée dans les assistants personnels intelligents aux algorithmes qui recommandent ce que nous devrions regarder ou acheter en ligne, l'IA est omniprésente. Elle transforme des secteurs tels que la santé, en aidant les médecins à diagnostiquer les maladies avec une précision inégalée, et le secteur financier, en sécurisant les transactions et en prévenant la fraude. Cependant, l'IA soulève également des questions éthiques importantes.",
    "voice": "shimmer"
}

# Envoi de la requête POST
response = requests.post("https://api.openai.com/v1/audio/speech", json=body, headers=headers)

# Vérifiez si la requête a réussi
if response.status_code == 200:
    # Sauvegarde de la réponse (flux audio) dans un fichier
    with open("speech.mp3", "wb") as file:
        file.write(response.content)
    print("Le fichier audio a été sauvegardé avec succès.")
else:
    print(f"La requête a échoué avec le statut {response.status_code}.")
