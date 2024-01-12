from pyautogui import *

sleep(1)
# Clicando na tela
click(10, 1057)

# Digitando o aplicativo e dando enter
typewrite('edge', interval=0.5)
press('enter')

# Colocando em tela cheia
sleep(1)
keyDown('winleft')
press('up')
keyUp('winleft')

# Digitando na barra de pesquisa a Documentação da biblioteca, O "\n" serve para dar enter
sleep(1)
write('PyAutoGUI\n', interval=0.05)

sleep(3) # Esperando a pagina carregar

# Entrando na Documentação Oficial
press('tab')
press('enter')

''' Script criado com o intuido do Computador Entrar no Edge 
    e Pesquise sobre a biblioteca PyAutoGUI'''