from tkinter import *
from functools import partial 
from pyautogui import *

interface = Tk()
interface.title('Auto-Tasks')

def command_click(x, y):
    click(x, y)

def command_write(word):
    write('ola mundo')

def btn(a, b, w, x, y, cmd):
    bt = Button(a, width=w, text=b, command=partial(cmd, 1799, 11))
    bt.place(x=x, y=y)

def frase(a, b, x, y):
    lb = Label(a, text=b)
    lb.place(x=x, y=y)

btn(interface, "Minimizar Tela", 20, 20, 65, command_click)
btn(interface, "Minimizar Tela", 20, 20, 65, command_write)

interface.geometry("370x320+200+500")
interface.mainloop()