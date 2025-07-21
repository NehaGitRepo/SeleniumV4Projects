import time

from selenium import  webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import datetime,timedelta

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)
browser.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()
FrameLo = browser.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(FrameLo)
time.sleep(2)
browser.find_element(By.CSS_SELECTOR,"#datepicker").click()
current_date = datetime.now()
next_date = current_date + timedelta(days=-1)
formatted_date = next_date.strftime("%m/%d/%y")
browser.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formatted_date+Keys.TAB)
time.sleep(2)
browser.quit()