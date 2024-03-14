import pyautogui
import time

def gon():

    time.sleep(0.5)
    pyautogui.click(2615, 16)
    time.sleep(0.5)
    pyautogui.click(3132, 248)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.doubleClick(861, 539)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.click(932, 611, button='right')
    time.sleep(0.5)
    pyautogui.click(1276, 94)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.doubleClick(1063, 578)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.click(2615, 16)
    time.sleep(0.5)
    pyautogui.click(3223, 245)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(989, 640)

def yes():
    pyautogui.doubleClick(1267, 845)
    pyautogui.press('c')
    pyautogui.press('o')
    pyautogui.press('r')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.click(615, 798)
    time.sleep(0.5)
    pyautogui.doubleClick(1126, 488)
    pyautogui.hotkey('ctrl', 'c')

def toi():
    time.sleep(0.5)
    pyautogui.click(617, 769)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')

def beforelast():
    time.sleep(0.5)
    pyautogui.click(617, 803)
    time.sleep(0.5)
    pyautogui.click(2835, 12)
    time.sleep(0.5)
    pyautogui.click(2485, 245)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.doubleClick(1123, 486)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

def last():
    time.sleep(0.5)
    pyautogui.click(618,768)
    time.sleep(0.5)
    pyautogui.click(621, 833)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.click(3302,247)
    time.sleep(0.5)
    pyautogui.click(3302,247)



def demander_et_executer(fonction, nom_fonction):
    reponse = input(f"Voulez-vous exécuter {nom_fonction}? (oui/non) ")
    if reponse.lower() == 'oui':
        fonction()

demander_et_executer(gon, "gon")
demander_et_executer(yes, "yes")
demander_et_executer(toi, "toi")
demander_et_executer(beforelast, "last")
demander_et_executer(last, "last")