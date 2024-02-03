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
write('=$B$2:$G$13')
press('enter')

# Criado coluna do Mês
click(120, 204, button='left')
typewrite('Mes')

sleep(1)
click(124, 229, button='left')
meses(13)

# Criando coluna do pagamanto da folha
sleep(1)
click(198, 211, button='left')
write('Pagamento de folha')
doubleClick(245, 172, button='left')

sleep(1)
click(204, 228, button='left')
sort(9240, 13200, 13)

# Criando coluna da conta de energia
sleep(1)
click(344, 211, button='left')
write('Conta de energia')
doubleClick(392, 172, button='left')

sleep(1) 
click(379, 231, button='left')
sort(100, 300, 13)

# Criando coluna da conta de Água
sleep(1)
click(476, 212, button='left')
write('Conta de Agua')
doubleClick(523, 172)

sleep(1)
click(490, 232, button='left')
sort(100, 300, 13)

# Formatando números
sleep(1)
mover(240, 230, 525, 452)

hotkey('ctrl', '1')
click(285, 527, button='left')
press(['down', 'down', 'enter'])

# Somando os gastos de cada Mês
sleep(1)
click(590, 210, button='left')
write('Total de Gastos')
doubleClick(636, 171)

click(613, 232, button='left')
write('=SOMA(C3:E3)')
press('enter')

# Criando Coluna da Quantidade de Funcionários
sleep(1)
click(710, 211, button='left')
write('Quantidade de Funcionarios')
doubleClick(754, 172)

sleep(1)
click(721, 232, button='left')
sort(8, 10, 13)

# Centralizando a coluna dos Funcionários
sleep(1)
mover(766, 230, 772, 453)

hotkey('ctrl', '1')
press(['right','tab', 'backspace','down', 'down', 'enter', 'enter'])