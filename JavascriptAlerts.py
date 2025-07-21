from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)
#handling JS Alert
AlertButton = browser.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
AlertButton.click()

#switch to alert
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(2)
alert.accept()
time.sleep(2)

#Handling JS Confirm
ConfirmButton = browser.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
ConfirmButton.click()

#switch to alert
Confirm = browser.switch_to.alert
Confirm_text = Confirm.text
print(Confirm_text)
time.sleep(2)
alert.dismiss()
time.sleep(2)


#Handling JS prompt
#Handling JS Confirm
PromptButton = browser.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
PromptButton.click()

#switch to alert
JSPrompt = browser.switch_to.alert
Prompt_text = JSPrompt.text
print(Prompt_text)
time.sleep(2)
JSPrompt.send_keys("This is a selenium with python script")
time.sleep(2)
alert.accept()

browser.quit()