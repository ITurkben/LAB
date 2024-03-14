import pyautogui
import time
import pyperclip

def ouvrir_la_console(chemin):
    # Copie le chemin dans le presse-papiers
 
    pyperclip.copy(chemin)
    
    time.sleep(1)
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    
    # Colle le chemin depuis le presse-papiers
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    
    pyautogui.press('enter')

def login1(ID, Mdp):
    time.sleep(4)
    pyperclip.copy(ID)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')
    pyperclip.copy(Mdp)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

def login2(ID, Mdp):
    time.sleep(4)
    pyautogui.write('QSECOFR')
    pyautogui.press('tab')
    pyautogui.write('RFOCESQ')
    pyautogui.press('enter')

def commande_wrkactjob():
    time.sleep(1)
    pyautogui.write('wrkactjob')
    pyautogui.press('enter')

def main():
    chemin = 'C:\\Users\\itu\\AppData\\Roaming\\IBM\\Client Access\\Emulator\\private\\as400.ws'
    ID = 'QSECOFR'
    Mdp = 'RFOCESQ'
    ouvrir_la_console(chemin)
    login1(ID, Mdp)
    login2(ID, Mdp)
    commande_wrkactjob()

if __name__ == '__main__':
    main()