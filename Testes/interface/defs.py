from tkinter import *
from functools import partial 
from pyautogui import *

def command_click(x, y):
    click(x, y)

def btn_click(a, b, w, x, y, cmd, xpy, ypy):
    bt = Button(a, width=w, text=b, command=partial(cmd, xpy, ypy))
    bt.place(x=x, y=y)

def pressionar(a, b, w, x, y, comando):
    bt = Button(a, width=w, text=b, command=lambda: press(comando))
    bt.place(x=x, y=y)

def pressionar2(a, b, w, x, y, c1, c2):
    bt = Button(a, width=w, text=b, command=lambda: hotkey(c1, c2))
    bt.place(x=x, y=y)

def pressionar3(a, b, w, x, y, c1, c2, c3):
    bt = Button(a, width=w, text=b, command=lambda: hotkey(c1, c2, c3))
    bt.place(x=x, y=y)