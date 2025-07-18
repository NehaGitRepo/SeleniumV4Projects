import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.find_element(By.XPATH,"//input[@value='Automation']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@value='Automation']").click()
# time.sleep(2)

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1


expected_checked_count = 2

if checked_count == expected_checked_count:
    print("checkbox count verified")
else:
    print('checkbox count mismatch')

time.sleep(4)
driver.close()