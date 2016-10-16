# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class testVK(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_testVK(self):
        success = True
        wd = self.wd
        wd.get("https://vk.com/")
        wd.find_element_by_id("index_email").click()
        wd.find_element_by_id("index_email").clear()
        wd.find_element_by_id("index_email").send_keys("rayalex2007@yandex.ru")
        wd.find_element_by_id("index_pass").click()
        wd.find_element_by_id("index_pass").clear()
        wd.find_element_by_id("index_pass").send_keys("231019887rayalex")
        wd.find_element_by_id("index_expire").click()
        wd.find_element_by_id("index_login_button").click()
        wd.find_element_by_css_selector("span.left_label.inl_bl").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
