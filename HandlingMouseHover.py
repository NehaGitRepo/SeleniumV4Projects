import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

actions = ActionChains(browser)
hover_element = browser.find_element(By.XPATH,"//a[normalize-space()='SwitchTo']")
time.sleep(2)
actions.move_to_element(hover_element).perform()
browser.find_element(By.XPATH,"//a[normalize-space()='Frames']").click()
time.sleep(2)
