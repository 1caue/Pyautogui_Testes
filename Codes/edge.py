from pyautogui import *

sleep(1)
# Só é necessario se for mover o mouse para o canto superior esquerdo
FAILSAFE = False

# Pegando as dimensôes da tela
width, height = size()

# Movendo
moveTo(10, 1057)

# Clicando na tela
click()

# Digitando o aplicativo e dando enter

typewrite('edge', interval=0.5)
press('enter')

sleep(2)

# Obtendo as coordenadas da imagem 
mais = locateOnScreen('Mais.png')

# Clicando no centro da imagem 
click(mais)

# Digitando na barra de pesquisa o instragram, O "\n" serve para dar enter
sleep(1)
typewrite('instagram\n', interval=0.2)

# Pressionando F11 para deixar a guia em tela cheia
press('f11')

sleep(2)
print("!")