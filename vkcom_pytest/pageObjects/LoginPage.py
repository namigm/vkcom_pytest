import time
from vkcom_pytest.locators.Locators_main import Locators
from selenium.webdriver.common.by import By


class loginPage:
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, Locators.indexEmail_id).clear()
        self.driver.find_element(By.ID, Locators.indexEmail_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, Locators.indexPassword_id).clear()
        self.driver.find_element(By.ID, Locators.indexPassword_id).send_keys(password)

    def logInn(self):
        self.driver.find_element(By.ID, Locators.signinButton_id).click()

    def topLogout(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.topProfileMenu_css).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators.topLogoutButton_xpath).click()

    def topHomeLinkSmall(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.topHomeLink_small_css).click()
        time.sleep(2)

    def topHomeLinkBig(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.topHomeLink_big_css).click()
        time.sleep(2)
