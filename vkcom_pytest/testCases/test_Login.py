import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from vkcom_pytest.pageObjects.LoginPage import loginPage
from vkcom_pytest.utilities.readproperties import ReadConfig
from vkcom_pytest.utilities.customLogger import LogGen
from loguru import logger
s = Service(ChromeDriverManager().install())




class Test_001_test_login:



    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(service=s)
    #     cls.driver.maximize_window()

    def test_homepage_title(self):
        LogGen.loggen().info("****************** Test_001_test_login ******************")
        LogGen.loggen().info("****************** Verifying test_homepage_title ******************")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(ReadConfig.getURL())

        actual_title = self.driver.title
        print(actual_title)
        if actual_title == "Welcome! | VK":
            LogGen.loggen().info("****************** test_homepage_title is passed ******************")
            self.driver.close()
            assert True

        else:
            self.driver.get_screenshot_as_file(r"vkcom_pytest/screenshots/test_homepage_title.png")
            LogGen.loggen().error("****************** test_homepage_title is failed ******************")
            self.driver.close()
            assert False


    def test_login(self):
        LogGen.loggen().info("****************** Test_001_test_login ******************")
        LogGen.loggen().info("****************** Verifying test_login ******************")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(ReadConfig.getURL())
        self.lp = loginPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.setUsername()
        self.lp.setPassword()
        self.lp.logInn()
        self.lp.topLogout()
        actual_title = self.driver.title
        if actual_title == "Новос[ти":
            LogGen.loggen().info("****************** test_login is passed ******************")
            self.driver.close()
            assert True
        else:
            LogGen.loggen().error("****************** test_login is failed ******************")
            self.driver.close()
            assert False

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()
    # print('tests completed')
