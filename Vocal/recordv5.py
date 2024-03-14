import time
from datetime import datetime, timedelta
import sounddevice as sd
import os
import tempfile
from pydub import AudioSegment
import soundfile as sf
import threading
import logging

# Configuration du logging
log_folder_path = r"C:\Users\itu\Documents\Enregistrements audio\log"
if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path)
log_file_path = os.path.join(log_folder_path, 'audio_recording_log.txt')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def record_audio_to_file(file_path, duration, fs=44100, channels=2):
    def callback(indata, frames, time, status):
        if status:
            logging.warning(status)
        file.write(indata)
    
    try:
        with sf.SoundFile(file_path, mode='x', samplerate=fs, channels=channels) as file:
            with sd.InputStream(samplerate=fs, channels=channels, callback=callback):
                logging.info("Début de l'enregistrement")
                sd.sleep(duration * 1000)
                logging.info("Enregistrement terminé")
    except Exception as e:
        logging.error(f"Erreur lors de l'enregistrement : {e}")

def save_mp3(input_file_path, output_file_path):
    try:
        audio = AudioSegment.from_wav(input_file_path)
        audio.export(output_file_path, format="mp3")
        os.remove(input_file_path)
        logging.info(f"Conversion en MP3 réussie pour {output_file_path}")
    except Exception as e:
        logging.error(f"Erreur lors de la conversion en MP3 : {e}")

def record_and_save(fs=44100, duration_per_recording=7200, total_duration=36000):
    end_time = datetime.now() + timedelta(seconds=total_duration)

    while datetime.now() < end_time:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        temp_file_path = tempfile.mktemp(suffix='.wav')
        output_file_path = f"./{now}.mp3"
        
        record_audio_to_file(temp_file_path, duration_per_recording, fs)
        
        thread = threading.Thread(target=save_mp3, args=(temp_file_path, output_file_path))
        thread.start()
        thread.join()
        
        if datetime.now() + timedelta(seconds=duration_per_recording) < end_time:
            time_remaining = (datetime.now() + timedelta(seconds=duration_per_recording) - datetime.now()).total_seconds()
            time.sleep(max(0, time_remaining))

if __name__ == "__main__":
    logging.info("Démarrage du script d'enregistrement audio")
    record_and_save()
    logging.info("Script d'enregistrement audio terminé")
