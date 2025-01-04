from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace with the GlobeOne web login URL
globe_url = "https://www.globe.com.ph/globeone.html"

# Set up WebDriver
driver = webdriver.Chrome()  # Or the WebDriver for your browser
driver.get(globe_url)

# Log in to your GlobeOne account
try:
    phone_number_field = driver.find_element(By.NAME, "phoneNumber")  # Update selector as needed
    phone_number_field.send_keys("numbr")

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Wait for OTP entry
    otp_field = driver.find_element(By.NAME, "otp")
    otp = input("Enter the OTP sent to your phone: ")
    otp_field.send_keys(otp)
    otp_field.send_keys(Keys.RETURN)

    time.sleep(5)  # Allow time for the page to load

    # Navigate to the balance section
    balance_element = driver.find_element(By.CLASS_NAME, "balance-text")  # Update selector as needed
    print(f"Remaining balance: {balance_element.text}")
finally:
    driver.quit()
