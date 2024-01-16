import pyautogui
import keyboard
import time

def click(x, y):
    pyautogui.click(x, y)

while not keyboard.is_pressed('c'):
    print('Começou a percorrer o SC')
    sc = pyautogui.screenshot(region=(0, 0, 629, 477))
    width, height = sc.size

    for x in range(0, width, 20):
       achou = 0
       
       for y in range(0, height, 20):
           r,g,b = sc.getpixel((x,y))
           print(r,g,b)    

           if r == 255 and b == 78:
               print('ok')
               click(x, y)
               achou = 1
               time.sleep(1)
               break
       
       if achou == 1:
           break    

# http://www.aimbooster.com/ 