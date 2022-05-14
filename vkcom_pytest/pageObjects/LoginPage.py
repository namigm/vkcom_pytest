import time
from locators.Locators_main import Locators
from selenium.webdriver.common.by import By


class loginPage:
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, Locators.accessLogin_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, Locators.subEmail_name).clear()
        self.driver.find_element(By.NAME, Locators.subEmail_name).send_keys(username)
        self.driver.find_element(By.XPATH, Locators.usernameSub_xpath).click()


    def setPassword(self, password):
        self.driver.find_element(By.NAME, Locators.subPassword_name).clear()
        self.driver.find_element(By.NAME, Locators.subPassword_name).send_keys(password)



    def logInn(self):
        self.driver.find_element(By.XPATH, Locators.loginSub_xpath).click()

    def topLogout(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.topProfileMenu_css).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, Locators.topLogoutButton_id).click()

    def topHomeLinkSmall(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.topHomeLink_small_css).click()
        time.sleep(2)

    def topHomeLinkBig(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.topHomeLink_big_css).click()
        time.sleep(2)
