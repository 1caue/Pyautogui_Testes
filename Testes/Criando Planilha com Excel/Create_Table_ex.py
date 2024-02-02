''' Criação de Tabelas no Excel Automaticamente '''

from pyautogui import *
from defs import *

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
write('=$B$2:$K$13')
press('enter')

# ------
click(120, 204, button='left')
typewrite('Mes')

sleep(1)
click(124, 229, button='left')
meses(13)

# ------ 
sleep(1)
click(198, 211, button='left')
write('Pagamento de folha')
doubleClick(245, 172, button='left')

sleep(1)
click(204, 228, button='left')
pagamento_folha(13)

# -----
sleep(2)
click(212, 344, button='left')
write('Conta de energia')
doubleClick(392, 172, button='left')

'Incompleto'