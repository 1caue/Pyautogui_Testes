from pyautogui import *
import webbrowser 

# Abrindo a pagina
webbrowser.open("http://www.google.com")

# Esperando 3s para ele abrir
sleep(3)

# Encontrando a página de pesquisa 
press('win' + 'up')
pesquisa = locateOnScreen(r"C:\Users\CAUÊ\Documents\PyAutoGui\Codes\search.png") 

# Texto digitado na pagina 
typewrite("pyautogui\n")

