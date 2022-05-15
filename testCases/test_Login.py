import pytest
from pageObjects.LoginPage import loginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_001_test_login:
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("****************** Test_001_test_login/homepage_title ******************")
        self.logger.info("****************** Verifying test_homepage_title ******************")
        self.driver = setup
        self.driver.get(ReadConfig.getURL())

        actual_title = self.driver.title
        if actual_title == "Welcome! | VK":
            self.logger.info("****************** Test_001_test_login/test_homepage_title is passed ******************")
            self.logger.info("****************** Test_001_test_login/homepage_title is completed ******************")
            self.driver.close()
            assert True

        else:
            self.driver.get_screenshot_as_file(r"vkcom_pytest/screenshots/test_homepage_title.png")
            self.logger.error("****************** test_homepage_title is failed ******************")
            self.logger.info("****************** Test_001_test_login/homepage_title is completed ******************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.uat
    @pytest.mark.test
    def test_login(self, setup):
        self.logger.info("****************** Test_001_test_login/test_login ******************")
        self.logger.info("****************** Verifying test_login/test_login ******************")
        self.driver = setup
        self.driver.get(ReadConfig.getURL())
        self.lp = loginPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.setUsername(ReadConfig.vk_login())
        self.lp.setPassword(ReadConfig.vk_password())
        self.lp.logInn()
        time.sleep(2)
        actual_title = self.driver.title
        if actual_title == "Новости":
            self.lp.topLogout()
            self.logger.info("****************** Test_001_test_login/test_login is passed ******************")
            self.logger.info("****************** Test_001_test_login/test_login is completed ******************")
            self.driver.close()
            assert True
        else:
            self.logger.error("****************** Test_001_test_login/test_login is failed ******************")
            self.logger.info("****************** Test_001_test_login/test_login is completed ******************")
            self.lp.topLogout()
            self.driver.close()
            assert False
