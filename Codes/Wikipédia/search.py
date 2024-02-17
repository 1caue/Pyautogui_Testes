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
sleep(3)

new_tab = locateOnScreen(r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\Wikipédia\new.png')
click(new_tab, button='middle')
click(x=361, y=17)
sleep(5)

procura2 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/div/input')
procura2.click()
write('Java')
press('enter')

sleep(100)
