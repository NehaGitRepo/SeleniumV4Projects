from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/iframe")
browser.find_element(By.XPATH,"//div[@aria-label='Close']//*[name()='svg']").click()#To close the warning

iFrame = browser.find_element(By.ID,"mce_0_ifr")
browser.switch_to.frame(iFrame)

Text_Editor = browser.find_element(By.ID,"tinymce")
# Text_Editor.clear()
Text_Editor.send_keys("Dummy text for test script using selenium with python")

#come out of iFrame

browser.switch_to.default_content()
Selenium_link = browser.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']")
Selenium_link.click()
time.sleep(4)
browser.quit()