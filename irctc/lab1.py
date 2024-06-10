from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace 'path_to_chromedriver' with the actual path to the ChromeDriver executable
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Open IRCTC website
driver.get("https://www.irctc.co.in/")

# Wait for the page to load and elements to become available
wait = WebDriverWait(driver, 10)

# Click on the login button
login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "LOGIN")))
login_button.click()

# Enter username
username_field = wait.until(EC.presence_of_element_located((By.ID, "userId")))
username_field.send_keys("Devendrajjw")

# Enter password
password_field = driver.find_element(By.ID, "pwd")
password_field.send_keys("your_password")

# Enter CAPTCHA manually or use an OCR service if applicable
captcha_field = driver.find_element(By.ID, "captchaImg")
captcha = input("Please enter CAPTCHA: ")  # In a real scenario, handle CAPTCHA with OCR or manually
captcha_field.send_keys(captcha)

# Click on sign-in button
sign_in_button = driver.find_element(By.ID, "loginbutton")
sign_in_button.click()

# Add delay to account for login process (use explicit waits instead if possible)
time.sleep(5)

# Navigate to booking section and fill out booking form
# This is a simplified example; adapt selectors and actions as needed
# Source station
source_field = wait.until(EC.presence_of_element_located((By.ID, "origin")))
source_field.send_keys("Source_Station")
source_field.send_keys(Keys.RETURN)

# Destination station
destination_field = driver.find_element(By.ID, "destination")
destination_field.send_keys("Destination_Station")
destination_field.send_keys(Keys.RETURN)

# Date of journey
date_field = driver.find_element(By.ID, "jDate")
date_field.send_keys("Date_in_DD-MM-YYYY")

# Submit the form to search for trains
search_button = driver.find_element(By.ID, "search_btn")
search_button.click()

# Handle the booking process based on the available trains and classes
# This part needs to be adapted based on the actual flow and available options

# Remember to close the browser at the end
driver.quit()
