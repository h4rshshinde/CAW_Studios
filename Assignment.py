from selenium import webdriver
from selenium.webdriver.common.by import By

# Setting up the Firefox web driver
driver = webdriver.Firefox()

# Navigate to the URL
url = "https://testpages.herokuapp.com/styled/tag/dynamic-table.html"
driver.get(url)

driver.maximize_window()
driver.implicitly_wait(5)

# Finding and clicking the button with the text "Table Data"
button = driver.find_element(By.XPATH, "//*[text() = 'Table Data']")
button.click()

inputBox = driver.find_element(By.XPATH, "//textarea[@id='jsondata']")
inputBox.clear()

jsonData = "[{\"name\" : \"bob\", \"age\" : 20, \"gender\": \"male\"}, {\"name\": \"George\", \"age\" : 42, \"gender\": \"male\"}, {\"name\": \"Sara\", \"age\" : 42, \"gender\": \"female\"}, {\"name\": \"Conor\", \"age\" : 40, \"gender\": \"male\"}, {\"name\": \"Jennifer\", \"age\" : 42, \"gender\": \"female\"}]"

inputBox.send_keys(jsonData)

# driver.find_element(By.XPATH,)
refreshButton = driver.find_element(By.XPATH, "//button[@id='refreshtable']")
refreshButton.click()

driver.implicitly_wait(10)

# Close the web driver
driver.quit()

