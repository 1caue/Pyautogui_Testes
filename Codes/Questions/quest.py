from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from defs import *
from pyautogui import *

pacote = 'chromedriver.exe'
chrome_service = Service(pacote)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://scholar.google.com.br/?hl=pt')
hotkey('win', 'up')
sleep(3)

typewrite('Cancer')
press('enter')

sleep(2)
tab_select(22)

sleep(2)
tab_select(2)

sleep(2)
hotkey('ctrl', 's')
sleep(1)
press('enter')

sleep(60)