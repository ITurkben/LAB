from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import torch

# Chemin vers votre fichier audio
chemin_fichier_audio = r"C:\Users\itu\Documents\Enregistrements audio\enregistrement_segment_1_2024-03-13_08-30-02.wav"

# Charger l'audio avec la bonne fréquence d'échantillonnage (16kHz pour Whisper)
print("Chargement de l'audio avec la bonne fréquence d'échantillonnage (16kHz pour Whisper)")
audio, sampling_rate = librosa.load(chemin_fichier_audio, sr=16_000)

# Initialisation du modèle et du processeur
print("Initialisation du modèle et du processeur")
processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")

# Préparation de l'invite de décodage pour la transcription en français
print("Préparation de l'invite de décodage pour la transcription en français")
# Cette fonction pourrait ne pas nécessiter de retour en tensors directement, donc vérifiez la documentation pour l'utilisation correcte.
forced_decoder_prompt = processor.get_decoder_prompt_ids(language="fr", task="transcribe")

# Traitement de l'audio pour le modèle
print("Traitement de l'audio pour le modèle")
inputs = processor(audio, sampling_rate=sampling_rate, return_tensors="pt")

# Afficher les inputs pour déboguer
print(inputs)

# Génération des ID de tokens pour la transcription
print("Génération des ID de tokens pour la transcription")
# La clé exacte à utiliser dépend de la sortie de votre processeur
predicted_ids = model.generate(inputs["input_features"], forced_bos_token_id=forced_decoder_prompt[0])

# Décodage des ID de tokens pour obtenir le texte
print("Décodage des ID de tokens pour obtenir le texte")
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

print(transcription)


""" résultat : PS C:\Users\itu> python C:\Users\itu\Documents\LAB\AI\Speech_text\test5.py
Chargement de l'audio avec la bonne fréquence d'échantillonnage (16kHz pour Whisper)
Initialisation du modèle et du processeur
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
Préparation de l'invite de décodage pour la transcription en français
Traitement de l'audio pour le modèle
{'input_features': tensor([[[ 0.5351,  0.5315,  0.5424,  ...,  0.5474,  0.5395,  0.5372],
         [ 0.2653,  0.2647,  0.2687,  ...,  0.2742,  0.2658,  0.2652],
         [-0.1318, -0.0682, -0.2495,  ..., -0.1866, -0.1643, -0.1460],
         ...,
         [-0.6062, -0.7257, -0.7651,  ..., -0.7308, -0.7830, -0.6981],
         [-0.5561, -0.8015, -0.7868,  ..., -0.8067, -0.8530, -0.7566],
         [-0.5793, -0.9072, -0.8366,  ..., -0.9352, -0.9800, -0.9425]]])}
Génération des ID de tokens pour la transcription
Due to a bug fix in https://github.com/huggingface/transformers/pull/28687 transcription using a multilingual Whisper will default to language detection followed by transcription instead of translation to English.This might be a breaking change for your use case. If you want to instead always translate your audio to English, make sure to pass `language='en'`.
Décodage des ID de tokens pour obtenir le texte
[" C'est un gars ? Non, pas un gars. C'est un gars."]"""

# Conclusion le modèle est fait pour transcrire des petits segments, une solution est apporté dans le test6.py (pas complet)