import pyautogui
pyautogui.sleep(2)

cor = (251, 0, 7)
regiao = (735, 386, 1168, 822)
try: 
    for i in range(100):
        pyautogui.sleep(0.0001)
        pyautogui.moveTo(937, 245)
        px_color = pyautogui.pixel(800, 500)
        cord = pyautogui.locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\Aimbot_tst\alvo.png', region=(735, 386, 1168, 822))

        if cord:
            pyautogui.click(cord, button='left')

        elif px_color == cor:
            pyautogui.click(cor, button='left')

        pyautogui.sleep(0.00001)

except KeyboardInterrupt:
    print('Erro: Imagem não Encontrada')

# site : https://www.arealme.com/aim-test/pt/#google_vignette
    
    ''' Script Criado com o intuito de simular um aimbot 
        em um game de reflexo'''