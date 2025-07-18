from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
driver.quit()