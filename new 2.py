import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# URL of the second link
text_field_url = "https://docs.google.com/forms/d/e/1FAIpQLSfUSqdaooNfJd_xZYM7ZIhpeLOscAR_prm9QBvxpSYfL_RRjQ/viewform?usp=sf_link"

# Open a web browser (Chrome in this example) with Selenium
driver = webdriver.Chrome()

# Go to the text_field_url
driver.get(text_field_url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//input[@jsname="YPqjbf"]')))

# Find all input fields on the page
input_fields = driver.find_elements(By.XPATH, '//input[@jsname="YPqjbf"]')

# Vind het label voor de checkbox met de tekst "Option 1"
checkbox_span = driver.find_element(By.XPATH, '//span[contains(@class, "aDTYNe") and contains(text(), "Option 1")]')

# Klik op het checkbox label
checkbox_span.click()

# Collect jsnames with index from the input fields
jsnames = []
for index, input_field in enumerate(input_fields, start=1):
    # Read the jsname from the input field
    jsname = input_field.get_attribute("jsname")
    jsnames.append(f"{jsname}_{index}")

    # Fill the input field with its corresponding jsname using ActionChains
    ActionChains(driver).move_to_element(input_field).click().send_keys(jsname).perform()

    # Add a delay to see the interaction
    time.sleep(1)

# Click the "NPEfkd" button
next_button = driver.find_element(By.CLASS_NAME, 'NPEfkd')
next_button.click()

# Add a delay after clicking the button
time.sleep(2)

# Find all input fields on the page
input_fields = driver.find_elements(By.XPATH, '//input[@jsname="YPqjbf"]')

# Collect jsnames with index from the input fields
jsnames = []
for index, input_field in enumerate(input_fields, start=1):
    # Read the jsname from the input field
    jsname = input_field.get_attribute("jsname")
    jsnames.append(f"{jsname}_{index}")

    # Fill the input field with its corresponding jsname using ActionChains
    ActionChains(driver).move_to_element(input_field).click().send_keys(jsname).perform()

    # Add a delay to see the interaction
    time.sleep(1)

# Vind het label voor de checkbox met de tekst "Option 1"
checkbox_span = driver.find_element(By.XPATH, '//span[contains(@class, "aDTYNe") and contains(text(), "Option 1")]')

# Klik op het checkbox label
checkbox_span.click()

time.sleep(2)

# Output the list of jsnames with index before and after clicking the button
print("jsnames before clicking NPEfkd:", jsnames)

# Close the browser
driver.quit()
