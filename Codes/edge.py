from pyautogui import *

sleep(1)
# Movendo
moveTo(10, 1057)

# Clicando na tela
click()

# Digitando o aplicativo e dando enter
typewrite('edge', interval=0.5)
press('enter')

# Colocando em tela cheia
sleep(1)
press('f11')

# Loop apertando tab até ele chegar na barra de pesquisa
sleep(2)
for a in range(0, 2):
    press('tab')

# Digitando na barra de pesquisa o instragram, O "\n" serve para dar enter
sleep(1)
write('instagram\n', interval=0.2)

# "Confirmador" de funcionamento
sleep(1)
print("Funcionouu!!")