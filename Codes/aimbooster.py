import pyautogui
import keyboard
import time

def click(x, y):
    pyautogui.click(x, y)

while not keyboard.is_pressed('c'):
    print('Começou a percorrer o SC')
    sc = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    width, height = sc.size

    for x in range(0, width, 7):
        achou = 0

        for y in range(0, height, 7):
            r, g, b = sc.getpixel((x, y))
            print(r, g, b)

            if r == 255 and g == 219 and b == 195:
                print('ok')
                click(x, y)
                achou = 1
                break

        if achou == 1:
            break
