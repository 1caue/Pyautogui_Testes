from pyautogui import *
from random import randint

def gerador(a, b):
    sleep(0.5)
    aleatorio = randint(a, b)
    aleatoriostr = str(aleatorio)
    return aleatoriostr

def meses(x):
    for a in range(1, x):
        write(f'Mes {a}')
        press('enter')

def pagamento_folha(x):
    sleep(0.5)
    for b in range(1, x):
        num_sort = gerador(9240, 13200)
        write(num_sort, interval=0.1)
        press('enter')

