from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Instagram profile page
driver.get("https://www.instagram.com/guvioffical/")
time.sleep(5)  # Wait for the page to load

# XPath for followers and following
followers_xpath = '//ul/li[2]/a/div/span'
following_xpath = '//ul/li[3]/a/div/span'

# Extract the number of followers
followers_element = driver.find_element(By.XPATH, followers_xpath)
followers = followers_element.get_attribute("title")

# Extract the number of following
following_element = driver.find_element(By.XPATH, following_xpath)
following = following_element.text

print(f"Followers: {followers}")
print(f"Following: {following}")

# Close the WebDriver
driver.quit()
