import random

MAJ = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
normale = 'azertyuiopqsdfghjklmwxcvbn'
special = ',;:!*ù$^.?§/µ%£¨=)+°àç_è-("é&²)'
chiffre = '123456789'
mot_de_passe = ''


def on_boucle():
    global mot_de_passe
    mot_de_passe += random.choice(MAJ)
    for i in range(9):
        mot_de_passe += random.choice(normale)
    mot_de_passe += random.choice(chiffre)
    mot_de_passe += random.choice(special)


on_boucle()
print(mot_de_passe)