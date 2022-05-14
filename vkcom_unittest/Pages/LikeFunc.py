import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "D:\python\Selenium\POMProjectDemo\Pages", "D:\python\Selenium\POMProjectDemo\Locators"))
from Locators import locators


class likefunc():
    def __init__(self, driver):
        self.driver = driver
        self.likeCount_xpath = locators.likeCount_xpath
        self.likeButton_selector = locators.likeButton_selector
        

    def likefunctional(self):
        initialLikecount = int((self.driver.find_element_by_xpath(self.likeCount_xpath).text).split()[1])
        # print(initialLikecount)
        # print(self.driver.find_element_by_xpath(self.likeCount_xpath).get_attribute('aria-label'))
        if  self.driver.find_element_by_xpath(self.likeCount_xpath).get_attribute('aria-label') == 'Убрать реакцию «Нравится»':
            self.driver.find_element_by_css_selector(self.likeButton_selector).click()
            finalLikecount = initialLikecount - 1
            tc = unittest.TestCase()
            tc.assertEqual(initialLikecount-1,finalLikecount, 'Like functionality is not working')
        else:
            self.driver.find_element_by_css_selector(self.likeButton_selector).click()
            finalLikecount = initialLikecount + 1
            tc = unittest.TestCase()
            tc.assertEqual(initialLikecount + 1,finalLikecount, 'Like functionality is not working')


        
    
    
    


        