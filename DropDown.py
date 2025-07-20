from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)
#1.locating the dropdown
dropdown_element = driver.find_element(By.ID,"dropdown")
target_value = "Option 4"
select = Select(dropdown_element)
option_count = len(select.options)


#2.clicking on the desired option in drop down
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break

    else:
        print(f"option '{option.text}' is Not selected.'{target_value}' is required")



# #3.select the value by visible text
# select.select_by_visible_text("Option 2")

# #4.select the value by Index
# select.select_by_index(2)


# #5.select the option by using a value
# select.select_by_value("2")



# #6.counting the actual number of options present in drop down and comparing it with any random expected count
# expected_count = 3
# if option_count == expected_count:
#     print("Test cases passed, count is correct")
# else:
#     print("Test cases failed, Count is incorrect")

driver.quit()
