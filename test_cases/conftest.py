import pytest
from selenium import webdriver
import undetected_chromedriver as uc
import warnings
from page_objects.login_page import Login
warnings.filterwarnings("ignore")


@pytest.fixture()
def setup_driver(request):
    driver = uc.Chrome()
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com/")
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


@pytest.fixture()
def setup_login(request):
    driver = uc.Chrome()
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com/")
    request.cls.driver = driver
    login = Login(driver)
    login.set_username("admin@yourstore.com")
    login.set_password("admin")
    login.click_login()
    yield
    driver.close()
    driver.quit()
