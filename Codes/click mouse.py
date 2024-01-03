import pyautogui, time

# pyautogui.click(464, 855, button='left')
# pyautogui.click(511, 833, button='left')
pyautogui.doubleClick(464, 855)
time.sleep(1)
# pyautogui.click(511, 833, button='left')
# pyautogui.click(522, 754, button='left')
pyautogui.doubleClick(511, 833)
time.sleep(1)
# pyautogui.click(457, 737, button='left')
# pyautogui.click(312, 313, button='left')
pyautogui.doubleClick(457, 737)
time.sleep(1)

pyautogui.click(636, 427, button='left')
time.sleep(1)
pyautogui.click(753, 11, button='left')
time.sleep(1)
pyautogui.click(536, 58, button='left')
time.sleep(1)
pyautogui.write("ola")
# Para mostrar a localização do cursor ↓
print(pyautogui.position())

# Todo esse sistema de clique foi feito com a calculadora aberta com o intuito que ela digite '1227'