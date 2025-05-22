# selenium_basics_cheatsheet.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Setup
s = Service(r"D:\path\to\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://example.com")

# Finding elements
driver.find_element(By.ID, "username").send_keys("myuser")
driver.find_element(By.CLASS_NAME, "btn").click()
driver.find_element(By.CSS_SELECTOR, "label[for='tree-node-documents']").click()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("email@example.com")

# Dropdown example
dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
dropdown.select_by_visible_text("Purple")

# Alert handling
driver.find_element(By.ID, "alertButton").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

# Upload file
driver.find_element(By.ID, "uploadFile").send_keys(r"C:\path\to\file.txt")

# Wait example
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "submit")))

# Cleanup
time.sleep(2)
driver.quit()
