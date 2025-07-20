from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.maximize_window()

browser.execute_script("window.scrollTo(0,700)")
table = browser.find_element(By.ID,"countries")
rows = browser.find_elements(By.TAG_NAME,"tr")
row_count = len(rows)   #it also contains the header row
print(row_count)

#finding a target value
target_value = "Australia"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME,"td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Found value : {target_value}")
            found = True
            break

    if found:
        break
if not found:
    print(f"'{target_value}' not found in table")



time.sleep(2)
browser.quit()