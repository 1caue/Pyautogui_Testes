from pyautogui import *

sleep(7)
local1 = list(locateAllOnScreen('circulo.png'))

for a in range(0, 5):
    if local1:
        for circle_pos in local1:
            circle_x, circle_y, _, _ = circle_pos
            click(605, 359)

    else:
        print("circulo não encontrado")

    print(a + 1)
    print(f"{circle_pos}\n")
    sleep(6)

# Site: https://www.adamantiun.com.br/reflexo-adamantiun-gamer