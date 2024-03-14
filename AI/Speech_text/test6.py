import librosa

# Charger l'audio
audio, sampling_rate = librosa.load(r"C:\Users\itu\Documents\Enregistrements audio\enregistrement_segment_1_2024-03-13_08-30-02.wav", sr=16000)

# (Optionnel) Découper l'audio en segments basés sur le silence ou en segments de durée fixe
# Exemple simple de découpage en segments de durée fixe (exemple : 30 secondes)
segment_length = 30 * sampling_rate  # 30 secondes en échantillons
segments = [audio[i:i+segment_length] for i in range(0, len(audio), segment_length)]

transcriptions = []
for segment in segments:
    # Traiter chaque segment avec le processeur et le modèle
    inputs = processor(segment, sampling_rate=sampling_rate, return_tensors="pt")
    predicted_ids = model.generate(inputs["input_features"], forced_bos_token_id=forced_decoder_prompt[0])
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    transcriptions.append(transcription[0])

# Combinez toutes les transcriptions
full_transcription = " ".join(transcriptions)
print(full_transcription)
