from faster_whisper import WhisperModel

model = WhisperModel("medium")

segments, info = model.transcribe("audio.mp3", language="fr")
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

"""itu@GL-POSTE97 MINGW64 ~/Documents/LAB/AI/Speech_text
$ py test4.py 
[2024-03-06 11:43:38.305] [ctranslate2] [thread 2816] [warning] The compute type inferred from the saved model is float16, but the target device or backend do not support efficient float16 computation. The model 
weights have been automatically converted to use the float32 compute type instead.
[0.00s -> 2.00s]  Et voilà, on a fini de la vidéo.
[2.00s -> 4.00s]  Merci d'avoir regardé cette vidéo.
[4.00s -> 6.00s]  J'ai eu un peu de mal à la fin.
[6.00s -> 8.00s]  J'ai eu un peu de mal à la fin.
[8.00s -> 10.00s]  Merci de vous avoir regardé cette vidéo.
[10.00s -> 12.00s]  Merci d'avoir regardé cette vidéo.
[12.00s -> 14.00s]  Merci d'avoir regardé cette vidéo.
[30.00s -> 32.00s]  Merci d'avoir regardé cette vidéo.
[32.00s -> 34.00s]  Merci d'avoir regardé cette vidéo.
[34.00s -> 36.00s]  Merci d'avoir regardé cette vidéo."""

#Pas conforme 