from pyautogui import click, write, doubleClick, position, typewrite
from time import sleep

click(756, 23, button='left')

sleep(1)
typewrite('https://twitter.com/home/\n')

sleep(4)
click(513, 187, button='left')
write('ola')

sleep(2)
print(position())
