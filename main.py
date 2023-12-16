import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# URL van de website voor web scraping
web_scrape_url = "https://stenbisschop.netlify.app/"
text_field_url = "https://docs.google.com/forms/d/e/1FAIpQLSfUSqdaooNfJd_xZYM7ZIhpeLOscAR_prm9QBvxpSYfL_RRjQ/viewform?usp=sf_link"

# Haal de eerste h1-tekst op van de web_scrape_url
response = requests.get(web_scrape_url)
soup = BeautifulSoup(response.text, 'html.parser')
eerste_h1 = soup.find('h1').text.strip()

# Open een webbrowser (Chrome in dit voorbeeld) met Selenium
driver = webdriver.Chrome()

# Ga naar het text_field_url
driver.get(text_field_url)

# Wacht tot het tekstveld met de jsname "YPqjbf" aanwezig is
wait = WebDriverWait(driver, 10)
text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@jsname="YPqjbf"]')))
text_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@jsname="YPqjbf"]')))

# Vul het tekstveld in met de opgehaalde eerste h1-tekst
text_field.send_keys(eerste_h1)

# Wacht even om ervoor te zorgen dat het veld wordt ingevuld voordat verder wordt gegaan
time.sleep(5)

# Vind de knop met de class "NPEfkd" (Next button)
next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'NPEfkd')))

# Klik op de knop "Next"
next_button.click()

# Wacht even om ervoor te zorgen dat het veld wordt ingevuld voordat verder wordt gegaan
time.sleep(5)

# Vind het label voor de checkbox met de tekst "Option 1"
checkbox_span = driver.find_element(By.XPATH, '//span[contains(@class, "aDTYNe") and contains(text(), "Option 1")]')

# Klik op het checkbox label
checkbox_span.click()

# Wacht even om ervoor te zorgen dat het veld wordt ingevuld voordat de browser wordt gesloten
time.sleep(5)

# Sluit de browser
driver.quit()
