from selenium import  webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import datetime,timedelta
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

browser.find_element(By.ID,"datepicker2").click()
time.sleep(5)
current_date = datetime.now()
print(current_date)

#To find the next day from current date
next_day = current_date + timedelta(days=1)
print(next_day)
Next_day = str(next_day.day)
print(Next_day)

#current month and year
current_month = datetime.now().month
current_year = current_date.year

#finding next month and year
next_month = (current_month % 12)+1
next_month_year = f"{next_month}/{current_year}"

#handling date picker to select month dropdown
Month_Dropdown = browser.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select_dropdown = Select(Month_Dropdown)
select_dropdown.select_by_value(str(next_month_year))

#handling date picker to select year dropdown and setting it's value to 2025
year_dropdown = browser.find_element(By.CSS_SELECTOR,"select[title='Change the year']")
select_dropdown = Select(year_dropdown)
select_dropdown.select_by_visible_text("2025")

#selecting the date 1 month and 1 date ahead from current date
browser.find_element(By.LINK_TEXT,Next_day).click()
time.sleep(5)













