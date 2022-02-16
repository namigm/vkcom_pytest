import pytest
from vkcom_pytest.pageObjects.LoginPage import loginPage
from vkcom_pytest.utilities.readproperties import ReadConfig
from vkcom_pytest.utilities.customLogger import LogGen
from vkcom_pytest.pageObjects.FindUser import findUser


class Test_004_find_user:
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.uat
    def test_find_user(self, setup):
        self.logger.info("****************** Test_004_find_user ******************")
        self.logger.info("****************** Verifying find_user function ******************")
        self.driver = setup
        self.driver.get(ReadConfig.getURL())
        self.lp = loginPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.setUsername(ReadConfig.vk_login())
        self.lp.setPassword(ReadConfig.vk_password())
        self.lp.logInn()
        self.fu = findUser(self.driver)
        self.fu.clickLeftMenuFriends()
        self.fu.clickFindFriendBtn()
        self.fu.clickFilterExpand()
        self.fu.setCountry('\'Азербайджан\'')
        self.fu.setOnlineNowFilter()
        self.fu.setSearchData("Ali")
        self.logger.info(f"****************** Test_004_found {int(self.fu.finalUserCount())} users ******************")
        for r in range(1, int(self.fu.finalUserCount()) + 1):
            self.flag = True
            found_user = self.fu.foundUser(r)
            if 'Ali' not in found_user and 'Али' not in found_user:
                self.flag = False
            break
        if self.flag is False:
            self.logger.error("****************** Test_004_find_user is failed ******************")
            self.driver.get_screenshot_as_file(r"vkcom_pytest/screenshots/find_user.png")
            self.logger.info("****************** Test_004_find_user is completed ******************")
            self.driver.close()
            self.driver.quit()
            assert False

        else:
            self.logger.info("****************** Test_004_find_user is passed ******************")
            self.logger.info("****************** Test_004_find_user is completed ******************")
            self.driver.close()
            self.driver.quit()
            assert True


