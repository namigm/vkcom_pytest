import time
from vkcom_pytest.locators.Locators_main import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class findUser:
    def __init__(self, driver):
        self.driver = driver

    def clickLeftMenuFriends(self):
        self.driver.find_element(By.ID, Locators.leftMenuFriends_id).click()

    def clickFindFriendBtn(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, Locators.bFindFriends_id).click()

    def setSearchData(self, input_data):
        time.sleep(3)
        self.driver.find_element(By.ID, Locators.topSearch_id).send_keys(input_data)
        time.sleep(1)
        self.driver.find_element(By.ID, Locators.topSearch_id).send_keys(Keys.ENTER)
        time.sleep(2)

    def clickFilterExpand(self):
        self.driver.find_element(By.XPATH, Locators.searchFilterExpand_xpath).click()

    def setCountry(self, country):
        self.driver.find_element(By.XPATH, Locators.regionFilter_xpath).click()
        time.sleep(1)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, f'//li[@title={country}]')).click().perform()
        time.sleep(2)

    def setOnlineNowFilter(self):
        self.driver.find_element(By.XPATH, Locators.setOnlineNowFilter_xpath).click()

    def finalUserCount(self):
        count = self.driver.find_element(By.XPATH, Locators.finalUserCount_xpath).text.replace(' ',
                                                                                               '')
        return count

    def foundUser(self, r):
        return self.driver.find_element(By.XPATH, f'//*[@id="results"]/div[{r}]/div[3]/div[1]/a').text
