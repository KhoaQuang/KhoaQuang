import sys,os,time,logging,datetime,unittest,inspect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import re


class Web():
    url=""
    def __init__(self):
        print("Create a object website")
        # self.url=url
    def prepare_webdriver(self):
        # print('Webdriver is ready')
        # profile_temp = webdriver.ChromeOptions()
        # profile_temp.accept_untrusted_cert = True
        # profile_temp.add_argument("--lang=en")
        # profile_temp.add_argument("--disable-application-cache")
        # profile_temp.add_argument("start-maximized")
        # self.cap = profile_temp.to_capabilities()
        # self.cap['goog:loggingPrefs'] = { 'browser':'ALL' }
        # self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=self.cap)    
        # options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome()
        print('Webdriver is ready')
        # options.accept_untrusted_cert = True # type: ignore
        # options.add_argument("--lang=en")
        # options.add_argument("--disable-application-cache")
        # options.add_argument("start-maximized")
        # self.cap = options.to_capabilities()
        self.driver.maximize_window()
        # self.cap['goog:loggingPrefs'] = { 'browser':'ALL' }
        # self.driver = webdriver.Remote(command_executor='http://10.102.1.25:4444/wd/hub',desired_capabilities=self.cap)    
        print('Webdriver was created')
        return True
    def launch_browser(self, url):
        print('Start launch_browser')
        self.prepare_webdriver()
        self.driver.get(url)
        time.sleep(5)
        print('End launch_browser')
        return True
    def title_mywebsite(self):
        # title_web = "My Store"
        # expected_title = "Example Domain"
        expected_title = "What is a Java Backend Developer?"
        # self.driver.get(self.url)
        title_current = self.driver.title
        # if title_current == title_web: 
        #     time.sleep(3)
        #     print("Welcome to My Website: " + title_current)
        #     return True
        # else:
        #     assert('Goto %s failed,please check network'% self.url)
        #     print("Invalid")
        #     return False
        if title_current == expected_title:
            time.sleep(5)
            print("Titles match!")
            return True
        else:
            print("Don't match")
            return ("Expected title: {expected_title}, Actual title: {title_current}")
        
    def signin(self, username, password):
        Username = self.driver.find_element(By.CSS_SELECTOR,"input[id='loginForm:username']")
        Username.clear()     
        Username.send_keys(username)
        print('Input Username')   
        time.sleep(3)
        Password = self.driver.find_element(By.CSS_SELECTOR,"input[id='loginForm:password']")
        Password.clear()     
        Password.send_keys(password)
        print('Input Password')
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,"span[id='loginForm:submitText']").click()
        print('Click button Sign In')
        time.sleep(5)

    def signout(self):
        self.driver.find_element(By.ID,"logoutForm:log_out").click()
        print('Click button Sign Out')
        time.sleep(5)
        
    def get_download(self):
        title_element = self.driver.find_element(By.CSS_SELECTOR,"li[id='downloads']")
        title_element.click()
        time.sleep(3)
        print("Click element successfully!")

    def perform_action(self):
        # Thực hiện một hành động nào đó (ví dụ: click, nhập liệu, ...)
        print("Đã thực hiện hành động!")

    def close_browser(self):
        print("Đóng browser")
        time.sleep(10)
        self.driver.quit()
        
# # web1 = Web("https://www.example.com/")
# web1 = Web("https://www.tealhq.com/career-paths/java-backend-developer")
# web1.launch_browser()
# web1.title_mywebsite()
# # web1.get_download()
# web1.close_browser()
