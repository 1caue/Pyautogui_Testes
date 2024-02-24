from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyautogui import *

user = input('O que deseja traduzir?: ')

pacote = r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\chromedriver.exe'
chrome_service = Service(pacote)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://translate.google.com.br/?hl=pt-BR')
hotkey('win', 'up')
sleep(1)

write(user)

sleep(4)
copy = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div/div[6]/div/div[6]/div[2]/span[2]/button/div[3]')
copy.click()

sleep(1)
click(503, 1056)
hotkey('win', 'up')

sleep(1)
hotkey('ctrl', 'v')

sleep(1)
hotkey('ctrl', 's')

sleep(60)

'Incompleto'