import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

s = Service(ChromeDriverManager().install())

from vkcom_pytest.pageObjects.LoginPage import loginPage
from vkcom_pytest.utilities.readproperties import ReadConfig


class Test_001_test_login:

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(service=s)
    #     cls.driver.maximize_window()

    def test_homepage_title(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(ReadConfig.getURL())
        actual_title = self.driver.title
        print(actual_title)
        if actual_title == "Welcome! | VK":
            assert True
        else:
            self.driver.get_screenshot_as_file(r"vkcom_pytest/screenshots/test_homepage_title.png")
            assert False
        self.driver.close()
        self.driver.quit()

    def test_login(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(ReadConfig.getURL())
        self.lp = loginPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.setUsername()
        self.lp.setPassword()
        self.lp.logInn()
        self.lp.topLogout()
        actual_title = self.driver.title
        if actual_title == "Новости":
            assert True
        else:
            assert False
        self.driver.close()
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()
    # print('tests completed')
