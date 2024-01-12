from pyautogui import *

sleep(2)
local = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\Circulo\circle.png')
while True:
    if local is True:
        print('imagem não encontrada')
        sleep(0.5)
    else:
        click(local)
        print('imagem encontrada')
        sleep(3)

''' Script Criado com o intuito do codigo Clicar na imagem 
    Fornecida quando aparente na tela '''

# Site: https://www.adamantiun.com.br/reflexo-adamantiun-gamer'