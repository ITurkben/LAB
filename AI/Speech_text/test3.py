from faster_whisper import WhisperModel

model = WhisperModel("large-v2")

segments, info = model.transcribe("audio.mp3")
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

#DOC : https://huggingface.co/guillaumekln/faster-whisper-large-v2/blob/main/README.md
#Après tests, fonctionne très bien, peux transcrire en temps réel et de bonne qualité, mais trop gourmand, utilise plus de 90% de 8 go ram, pour transcrire simplement avec le code au dessus,
    
"""$ py test3.py 
[2024-03-06 10:42:30.754] [ctranslate2] [thread 9584] [warning] The compute type inferred from the saved model is float16, but the target device or backend do not support efficient float16 computation. The model 
weights have been automatically converted to use the float32 compute type instead.
[90.00s -> 100.00s]  Oui bonjour, Ibrahim du service pharmatique de l'associé des groupes épines, je vous appelle parce qu'on a rencontré un petit souci au niveau d'une douchette, d'une nouveau douchette symbole.[105.00s -> 108.00s]  Ok, merci.
[120.00s -> 130.00s]  Ok, c'est ça, groupe épines, tout simplement.
[130.00s -> 137.00s]  Celui avec lequel j'appelle, le 04-26-96-05.
[137.00s -> 142.00s]  Moi c'est M.Turkben, T-U-R-K-B-E-N.
[142.00s -> 154.00s]  Nickel, par contre, vous routez la demande au service après-vente, c'est ça ?
[154.00s -> 160.00s]  Parce qu'il s'agit d'un problème technique au niveau de la douchette, vous n'avez pas un...
[160.00s -> 163.00s]  Ok, ça marche.
[163.00s -> 167.00s]  Merci beaucoup, idéalement, au revoir."""