from pyautogui import *

sleep(2)

# Abrir Calculadora
click(201, 1060)
write('calculadora\n', interval=0.1)
sleep(2)

# Procurar Números 
dois = locateAllOnScreen('dois.png')

for num in dois:
    x, y = num.left, num.top
    click(x, y)

''' Todo esse sistema de clique foi feito com a calculadora 
    com o intuito que ela digite '1227' '''