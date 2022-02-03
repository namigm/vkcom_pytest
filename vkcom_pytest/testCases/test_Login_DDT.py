import pytest
from vkcom_pytest.pageObjects.LoginPage import loginPage
from vkcom_pytest.utilities.readproperties import ReadConfig
from vkcom_pytest.utilities.customLogger import LogGen
from vkcom_pytest.utilities import XLUtils
import time


class Test_002_test_login_DDT:
    logger = LogGen.loggen()
    path = r"C:\Selenium\vkcom\vkcom_pytest\testData\loginData.xlsx"
    expected_title = "Новости"

    def test_login(self, setup):
        self.logger.info("****************** Test_002_test_login_DDT ******************")
        self.logger.info("****************** Verifying test_login_DDT ******************")
        self.driver = setup
        self.driver.get(ReadConfig.getURL())
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.lp = loginPage(self.driver)
        result_list = []

        for r in range(2, self.rows+1):
            self.vk_username = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.vk_password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.er = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUsername(self.vk_username)
            self.lp.setPassword(self.vk_password)
            self.lp.logInn()
            time.sleep(10)

            self.actual_title = self.driver.title

            if self.actual_title == self.expected_title:
                if self.er == 'Pass':
                    result_list.append('Passed')
                    self.logger.info(f"****************** Passed_DDT_value {self.vk_username} ******************")
                    self.lp.topLogout()
                    time.sleep(3)
                    self.lp.topHomeLinkBig()
                elif self.er == 'Fail':
                    result_list.append('Failed')
                    self.logger.info(f"****************** Failed_DDT_value {self.vk_username} ******************")
                    self.lp.topLogout()
                    self.lp.topHomeLinkBig()
            elif self.actual_title != self.expected_title:
                if self.er == 'Pass':
                    result_list.append('Failed')
                    self.logger.info(f"****************** Failed_DDT_value {self.vk_username} ******************")
                    if "Passed" in result_list:
                        self.lp.topHomeLinkBig()
                    else:
                        self.lp.topHomeLinkSmall()

                elif self.er == 'Fail':
                    result_list.append('Passed')
                    self.logger.info(f"****************** Passed_DDT_value {self.vk_username} ******************")
                    if "Passed" in result_list:
                        self.lp.topHomeLinkBig()
                    else:
                        self.lp.topHomeLinkSmall()

        if 'Failed' not in result_list:
            self.logger.info("****************** Test_002_test_login_DDT is passed ******************")
            self.driver.close()
            assert True

        else:
            self.logger.info("****************** Test_002_test_login_DDT is failed ******************")
            self.driver.close()
            assert False

        self.logger.info("****************** Test_002_test_login_DDT is completed ******************")

