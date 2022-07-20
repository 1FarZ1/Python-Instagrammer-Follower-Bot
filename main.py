from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from obj import InstaFollower
EMAIL=UR_EMAIL
PASSWORD=UR_PASSWORD
target=UR_TARGET
chrome_driver_path="C:\chrome\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
fares=InstaFollower(driver)
fares.login()
fares.find_followers()
# fares.follow()
