from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):

        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        username_box = driver.find_element_by_xpath("//input[@name='username']")
        password_box = driver.find_element_by_xpath("//input[@name='password']")
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.ENTER)
        time.sleep(10)
        #powiadomienia_button= driver.find_element_by_class_name("/html/body/div[3]/div/div/div[3]/button[2]")
        #powiadomienia_button.click()
        #powiadomienia_button.click()
        driver.find_element_by_xpath('//button[text()="Nie teraz"]').click()

    def Liking(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(2)
        for i in range(1, 4):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        #wyszukiwanie linkow
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + ' photos ' + str(len(pic_hrefs)))
        i = 1

        for pic in pic_hrefs:
            driver.get(pic)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                driver.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
                print('Zalajkowalem foto' + pic)
                time.sleep(random.randint(5, 30))
            except Exception as e:
                time.sleep(3)

username = 'username'
password = 'password'


OloIG = InstagramBot(username, password)
OloIG.login()

#OloIG.Liking('trekking')
OloIG.Liking('polishphotocommunity')
OloIG.Liking('warszawa')
OloIG.Liking('LANDSCAPE')
