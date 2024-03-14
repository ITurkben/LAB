import sounddevice as sd
from pydub import AudioSegment
import os

# Paramètres d'enregistrement
fréquence_déchantillonnage = 44100  # Fréquence d'échantillonnage
#durée = 8 * 60 * 60  # 8 heures converties en secondes
durée = 10
nom_du_fichier = "enregistrement.mp3"  # Nom du fichier à sauvegarder
chemin_complet = os.path.join("C:\\Users\\itu\\Documents\\Enregistrements audio", nom_du_fichier)

print("Début de l'enregistrement")
enregistrement = sd.rec(int(durée * fréquence_déchantillonnage), samplerate=fréquence_déchantillonnage, channels=2, dtype='int16')
sd.wait()  # Attendre la fin de l'enregistrement
print("Enregistrement terminé, sauvegarde du fichier...")

# Conversion de l'array NumPy en audio segment
audio_segment = AudioSegment(
    data=enregistrement.tobytes(),
    sample_width=enregistrement.dtype.itemsize,
    frame_rate=fréquence_déchantillonnage,
    channels=2
)

# Sauvegarde de l'enregistrement audio au format MP3
audio_segment.export(chemin_complet, format="mp3")
print(f"Fichier sauvegardé sous : {chemin_complet}")
