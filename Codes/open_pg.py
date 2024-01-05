from pyautogui import *
import webbrowser 

# Abrindo a pagina
webbrowser.open("http://www.google.com")

# Esperando 5s para ele abrir
PAUSE = 5

# Encontrando a página de pesquisa 
pesquisa = locateCenterOnScreen("search.png") 

# Texto digitado na pagina 
typewrite("pyautogui\n")

