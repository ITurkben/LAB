import pyautogui
import time

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

yes()
