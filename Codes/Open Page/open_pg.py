from pyautogui import *
import webbrowser 

# Abrindo a pagina
webbrowser.open("http://www.google.com", new=0)

# Esperando 3s para ele abrir
sleep(2)

# Encontrando a página de pesquisa 
press('win' + 'up')
pesquisa = locateOnScreen("search.png") 
click(pesquisa)

# Texto digitado na pagina 
typewrite("pyautogui\n")

webbrowser.open('https://chat.openai.com/c/4f4b63e2-8cf4-498f-8866-0f18be51b79e')