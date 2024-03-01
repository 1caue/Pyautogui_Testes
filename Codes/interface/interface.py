from defs import *

interface = Tk()
interface.title('Windows 10 Pro')

btn_click(interface, "Minimizar Tela", 20, 20, 35, command_click, 1799, 11)

btn_click(interface, "Entrar nos aplicativos", 20, 20, 65, command_click, 24, 1054)

btn_click(interface, "Barra de pesquisa", 20, 20, 95, command_click, 114, 1057)

pressionar2(interface, "Abrir Executador", 20, 20, 125, 'win', 'r')

pressionar3(interface, "Tirar print", 20, 20, 155, 'win', 'shift', 's')

pressionar2(interface, "Ver Janelas Abertas", 22, 175, 35, 'win', 'tab')

pressionar2(interface, "Abrir Explorador de arquivos", 22, 175, 65, 'win', 'e')

pressionar2(interface, "Abrir Configurações", 22, 175, 95, 'win', 'i')

pressionar2(interface, "Centro de Ação", 22, 175, 125, 'win', 'a')

pressionar2(interface, "Barra de jogos do Windows", 22, 175, 155, 'win', 'g')

pressionar3(interface, "Criar Nova Área de Trabalho", 22, 175, 185, 'ctrl', 'win', 'd')

pressionar3(interface, "Ver data e hora", 13, 5, 260, 'win', 'alt', 'd')

pressionar2(interface, "Fechar", 13, 5, 290, 'alt', 'f4')

interface["bg"] = "grey"
interface.geometry("370x320+200+500")
interface.mainloop()