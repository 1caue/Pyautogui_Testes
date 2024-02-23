from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyautogui import *

pacote = r'C:\Users\CAUÊ\Documents\PyAutoGui\Codes\chromedriver.exe'
chrome_service = Service(pacote)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://gemini.google.com/')
hotkey('win', 'up')
sleep(1)

comecar = driver.find_element(By.XPATH, '//*[@id="app-root"]/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div/main/div/welcome-window/div/landing-page-variant-a/div/div/div[2]/button/span[2]')
comecar.click()
sleep(10)