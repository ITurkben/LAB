import time
from datetime import datetime, timedelta
import sounddevice as sd
import os
import tempfile
from pydub import AudioSegment
import soundfile as sf
import threading

def record_audio_to_file(file_path, duration, fs=44100, channels=2):
    def callback(indata, frames, time, status):
        if status:
            print(status)
        file.write(indata)
    
    try:
        with sf.SoundFile(file_path, mode='x', samplerate=fs, channels=channels) as file:
            with sd.InputStream(samplerate=fs, channels=channels, callback=callback):
                print("Début de l'enregistrement")
                sd.sleep(duration * 1000)
                print("Enregistrement terminé")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement : {e}")

def save_mp3(input_file_path, output_file_path):
    try:
        audio = AudioSegment.from_wav(input_file_path)
        audio.export(output_file_path, format="mp3")
        os.remove(input_file_path)
    except Exception as e:
        print(f"Erreur lors de la conversion en MP3 : {e}")

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
    record_and_save()
