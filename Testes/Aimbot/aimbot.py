import pyautogui
import keyboard
import time
import pywin32_system32

def click(x, y):
    pywin32_system32.SetCursorPos(x, y)
    pywin32_system32.mouse_event(pywin32_system32.MOUSEEVENTF_LEFTDOWN,0,0)
    pywin32_system32.mouse_event(pywin32_system32.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('c') == False:
    print('Começou a percorrer o SC')
    sc = pyautogui.screenshot(region=(1899, 736, 580, 400))
    width, height = sc.size

    for x in range(0, width, 12):
       achou = 0
       for y in range(0,height,12):
           r,g,b = sc.getpixel((x,y))
           print(r,g,b)

           if r == 255 and b == 73:
               achou = 1
               click(1899, 736)
               time.sleep(0.05)
               break
       if achou == 1:
         break

