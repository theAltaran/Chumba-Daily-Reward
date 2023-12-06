from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

# Load variables from the .env file
load_dotenv()

# Get the username and password from the environment variables
username = os.getenv("CHUMBA_USERNAME")
password = os.getenv("CHUMBA_PASSWORD")

# URL of the login page
login_url = "https://login.chumbacasino.com/"

# Create a new instance of the Firefox driver (you can use other browsers as well)
driver = webdriver.Firefox()

try:
    # Open the login page
    driver.get(login_url)

    # Find the username, password, and login button elements using their IDs or other attributes
    username_field = driver.find_element(By.ID, "login_email-input")
    password_field = driver.find_element(By.ID, "login_password-input")
    login_button = driver.find_element(By.ID, "login_submit-button")

    # Input username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click the login button
    login_button.click()

    # Wait for 5 seconds after logging in
    time.sleep(5)

    # Find and click the "daily-bonus__claim-btn" element
    claim_button = driver.find_element(By.ID, "daily-bonus__claim-btn")
    claim_button.click()

    # Wait for 5 seconds after claiming the bonus
    time.sleep(5)

finally:
    # Close the browser window
    driver.quit()
