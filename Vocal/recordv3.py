import time
from datetime import datetime, timedelta
import sounddevice as sd
import os
import tempfile
from pydub import AudioSegment
import soundfile as sf

def record_audio_to_file(file_path, duration, fs):
    """
    Enregistre l'audio du microphone par défaut dans un fichier sur le disque pour une durée spécifiée.
    Cette fonction écrit l'audio en continu dans un fichier temporaire pour soulager la mémoire vive.
    Args:
        file_path (str): Chemin du fichier WAV temporaire où l'audio est stocké pendant l'enregistrement.
        duration (int): Durée de l'enregistrement en secondes. 10 par défaut.
        fs (int): Fréquence d'échantillonnage de l'enregistrement. 44100 Hz par défaut.
    """
    # Définit une fonction de callback pour écrire les blocs audio dans un fichier au fur et à mesure
    def callback(indata, frames, time, status):
        if status:
            print(status)
        file.write(indata)  # Utilisez file.write pour écrire les données audio
    
    # Ouvre un fichier temporaire pour écrire l'audio
    with sf.SoundFile(file_path, mode='x', samplerate=fs, channels=2) as file:
        with sd.InputStream(samplerate=fs, channels=2, callback=callback):
            print("Début de l'enregistrement")
            sd.sleep(duration * 1000)  # Attend la fin de l'enregistrement en utilisant sleep
            print("Enregistrement terminé")

def save_mp3(input_file_path, output_file_path):
    """
    Convertit le fichier audio temporaire en MP3.
    Args:
        input_file_path (str): Chemin du fichier WAV temporaire.
        output_file_path (str): Chemin du fichier de sortie MP3.
    """
    # Convertit le fichier WAV en MP3 en utilisant pydub
    audio = AudioSegment.from_wav(input_file_path)
    audio.export(output_file_path, format="mp3")
    
    # Supprime le fichier WAV temporaire
    os.remove(input_file_path)


if __name__ == "__main__":
    fs = 44100  # Fréquence d'échantillonnage
    duration_per_recording = 7200  # Durée de l'enregistrement en secondes (2 heures)
    total_duration = 36000  # Durée totale d'enregistrement en secondes (10 heures)

    # Calculez l'heure de fin en ajoutant 10 heures à l'heure de début
    end_time = datetime.now() + timedelta(seconds=total_duration)

    while datetime.now() < end_time:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        temp_file_path = tempfile.mktemp(suffix='.wav')
        output_file_path = f"C:\\Users\\itu\\Documents\\Enregistrements audio\\{now}.mp3"
        
        # Enregistre l'audio directement dans un fichier temporaire
        record_audio_to_file(temp_file_path, duration_per_recording, fs)
        
        # Convertit le fichier temporaire en MP3 et le sauvegarde
        save_mp3(temp_file_path, output_file_path)
        
        # Attendre jusqu'à la prochaine itération qui doit avoir lieu dans deux heures
        # Mais vérifiez aussi si le temps total n'a pas été dépassé avant de dormir
        if datetime.now() + timedelta(hours=2) < end_time:
            time.sleep(7200)  # 7200 secondes correspondent à deux heures


# NON testé 