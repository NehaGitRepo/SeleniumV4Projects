import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
username = "admin"
password = "admin"

browser = webdriver.Chrome()
browser.maximize_window()


#syntax for authentication->  https://username:password@domain/path

url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
browser.get(url)
time.sleep(2)
browser.quit()