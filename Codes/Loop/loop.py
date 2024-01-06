from pyautogui import *
import webbrowser

webbrowser.open('https://www.google.com/search?q=calculadora&oq=ca&gs_lcrp=EgZjaHJvbWUqDggBEEUYJxg7GIAEGIoFMgYIABBFGDwyDggBEEUYJxg7GIAEGIoFMgYIAhBFGDsyBggDEEUYOzIGCAQQRRg7MgYIBRBFGDwyBggGEEUYPDIGCAcQRRg80gEIMTgyM2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8')
sleep(2)

try:
    while True:
        dois = locateOnScreen('dois.png')
        multiplicar = locateOnScreen('multiplicar.png')
        sete = locateOnScreen('sete.png')
        igual = locateOnScreen('igual.png')

        if (dois is None) or (multiplicar is None) or (sete is None) or (igual is None):
            continue
        
        else: 
            click(center(dois))

            sleep(1)
            click(center(multiplicar))

            sleep(1)
            click(center(sete))

            sleep(1)
            click(center(igual))

            sleep(1)
            print(f"{dois}\n{multiplicar}\n{sete}\n{igual}\n")
            break

except ImageNotFoundException:
    print("Imagem não encontrada")

# Site https://www.google.com/search?q=calculadora&oq=calcy&gs_lcrp=EgZjaHJvbWUqDwgBEAAYChiDARixAxiABDIJCAAQRRg5GIAEMg8IARAAGAoYgwEYsQMYgAQyBwgCEAAYgAQyDAgDEAAYChixAxiABDIJCAQQABgKGIAEMg8IBRAAGAoYgwEYsQMYgAQyCQgGEAAYChiABDIMCAcQABgKGLEDGIAEMgwICBAAGAoYsQMYgAQyDwgJEAAYChiDARixAxiABNIBCDI0NDdqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8