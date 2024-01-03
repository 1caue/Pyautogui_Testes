from pyautogui import *

local1 = locateOnScreen('circulo.png')

print(local1)

print(local1.left)
print(local1[0])

print(local1.top)
print(local1[1])

local_todos = list(locateAllOnScreen('circulo.png'))
print(local_todos)