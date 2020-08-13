from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os


class Instabot:
    def __init__(self,bot_id,passscode):
        self.bot_id=bot_id
        self.bot_password=passscode

    def getinstagram(self):
        self.PATH="C:\Program Files (x86)\chromedriver"
        print(self.PATH)
        self.url="https://instagram.com"
        self.driver=webdriver.Chrome(self.PATH)
        self.driver.maximize_window()
        self.driver.get(self.url)
        print("Opened the url.")

    def login(self,bot_id,bot_password):
        self.getinstagram()
        time.sleep(3)

        self.username=self.driver.find_element_by_css_selector('input[name="username"]')
        self.password=self.driver.find_element_by_css_selector('input[type="password"]')

        self.username.clear()
        self.password.clear()

        self.username.send_keys(self.bot_id)
        self.password.send_keys(self.bot_password)

        self.login_button=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        self.login_button.click()

        try:
            time.sleep(3)
            self.cancel_saveinfo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
            self.cancel_saveinfo.click()
        except NoSuchElementException:
            pass


        try:
            self.cancel_notification=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            self.cancel_notification.click()
        except NoSuchElementException:
            pass

        print(f'logged in as {self.bot_id}')
    
    def search_user(self,target_id):
        self.target_id=target_id

        self.login(self.bot_id,self.bot_password)
        time.sleep(3)

        self.search_bar=self.driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
        self.search_bar.send_keys(self.target_id)
        self.search_bar.send_keys(Keys.ENTER)

        self.search_icon=self.driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > span')
        self.search_icon.click()
        time.sleep(3)

        self.result_1=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/div/span')
        self.result_1.click()

        print(f'found the user {self.target_id}')

    def like_posts(self,target_id,no_of_posts):
        self.target_id=target_id
        self.no_of_posts=no_of_posts
        self.liked_posts=0

        self.search_user(self.target_id)
        time.sleep(3)

        self.posts=self.driver.find_elements_by_class_name('_9AhH0')
        for self.post in  self.posts:
            self.post.click()
            time.sleep(3)

            try:
                self.like_button=self.driver.find_element_by_css_selector('svg[aria-label="Like"]')
                time.sleep(3)
                self.like_button.click()
                self.liked_posts+=1
                print(f'successfully liked {self.liked_posts} post(s)!')
            except NoSuchElementException:
                try:
                    self.unlike_button=self.driver.find_element_by_css_selector('svg[aria-label="Unlike"]')
                    pass
                except NoSuchElementException:
                    print("Unabel to find the element 👎")
                    self.driver.close()


            self.close_button=self.driver.find_element_by_css_selector('svg[aria-label="Close"]')
            time.sleep(3)
            self.close_button.click()
            time.sleep(3)

            if self.liked_posts >= self.no_of_posts:
                break


if __name__=="__main__":

    BOT_ID=os.environ.get("BOT_ID")
    BOT_PASSWORD=os.environ.get("BOT_PASSWORD")

    bot=Instabot(BOT_ID,BOT_PASSWORD)
    bot.like_posts("hard_code_brain",3)
    bot.driver.close()

    
