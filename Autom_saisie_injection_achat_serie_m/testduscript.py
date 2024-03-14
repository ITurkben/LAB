import pyautogui
import time


def test():
    pyautogui.doubleClick(325, 250)
    time.sleep(5)
    pyautogui.write('tca')
    pyautogui.press('tab')
    pyautogui.write('tca')
    pyautogui.press('enter')
    
    time.sleep(3)
    pyautogui.hotkey('ctrl', 's')
    pyautogui.click(1480, 422)
test()