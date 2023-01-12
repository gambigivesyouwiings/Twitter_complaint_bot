from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import tweepy

path = "Get the executable file path on your computer by downloading Selenium package online"
consumer_key = 'Get the following four variables by visiting the twitter developer API'
consumer_secret = "xxxxxx"
access_token = 'xxxxx'
access_token_secret = 'xxxxxxxx'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class InternetSpeedTwitterBot:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service=service, options=options)
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        print(go_button.text)
        go_button.click()
        time.sleep(200)
        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(download_speed)
        print(upload_speed)
        self.driver.close()

        return [download_speed, upload_speed]

    def text_provider(self, down, up):
        self.api.update_status(status=f"Zuku perfomance update: My download speed is {down} mbps, and my upload speed is {up} mbps,yet my current subscription is 10Mbps")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
