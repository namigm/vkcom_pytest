import pytest
from vkcom_pytest.pageObjects.LoginPage import loginPage
from vkcom_pytest.utilities.readproperties import ReadConfig
from vkcom_pytest.utilities.customLogger import LogGen


class Test_001_test_login:
    logger = LogGen.loggen()

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(service=s)
    #     cls.driver.maximize_window()

    def test_homepage_title(self, setup):
        self.logger.info("****************** Test_001_test_login ******************")
        self.logger.info("****************** Verifying test_homepage_title ******************")
        self.driver = setup
        self.driver.get(ReadConfig.getURL())

        actual_title = self.driver.title
        print(actual_title)
        if actual_title == "Welcome! | VK":
            self.logger.info("****************** test_homepage_title is passed ******************")
            self.driver.close()
            assert True

        else:
            self.driver.get_screenshot_as_file(r"vkcom_pytest/screenshots/test_homepage_title.png")
            self.logger.error("****************** test_homepage_title is failed ******************")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("****************** Test_001_test_login ******************")
        self.logger.info("****************** Verifying test_login ******************")
        self.driver = setup
        self.driver.get(ReadConfig.getURL())
        self.lp = loginPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.setUsername()
        self.lp.setPassword()
        self.lp.logInn()
        self.lp.topLogout()
        actual_title = self.driver.title
        if actual_title == "Новости":
            self.logger.info("****************** test_login is passed ******************")
            self.driver.close()
            assert True
        else:
            self.logger.error("****************** test_login is failed ******************")
            self.driver.close()
            assert False

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()
    # print('tests completed')
