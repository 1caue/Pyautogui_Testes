from pyautogui import *

im = screenshot()
print(pixel(0, 0))
print(pixel(50, 250))

print(pixelMatchesColor(50, 250, (70, 170, 236)))
print(pixelMatchesColor(50, 250, (50, 60, 72)))

