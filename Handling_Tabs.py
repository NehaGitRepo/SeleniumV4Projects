from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.maximize_window()
#open 1st  browser  window
browser.get("https://www.selenium.dev/")
#open 2nd  browser window
browser.switch_to.new_window()
browser.get("https://playwright.dev/")
#find total number of windows
number_of_tabs = len(browser.window_handles)
#to print the unique values of browser windows
tabs_value = browser.window_handles
print("ID of all tabs: ",tabs_value)
#print current id of browser window
current_tab = browser.current_window_handle
print("ID of current tab is: ", current_tab)
#click on "get started" link on playwright(2nd window) homepage
browser.find_element(By.CSS_SELECTOR,".getStarted_Sjon").click()
time.sleep(2)
#switching back to first tab
First_Tab = browser.window_handles[0]
if current_tab!=First_Tab:
    browser.switch_to.window(First_Tab)
#click on "Downloads" link on "Downloads" (1st window) homepage
browser.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()
time.sleep(2)
browser.quit()