import pyautogui
pyautogui.sleep(2)
pyautogui.displayMousePosition()

for i in ('i' * 100):
    cord = pyautogui.locateOnScreen('alvo.png', region=(735, 386, 1168, 822))
    pyautogui.click(cord, button='left')
    pyautogui.PAUSE = 0.000000000000001

# site : https://www.arealme.com/aim-test/pt/#google_vignette