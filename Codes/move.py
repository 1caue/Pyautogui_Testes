from pyautogui import *

# Deixando em tela cheia 
sleep(1)
press('f11')

# Movendo o cursor para a posição 
sleep(0.5)
click(22, 53)

# Movendo o cursor até a posição do arquivo desejado
moveTo(110, 409, duration=0.25)

# Movendo o arquivo até a pasta desejada
dragTo(108, 96, duration=1, button='left')


# Pressionando enter para confirmar a mudança de pasta
sleep(0.5)
press('enter')

# Saindo da tela cheia 
press('f11')

''' 
    Codigo Criado com o Intuito da maquina Mover arquivo
    De uma pasta para outra no Vs Code
''' 