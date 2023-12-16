import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class FormHandler:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    def open_form(self):
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@jsname="YPqjbf"]')))

    def fill_text_fields(self, text):
        input_fields = self.driver.find_elements(By.XPATH, '//input[@jsname="YPqjbf"]')
        for input_field in input_fields:
            ActionChains(self.driver).move_to_element(input_field).click().send_keys(text).perform()
            time.sleep(1)

    def click_checkbox(self, checkbox_text):
        checkbox_span = self.driver.find_element(By.XPATH, f'//span[contains(@class, "aDTYNe") and contains(text(), "{checkbox_text}")]')
        checkbox_span.click()
        time.sleep(2)

    def click_button(self, button_class):
        button = self.driver.find_element(By.CLASS_NAME, button_class)
        button.click()
        time.sleep(2)

    def close_form(self):
        self.driver.quit()

# Example of how to use the class
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfUSqdaooNfJd_xZYM7ZIhpeLOscAR_prm9QBvxpSYfL_RRjQ/viewform?usp=sf_link"
form_handler = FormHandler(form_url)

# Open the form
form_handler.open_form()

# Fill in text fields
form_handler.fill_text_fields("hello world")

# Click checkbox
form_handler.click_checkbox("Option 1")

# Click the first button
form_handler.click_button('NPEfkd')

# Fill in text fields again
form_handler.fill_text_fields("hello world again")

# Click checkbox again
form_handler.click_checkbox("Option 1")

# Close the form
form_handler.close_form()
