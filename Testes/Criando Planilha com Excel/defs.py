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


def sort(pn, sn, x):
    sleep(0.5)
    for b in range(1, x):
        num_sort = gerador(pn, sn)
        write(num_sort)
        press('enter')

def mover(xini, yini, xfim, yfim):
    x_ini,  y_ini = xini, yini
    x_final, y_final = xfim, yfim
    moveTo(x_ini, y_ini)
    mouseDown()

    moveTo(x_final, y_final)
    sleep(1)
    mouseUp()

