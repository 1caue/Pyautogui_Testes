from pyautogui import *
import webbrowser

# Entrando no site 
webbrowser.open('https://form.jotform.com/240106728409656')
click(1747, 433)   

# Digitando o Nome
sleep(2)
press('tab')
write('Caue', interval=0.01)

# Digitando o Sobrenome
sleep(0.5)     
press('tab')
write(' Santos Pereira', interval=0.01)

# Digitando o número
sleep(0.5)
press('tab')
write('73 93243-55275', interval=0.01)

# Digitando o Email
sleep(0.5)
press('tab')
write('joaozinhopedemesa@gmail.com', interval=0.01)

# Digitando o endereço
sleep(0.5)
press('tab')
write('Casa na arvore', interval=0.01)
press('tab')
write('Casa Amarela', interval=0.01)

# Digitando a cidade e estado
sleep(0.5)
press('tab')
write('Salvador', interval=0.01)
press('tab')
write('Bahia', interval=0.01)

# Digitar endereço postal
sleep(0.5)
press('tab')
write('422142-42', interval=0.01)

scroll(-1000) # Scrollando a tela

# Procurando por Imagem
horas = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Testes\Preenchimento de Formulário\horas.png')

# Digitando a data
sleep(2)
press('tab')
write('01/17/2024', interval=0.01)

# Dando Tab e Digitando a data novamente
for a in range(0, 9):
    press('tab')
write('22/05/2000')

# Selecionando as horas
click(horas)

# Digitando as horas
for a in range(0, 10):
    press('tab')
write('10:00')

scroll(-400) # Scrollando a tela

for a in range(0, 2):
    press('tab')
write('Fim')
press('tab')
press('enter')

# Formulário https://form.jotform.com/240106728409656

''' Script Criado com o Intuito de 
    Preencher um Formulário Automaticamente
    Nenhuma informação passada é Veridica 
    (Apenas Meu Nome)
'''