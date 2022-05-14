import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "D:\python\Selenium\POMProjectDemo\Pages", "D:\python\Selenium\POMProjectDemo\Locators"))
from Locators import locators


class lastpost():
    def __init__(self, driver):
        self.driver = driver
        self.myPage_xpath = locators.myPage_xpath
        self.lastPost_xpath = locators.lastPost_xpath

    def gomypage(self):
        self.driver.find_element_by_xpath(self.myPage_xpath).click()
        

    def lastpost(self):
        self.driver.find_element_by_xpath(self.lastPost_xpath)

    
        
    




