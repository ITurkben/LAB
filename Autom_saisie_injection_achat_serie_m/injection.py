import pyautogui
import time

def ouvrir_et_gestion_serieM():
    # Double clic pour ouvrir SerieM
    pyautogui.doubleClick(120, 120)  # Remplace x, y par les coordonnées du raccourci SerieM
    time.sleep(2)  # Attends que l'application se lance

    # Se connecter avec les id tca/tca
    pyautogui.write('tca')
    pyautogui.press('tab')  # passe au champ du mot de passe
    pyautogui.write('tca')
    pyautogui.press('enter')
    time.sleep(2)

    # Cliquer sur "OK"
    pyautogui.click(x_ok, y_ok)  # Remplace x_ok, y_ok par les coordonnées du bouton OK

    # Cliquer sur "Série M / Gestion"
    pyautogui.click(x_gestion, y_gestion)  # Remplace par les coordonnées du bouton

    # Cliquer sur "GESTION DES ACHATS"
    pyautogui.click(x_achats, y_achats)  # Coordonnées du bouton "GESTION DES ACHATS"

    # Cliquer sur "Divers"
    pyautogui.click(x_divers, y_divers)  # Coordonnées du bouton "Divers"

    # Cliquer sur "Injection Bons d'Achats via EXCEL"
    pyautogui.click(x_injection, y_injection)  # Coordonnées du bouton

    # Saisir "tca"
    pyautogui.write('tca')
    pyautogui.press('enter')
    time.sleep(2)

    # Cliquer sur "OK"
    pyautogui.click(x_ok2, y_ok2)  # Coordonnées du deuxième bouton OK

    # Cliquer sur "Oui"
    pyautogui.click(x_oui, y_oui)  # Coordonnées du bouton "Oui"

# Répète l'opération 60 fois
for i in range(60):
    ouvrir_et_gestion_serieM()
    time.sleep(60)  # Attend 1 minute avant de recommencer
