import random

class GenerateurMotDePasse:
    def __init__(self):
        self.MAJ = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
        self.normale = 'azertyuiopqsdfghjklmwxcvbn'
        self.special = ',;:!*ù$^.?§/µ%£¨=)+°àç_è-("é&²)'
        self.chiffre = '123456789'

    def generer_mot_de_passe(self):
        mot_de_passe = random.choice(self.MAJ)
        for i in range(9):
            mot_de_passe += random.choice(self.normale)
        mot_de_passe += random.choice(self.chiffre)
        mot_de_passe += random.choice(self.special)
        return mot_de_passe

generateur = GenerateurMotDePasse()
mot_de_passe = generateur.generer_mot_de_passe()
print(mot_de_passe)
