from openai import OpenAI

# Initialisation du client OpenAI avec votre clé d'API
client = OpenAI()

# Ouverture du fichier audio pour lecture
audio_file = open("speech.mp3", "rb")

# Création de la transcription
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  language="fr",
)

# Fermeture du fichier audio après lecture
audio_file.close()

# Affichage de la transcription dans la console
print(transcript)

# Sauvegarde de la transcription dans un fichier texte
with open("transcription.txt", "w") as text_file:
    text_file.write(str(transcript))
