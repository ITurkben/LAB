import sounddevice as sd
from datetime import datetime
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
    duration = 7200  # Durée de l'enregistrement en secondes
    fs = 44100  # Fréquence d'échantillonnage
    
    # Chemin de sortie et nom de fichier basé sur la date et l'heure actuelles
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    temp_file_path = tempfile.mktemp(suffix='.wav')
    output_file_path = f"C:\\Users\\itu\\Documents\\Enregistrements audio\\{now}.mp3"
    
    # Enregistre l'audio directement dans un fichier temporaire
    record_audio_to_file(temp_file_path, duration, fs)
    
    # Convertit le fichier temporaire en MP3 et le sauvegarde
    save_mp3(temp_file_path, output_file_path)
