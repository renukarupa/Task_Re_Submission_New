from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the Instagram profile page
driver.get("https://www.instagram.com/guvioffical/")

# Wait for the page to load
time.sleep(5)

# Define the XPath and commands for various tasks
profile_picture_xpath = '//*[@id="react-root"]/section/main/div/header/div/div/span/img'
profile_picture = driver.find_element(By.XPATH, profile_picture_xpath)

# Find the username path
username_xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/h2'
username = driver.find_element(By.XPATH, username_xpath)

# Find the follower count
followers_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'
followers = driver.find_element(By.XPATH, followers_xpath)

# Print out the information
print("Profile Picture URL:", profile_picture.get_attribute('src'))
print("Username:", username.text)
print("Followers:", followers.get_attribute('title'))

# Close the browser
driver.quit()
