import time
from vkcom_pytest.locators.Locators_main import Locators
from vkcom_pytest.testData.authdata import authdata
from selenium.webdriver.common.by import By


class loginPage:
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, Locators.indexEmail_id).clear()
        self.driver.find_element(By.ID, Locators.indexEmail_id).send_keys(authdata.vk_login)

    def setPassword(self):
        self.driver.find_element_by_id(Locators.indexPassword_id).clear()
        self.driver.find_element_by_id(Locators.indexPassword_id).send_keys(authdata.vk_password)

    def logInn(self):
        self.driver.find_element_by_id(Locators.signinButton_id).click()

    def topLogout(self):
        self.driver.find_element_by_css_selector(Locators.topProfileMenu_css).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.topLogoutButton_xpath).click()
