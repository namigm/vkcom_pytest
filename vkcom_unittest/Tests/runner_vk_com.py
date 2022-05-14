from selenium import webdriver
import time
import unittest

# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "C:\Users\99455\Desktop\Automation\Selenium\vkcom\vkcom_automation\Tests", "C:\Users\99455\Desktop\Automation\Selenium\vkcom\vkcom_automation\Pages"))

from vkcom_automation.Pages.LoginPage import loginpage
from vkcom_automation.Pages.LoginPage import lastpost
from vkcom_automation.Pages.LoginPage import likefunc


class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='D:\python\Selenium\chrome_driver\chromedriver.exe')#, options = webdriver.ChromeOptions())
        #options.add_experimental_option('excludeSwitches', ['enable-logging'])
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
    

    def test_01_login_valid(self):
        driver = self.driver
        driver.get('https://vk.com/')
        login = loginpage(driver)
        login.enter_user_name()
        login.enter_user_password()
        login.login_button()

    def test_02_last_post(self):
        driver = self.driver
        post = lastpost(driver)
        post.gomypage()
        post.lastpost()

    def test_03_like_functional(self):
        driver = self.driver
        post = likefunc(driver)
        post.likefunctional()
      

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test completed')

if __name__ == '__main__':
    unittest.main()


    
        


        





