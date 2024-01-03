import pyautogui, time

# Obtem a janela atuva ↓
window = pyautogui.getActiveWindow()
print(f"{window}\n")

# Mostra o nome da janela ↓
print(f"{window.title}\n")

# Imprime o tamanho da janela (largura x altura)
print(f"{window.size}\n")

# Cordenadas do campo superior esquerdo (x e y) 
print(f"{window.topleft}\n")

# Imprime a área da janela ativa, contem informações da área total
print(f"{window.area}\n")

# CLica no topo da janela ativa
pyautogui.click(window.left + 30, window.top + 50)

time.sleep(1.5)
window.width = 1000
time.sleep(3)
window.topleft = (500, 300)

'''Cada uma dessas linhas print acessa propriedades específicas do objeto window, 
que foi obtido usando a função pyautogui.getActiveWindow(). Isso permite visualizar 
informações sobre a janela ativa, como título, tamanho, posição, e outras características 
relacionadas à área da janela.'''
