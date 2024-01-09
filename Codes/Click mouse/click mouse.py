from pyautogui import *

sleep(2)

# Abrir Calculadora
click(201, 1060)
write('calculadora\n', interval=0.1)
sleep(1)

# Procurar Números 
um = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\Click mouse\um.png')
dois = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\Click mouse\dois.png')
sete = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\Click mouse\sete.png')

click(um)
doubleClick(dois)
click(sete)

''' Todo esse sistema de clique foi feito com a calculadora 
    com o intuito que ela digite '1227' '''
print(sete)