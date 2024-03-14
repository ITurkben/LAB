import pyautogui

print("Déplace la souris et clique quelque part sur l'écran pour obtenir les coordonnées. Appuie sur Ctrl+C dans la console pour quitter.")

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'Position actuelle de la souris: X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nTerminé.')
