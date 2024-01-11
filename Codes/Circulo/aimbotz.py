from pyautogui import *

sleep(2)
local = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\Circulo\circle.png')
while True:
    if local is True:
        click(local)
    else:
        print('imagem não encontrada')
        sleep(0.5)

# Site: https://www.adamantiun.com.br/reflexo-adamantiun-gamer'