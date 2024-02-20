from pyautogui import *

def tab_select(value):
    for a in range(0, value):
        press('tab')
    press('enter')