from pyautogui import * 

try:
    
    sleep(0.5)
    moveTo(111, 1058)
    click()

    sleep(0.5)
    typewrite('google chrome\n', interval=0.1)

    sleep(1)
    
    press('f11')
    
    user = locateOnScreen('Person.png')
    
    click(user)

    sleep(0.5)
    typewrite('https://www.crunchyroll.com/pt-br\n', interval=0.01)

    sleep(0.5)

except:
    print('erro')