import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from selenium_tests.utils.base_test import BaseTest
from selenium.webdriver.common.by import By
import time

from dotenv import load_dotenv
load_dotenv("utils/.env_test")

class TestLogin(BaseTest):
    def test_valid_login(self):
        self.driver.get(os.getenv('URL'))
        self.driver.find_element(By.ID, "email").send_keys(os.getenv('VALID_EMAIL'))
        self.driver.find_element(By.ID, "password").send_keys(os.getenv('VALID_PASSWORD'))
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        assert "Todo Manager" in self.driver.page_source
    
    def test_invalid_login(self):
        self.driver.get(os.getenv('URL'))
        self.driver.find_element(By.ID, "email").send_keys(os.getenv('INVALID_EMAIL'))
        self.driver.find_element(By.ID, "password").send_keys(os.getenv('INVALID_PASSWORD'))
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        assert "Invalid credentials" in self.driver.page_source