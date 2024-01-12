from pyautogui import *
import webbrowser 

# Abrindo a pagina
webbrowser.open("http://www.google.com", new=0)

# Esperando 2s para ele abrir
sleep(2)

# Encontrando a página de pesquisa 
press('win' + 'up')
pesquisa = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\Open Page\search.png') 
click(pesquisa)

# Texto digitado na pagina 
typewrite("pyautogui\n")

webbrowser.open('https://pyautogui.readthedocs.io/en/latest/')