import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class FormFiller:
    def __init__(self, form_url, jsnames):
        self.form_url = form_url
        self.jsnames = jsnames
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def fill_form(self):
        self.driver.get(self.form_url)

        # Wait for the page to load
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@jsname="YPqjbf"]')))

        # Find the checkbox and click it
        checkbox_span = self.driver.find_element(By.XPATH, '//span[contains(@class, "aDTYNe") and contains(text(), "Option 1")]')
        checkbox_span.click()

        # Find all input fields on the page and fill in the values
        input_fields = self.driver.find_elements(By.XPATH, '//input[@jsname="YPqjbf"]')
        for jsname, input_field in zip(self.jsnames, input_fields):
            ActionChains(self.driver).move_to_element(input_field).click().send_keys(jsname).perform()
            time.sleep(1)

        # Click the "NPEfkd" button
        next_button = self.driver.find_element(By.CLASS_NAME, 'NPEfkd')
        next_button.click()

        # Add a delay after clicking the button
        time.sleep(2)

        # Find all input fields on the page and fill in the values again
        input_fields = self.driver.find_elements(By.XPATH, '//input[@jsname="YPqjbf"]')
        for jsname, input_field in zip(self.jsnames, input_fields):
            ActionChains(self.driver).move_to_element(input_field).click().send_keys(jsname).perform()
            time.sleep(1)

        # Find the checkbox and click it
        checkbox_span = self.driver.find_element(By.XPATH, '//span[contains(@class, "aDTYNe") and contains(text(), "Option 1")]')
        checkbox_span.click()

        time.sleep(2)

    def close_browser(self):
        self.driver.quit()

# Example usage
jsnames_list = ["thanks", "chat", "GPT"]
form_filler = FormFiller("https://docs.google.com/forms/d/e/1FAIpQLSfUSqdaooNfJd_xZYM7ZIhpeLOscAR_prm9QBvxpSYfL_RRjQ/viewform?usp=sf_link", jsnames_list)
form_filler.fill_form()
form_filler.close_browser()
