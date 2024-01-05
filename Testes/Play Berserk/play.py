''' 
    Codigo com o objetivo de Entrar no chrome, digitar o nome do site, 
    Pesquisar o nome do anime desejado e dar play no ultimo episódio
'''

import pyautogui
from time import sleep

try:
    # Movendo Cursor até o "Pesquisar"
    pyautogui.moveTo(111, 1058)
    pyautogui.click()
   
    # Digitando e dando enter no chrome
    sleep(0.5)
    pyautogui.typewrite('google chrome\n', interval=0.1)
   
    # Deixando a tela Cheia
    sleep(1)
    pyautogui.press('win' + 'up')
   
    # Dando tab até ele chegar no modo visitante
    sleep(1)
    for a in range(0, 8):
        pyautogui.press('tab')
    
    # Pressionando enter após ela ter chegado no modo visitante
    sleep(0.5)
    pyautogui.press('enter')

    # Pesquisando o site
    sleep(0.5)
    pyautogui.typewrite('https://www.crunchyroll.com/pt-br\n', interval=0.01)

    # Loop for até ela chegar na lupa de pesquisa
    sleep(5)
    for a in range(0, 13):
        pyautogui.press('tab')
    pyautogui.press('enter')

    # Enter e Escrita do anime desejado
    pyautogui.typewrite(' Berserk ', interval=0.5)
    pyautogui.press('enter')

    # Loop até o botão de play
    sleep(1)
    for a in range(0, 3):
        pyautogui.press('tab')
    pyautogui.press('enter')

except:
    print('erro')