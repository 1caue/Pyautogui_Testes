from pyautogui import *
from time import sleep

sleep(2)
click(157, 1068)

sleep(2)
write('paint\n', interval=0.1)

sleep(1)
hotkey('win', 'up')

sleep(2)
click(561, 257)

distance = 500
delta = 50

while distance > 0:
    drag(distance, 0, duration=0.2)
    distance = distance - delta
    drag(0, distance, duration=0.2) 
    drag(-distance, 0, duration=0.2)

    distance = distance - delta
    drag(0, -distance, duration=0.2)

hotkey('ctrl', 's')
