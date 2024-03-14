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

gon()
