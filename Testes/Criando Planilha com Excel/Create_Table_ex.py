''' Criação de Tabelas no Excel Automaticamente '''

from pyautogui import *

# Abrindo o Excel 
click(121, 1063, button='left')
sleep(0.7)
write(' excel\n', interval=0.2)

# Colocando em Tela Cheia
sleep(0.1)
keyDown('winleft')
press('up')
keyUp('winleft')

# Selecionar a Opção De Tabela formatada
sleep(1)
formatar = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Testes\Criando Planilha com Excel\formatar.png')
click(formatar, button='left')

# Selecionando Formatação
sleep(0.5)
for a in range(0, 36):
    press('tab')
press('enter')

# Puxar de A1 até H10
sleep(0.5)
write('=$B$2:$K$12')
press('enter')

click(924, 510, button='left')

