from pyautogui import *

# Movendo o Cursor para o meio da tela
move(954, 411) 

# Localizando a imagem na tele
sleep(1)
local1 = locateOnScreen('debug.png') 

# Imprimindo as informações de localização de maneiras diferentes
print(local1)

print(local1.left)
print(local1[0]) 

print(local1.top)
print(local1[1])

# Localizando e imprimindo todas as instâncias da imagem na tela:
sleep(1)
local_todos = list(locateAllOnScreen('debug.png'))
print(local_todos)

# Clicando na imagem encontrada 
click(local1)

''' Codigo criado com o intuito do Script Clique no "Run"
    Repetidas vezes e imprima sua localização De maneiras 
    Diferentes '''