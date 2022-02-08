import time
from vkcom_pytest.locators.Locators_main import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from vkcom_pytest.utilities.customLogger import LogGen


class changeUserInfo:
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def goMyPage(self):
        self.driver.find_element(By.ID, Locators.mainPage_id).click()

    def profileEdit(self):
        self.driver.find_element(By.ID, Locators.profileEdit_id).click()

    def setFamilyStatus(self, f_status):
        self.driver.find_element(By.CSS_SELECTOR, Locators.fsField_css).click()
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.ID, f_status)).click().perform()

    def setBirthday(self, b_day, b_month, b_year):
        self.driver.find_element(By.CSS_SELECTOR, Locators.bdField_css).click()
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.ID, b_day)).click().perform()
        self.driver.find_element(By.CSS_SELECTOR, Locators.bmField_css).click()
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.ID, b_month)).click().perform()
        self.driver.find_element(By.CSS_SELECTOR, Locators.byField_css).click()
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.ID, b_year)).click().perform()

    def setLanguageSkill(self, add_language):
        if len(self.driver.find_elements(By.ID, Locators.ruLanguage_id)) > 0:
            self.driver.find_element(By.XPATH, Locators.delRusLang_id).click()
            self.logger.info("****************** Test_003_Rus_language_is_removed from skills ******************")
        if len(self.driver.find_elements(By.ID, Locators.azLanguage_id)) > 0:
            self.driver.find_element(By.XPATH, Locators.delAzLang_id).click()
            self.logger.info("****************** Test_003_Aze_language_is_removed from skills  ******************")
        self.driver.find_element(By.CSS_SELECTOR, Locators.langField_css).click()
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH, add_language)).click().perform()

    def saveChangesInfo(self):
        self.driver.find_element(By.XPATH, Locators.bSaveProfInfo).click()
