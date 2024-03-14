import sounddevice as sd
import soundfile as sf
import os
from datetime import datetime
from pydub import AudioSegment
import sys

# Paramètres de configuration
dossier_cible = "C:\\Users\\itu\\Documents\\Enregistrements audio"  # Dossier de sauvegarde des enregistrements
fs = 44100  # Fréquence d'échantillonnage
duration = 20 * 60  # Durée de chaque segment en secondes (20 minutes)
gain_db = 20  # Gain en décibels pour augmenter le volume
total_duration_hours = 10  # Durée totale de l'enregistrement en heures
segment_duration_minutes = 20  # Durée de chaque segment en minutes
total_segments = (total_duration_hours * 60) // segment_duration_minutes

def record_direct_to_file(file_path, duration, fs):
    print(f"Enregistrement direct sur le disque : {file_path}")
    # Créer une nouvelle fonction de callback pour écrire les frames dans le fichier
    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        file.write(indata)
    
    # Ouvrir le fichier avec soundfile.SoundFile pour l'écriture
    with sf.SoundFile(file_path, mode='x', samplerate=fs, channels=2, subtype='PCM_16') as file:
        # Créer et démarrer l'InputStream
        with sd.InputStream(samplerate=fs, channels=2, callback=callback):
            sd.sleep(int(duration * 1000))  # Attendre que l'enregistrement soit terminé


def convert_to_mp3_and_adjust_volume(wav_path, gain_db):
    mp3_path = wav_path.replace('.wav', '.mp3')
    print(f"Conversion en MP3 et ajustement du volume : {mp3_path}")
    audio = AudioSegment.from_wav(wav_path)
    audio = audio.apply_gain(gain_db)
    audio.export(mp3_path, format='mp3')
    #os.remove(wav_path)  # Supprime le fichier WAV original après conversion

def main():
    if not os.path.exists(dossier_cible):
        os.makedirs(dossier_cible)

    for segment_number in range(1, total_segments + 1):
        filename = f"enregistrement_segment_{segment_number}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"
        filepath = os.path.join(dossier_cible, filename)
        print(f"Enregistrement du segment {segment_number} sur {total_segments}")
        record_direct_to_file(filepath, duration, fs)
        convert_to_mp3_and_adjust_volume(filepath, gain_db)

if __name__ == "__main__":
    main()
