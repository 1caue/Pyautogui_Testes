from pyautogui import *

hotkey('win', 'd')
sleep(2)
click(966, 1076)

try:
    img = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Projeto\att.png')
    
    if img is not None:
        print('tudo ok')

except Exception as e:
   print('Mudanças foram feitas!')
   prin = screenshot(region=(0, 0, 1914, 1034))
   prin.show()

finally:
    sleep(5)
    hotkey('win', 'd')
    