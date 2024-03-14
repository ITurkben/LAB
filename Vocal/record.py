import sounddevice as sd
import numpy as np
from datetime import datetime
import os
import tempfile
from pydub import AudioSegment
import soundfile as sf

def record_audio(duration=10, fs=44100):
    """
    Enregistre l'audio du microphone par défaut pour une durée spécifiée.
    Args:
        duration (int): Durée de l'enregistrement en secondes. 10 par défaut.
        fs (int): Fréquence d'échantillonnage de l'enregistrement. 44100 Hz par défaut.
    Returns:
        Numpy array: Enregistrement audio.
    """
    print("Début de l'enregistrement")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float64')
    sd.wait()  # Attend la fin de l'enregistrement
    print("Enregistrement terminé")
    return recording

def save_mp3(data, fs, file_path):
    """
    Sauvegarde l'array numpy en tant que fichier MP3.
    Args:
        data (numpy array): Enregistrement audio.
        fs (int): Fréquence d'échantillonnage.
        file_path (str): Chemin du fichier de sortie.
    """
    # Utilise soundfile pour gérer la conversion de format de manière plus flexible
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmpfile:
        sf.write(tmpfile.name, data, fs)
        tmpfile.close()
        
        # Convertit le fichier WAV en MP3 en utilisant pydub
        audio = AudioSegment.from_wav(tmpfile.name)
        audio.export(file_path, format="mp3")
        
        # Supprime le fichier WAV temporaire
        os.remove(tmpfile.name)

if __name__ == "__main__":
    duration = 7200  # Durée de l'enregistrement en secondes
    fs = 44100  # Fréquence d'échantillonnage
    
    # Chemin de sortie et nom de fichier basé sur la date et l'heure actuelles
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"C:\\Users\\itu\\Documents\\Enregistrements audio\\{now}.mp3"
    
    # Enregistrement et sauvegarde
    recording = record_audio(duration, fs)
    save_mp3(recording, fs, file_path)


#Fonctionne très bien MAIS stock l'enregistrement en RAM, ce qui pose un gros problème pour des enregistrement dépassant 5 minutes