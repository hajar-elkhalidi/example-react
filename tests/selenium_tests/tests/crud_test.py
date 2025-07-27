import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from selenium_tests.utils.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

from dotenv import load_dotenv
load_dotenv("utils/.env_test")

class TestCrud(BaseTest):
    # Test case for creating a todo item
    def test_create_todo(self):
        self.driver.get(os.getenv('URL'))
        self.driver.find_element(By.ID, "email").send_keys(os.getenv('VALID_EMAIL'))
        self.driver.find_element(By.ID, "password").send_keys(os.getenv('VALID_PASSWORD'))
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # Create a new todo
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter task title...']").send_keys(f"Task item #{current_datetime}")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        assert "Todo created successfully!" in self.driver.page_source

    # # Test case for updating a todo item
    # def test_update_todo(self):
    #     self.test_create_todo()
    #     self.driver.find_element(By.XPATH, "//div[2]/div/div/button").click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div/div/div/div[3]/div[2]/div/div/div/div/input").clear()
    #     #aa      
    #     self.driver.find_element(By.XPATH, "//div[@id='root']/div/div/div/div[3]/div[2]/div/div/div/div/input").send_keys("Updated Task")
    #     self.driver.find_element(By.XPATH, "//div[2]/div/div/div/div/button").click()
    #     time.sleep(2)

    #     assert "Todo updated successfully!" in self.driver.page_source

    # Test case for deleting a todo item
    def test_delete_todo(self):
        self.test_create_todo()
        self.driver.find_element(By.CSS_SELECTOR, "button.bg-destructive").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Delete']").click()
        time.sleep(2)

        assert "Todo deleted successfully!" in self.driver.page_source