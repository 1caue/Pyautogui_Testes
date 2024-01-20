from pyautogui import *

moveTo(966, 1076)
hotkey('win', 'd')
sleep(2)

img = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Projeto\img.png')

try:
    
    if img:
        print('tudo ok')
        prin = screenshot(region=(0, 0, 344, 1026))
        prin.show()
    else:
        print('imagem não encontrada')

except ImageNotFoundException:
    print('Erro')
        
