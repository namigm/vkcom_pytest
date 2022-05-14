import unittest
import time
import sys
import os

from selenium import webdriver
sys.path.append(os.path.join(os.path.dirname(__file__), "D:\python\Selenium\POMProjectDemo\Pages", "D:\python\Selenium\POMProjectDemo\Locators"))
from Locators import locators

from auth_data import vk_password,vk_login


class loginpage():
    def __init__(self, driver):
        self.driver = driver
        self.index_email_id = locators.index_email_id
        self.index_pass_id = locators.index_pass_id
        self.loginButton_id = locators.loginButton_id
        
        

    def enter_user_name(self):
        self.driver.find_element_by_id(self.index_email_id).clear()
        self.driver.find_element_by_id(self.index_email_id).send_keys(vk_login)
        

    def enter_user_password(self):
        self.driver.find_element_by_id(self.index_pass_id).clear()
        self.driver.find_element_by_id(self.index_pass_id).send_keys(vk_password)
        

    def login_button(self):
        self.driver.find_element_by_id(self.loginButton_id).click()
        



