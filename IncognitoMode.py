import time

from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

##For chrome incognito window
# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# browser = webdriver.Chrome(options=chrome_options)

##for firefox private window
firefox_options = Options()
firefox_options.add_argument("--private")
browser = webdriver.Firefox(options=firefox_options)

browser.maximize_window()
url = "https://www.google.com/"
browser.get(url)

time.sleep(2)
browser.quit()