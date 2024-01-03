from pyautogui import *
from time import sleep

sleep(2)
click(198, 1064)

sleep(0.5)
click(186, 728)

sleep(0.5)
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