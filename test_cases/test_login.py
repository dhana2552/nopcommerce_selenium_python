import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from page_objects.login_page import Login

@pytest.mark.usefixtures("setup_driver")
class TestLoginPage:

    def test_login_page(self):
        login = Login(self.driver)
        login.set_username("admin@yourstore.com")
        login.set_password("admin")
        login.click_login()
        sleep(5)
        logout = self.driver.find_elements(By.XPATH, "//*[text()='Logout']")
        assert len(logout) > 0, "Not a successful login page"
        sleep(2)
