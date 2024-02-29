from tkinter import *
from defs import *

interface = Tk()
interface.title('windows 10 pro')

btn_click(interface, "Minimizar Tela", 20, 20, 65, command_click, 1799, 11)

btn_click(interface, "Entrar nos aplicativos", 20, 20, 95, command_click, 24, 1054)

btn_click(interface, "Barra de pesquisa", 20, 20, 125, command_click, 114, 1057)

escrever(interface, "Escrever", 20, 20, 155, write, 'ola mundo')

pressionar(interface, "Comando", 20, 20, 185, 'f10')

pressionar2(interface, "Abrir Executador", 20, 20, 215, 'win', 'r')

pressionar2(interface, "Ver Janelas Abertas", 22, 175, 155, 'win', 'tab')

pressionar2(interface, "Abrir Explorador de arquivos", 22, 175, 185, 'win', 'e')

pressionar2(interface, "Abrir Configurações", 20, 175, 215, 'win', 'i')

pressionar2(interface, "Fechar", 20, 1, 290, 'alt', 'f4')

interface.geometry("370x320+200+500")
interface.mainloop()