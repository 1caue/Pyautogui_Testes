from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyautogui import *

pacote = 'chromedriver.exe'
chrome_service = Service(pacote)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal')
hotkey('win', 'up')
sleep(2)

procura = driver.find_element(By.NAME, 'search')
procura.click()
write('Python')
press('enter')
sleep(10)

new_tab = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\Wikipédia\new.png')
click(new_tab, button='middle')
click(x=315, y=11)
moveTo(x=188, y=276)
sleep(1)

press(['tab', 'tab', 'tab', 'tab'])
write('PHP')
press('enter')
sleep(10)

click(new_tab, button='middle')
click(x=552, y=11)
moveTo(x=188, y=276)
press(['tab', 'tab', 'tab', 'tab'])
write('Ruby on Rails')
press('enter')

sleep(100)

'Script Criado com o intuito de Fazer pesquisa no Wikipédia'