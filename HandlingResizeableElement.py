import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://demo.automationtesting.in/Resizable.html"
browser.get(url)

resizeable_element = browser.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
initial_element_size = browser.find_element(By.XPATH,"//div[@id='resizable']")
initial_size = initial_element_size.size
print("Initial Size: ",initial_size)

action_chains = ActionChains(browser)
action_chains.click_and_hold(resizeable_element).move_by_offset(100,100).release().perform()
time.sleep(2)

resized_element_size = initial_element_size.size
print("Resized element size: ",resized_element_size)
browser.quit()