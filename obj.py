from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
EMAIL=UR_EMAIL
PASSWORD=UR_PASSWORD
target=UR_TARGET
class InstaFollower():
    def __init__(self,driver):
        self.driver=driver
    def login(self):
        self.driver.get("https://www.instagram.com")
        sleep(2)
        username=self.driver.find_element(By.NAME,value="username")
        username.send_keys(EMAIL)
        password=self.driver.find_element(By.NAME,value="password")
        password.send_keys(PASSWORD,Keys.ENTER)
        sleep(10)
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{target}")
        sleep(5)
        button_f=self.driver.find_element(By.XPATH,value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a')
        button_f.click()
        sleep(2)
        page = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]')
        for char in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", page)
            sleep(2)
    def follow(self):
        all_buttons=self.driver.find_element_by_css_selector("li button")
        for btn in all_buttons:
            if btn.text=="Follow":
                btn.click()
                sleep(1)
            else:
                dislike=self.driver.find_element(by=By.LINK_TEXT,value="reject")
                print("already followed")
                sleep(1)
