import pyautogui
import keyboard
import win32api
import win32con

def click2(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed('c'):
    print('Começou a percorrer o SC')
    sc = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    width, height = sc.size

    for x in range(0, width, 17):
        achou = 0

        for y in range(0, height, 17):
            r, g, b = sc.getpixel((x, y))
            print(r, g, b)

            if r == 255 and g == 219 and b == 195:
                print('ok')
                click2(0 + x, 0 + y)
                achou = 1
                break

        if achou == 1:
            break
