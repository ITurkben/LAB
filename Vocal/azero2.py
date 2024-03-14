import sounddevice as sd
from pydub import AudioSegment
from datetime import datetime
import numpy as np
import os

# Chemin du dossier où les fichiers MP3 seront sauvegardés
dossier_cible = "C:\\Users\\itu\\Documents\\Enregistrements audio"

def record_segment(duration, fs, segment_number):
    print(f"Enregistrement du segment {segment_number}...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    return myrecording

def save_segment_as_mp3(segment, fs, segment_number, gain_db):
    """
    Sauvegarde un segment audio en format MP3 après l'avoir converti et augmenté le volume.
    
    Args:
    - segment: Le segment audio à sauvegarder.
    - fs: La fréquence d'échantillonnage de l'audio.
    - segment_number: Le numéro du segment actuel, utilisé pour le nom de fichier.
    - gain_db: Le gain en décibels à appliquer pour augmenter le volume. Par défaut à 10 dB.
    """
    if not os.path.exists(dossier_cible):
        os.makedirs(dossier_cible)  # Crée le dossier s'il n'existe pas
    filename = f"segment_{segment_number}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp3"
    filepath = os.path.join(dossier_cible, filename)
    print(f"Conversion et sauvegarde du segment {segment_number} en MP3: {filepath}")
    audio_segment = AudioSegment(segment.tobytes(), frame_rate=fs, sample_width=segment.dtype.itemsize, channels=2)
    
    # Augmente le volume de l'audio
    audio_segment = audio_segment.apply_gain(gain_db)
    
    audio_segment.export(filepath, format="mp3")


def main():
    total_duration_hours = 1  # Durée totale de l'enregistrement en heures
    segment_duration_minutes = 20  # Durée de chaque segment en minutes
    fs = 44100  # Fréquence d'échantillonnage
    gain_db = 20

    total_segments = (total_duration_hours * 60) // segment_duration_minutes

    for segment_number in range(1, total_segments + 1):
        segment = record_segment(segment_duration_minutes * 60, fs, segment_number)
        save_segment_as_mp3(segment, fs, segment_number, gain_db)

if __name__ == "__main__":
    main()
