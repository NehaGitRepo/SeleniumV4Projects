from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/nested_frames")
#Switch to main frame
browser.switch_to.frame("frame-top")
#switch to middle frame
browser.switch_to.frame("frame-middle")
#finding content of middle frame by ID
content = browser.find_element(By.ID,"content").text
print("Content in middle frame is: ",content)

#switch to default content
browser.switch_to.default_content()

#switch to bottom frame
browser.switch_to.frame("frame-bottom")
content_bottom = browser.find_element(By.TAG_NAME,"body").text
print("Content in the Bottom frame is: ",content_bottom)

browser.quit()
