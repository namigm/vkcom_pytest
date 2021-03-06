import pytest
from pageObjects.LoginPage import loginPage
from pageObjects.ChangeUserInfo import changeUserInfo
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from locators.Locators_main import Locators
from selenium.webdriver.common.by import By


class Test_003_change_user_info:
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.uat
    def test_change_user_info(self, setup):
        self.logger.info("****************** Test_003_change_user_info ******************")
        self.logger.info("****************** Verifying change_user_info ******************")
        self.driver = setup
        self.driver.get(ReadConfig.getURL())
        self.lp = loginPage(self.driver)
        self.ci = changeUserInfo(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.setUsername(ReadConfig.vk_login())
        self.lp.setPassword(ReadConfig.vk_password())
        self.lp.logInn()
        self.ci.goMyPage()
        self.ci.profileEdit()
        self.ci.setFamilyStatus(Locators.fsDating_id)
        self.ci.setBirthday(Locators.bd5_id, Locators.bmMarch_id, Locators.by1990_id)
        self.ci.setLanguageSkill(Locators.addAzLang_xpath)
        self.ci.saveChangesInfo()
        self.msg = self.driver.find_element(By.CLASS_NAME, 'msg_text').text
        if "Изменения сохранены" in self.msg:
            self.logger.info("****************** Test_003_change_user_info is passed ******************")
            assert True
        else:
            self.logger.error("****************** Test_003_change_user_info is failed ******************")
            self.driver.get_screenshot_as_file(r"vkcom_pytest/screenshots/test_change_User_info.png")
            assert False
        self.logger.info("****************** Test_003_change_user_info is completed ******************")
        self.driver.close()
        self.driver.quit()
