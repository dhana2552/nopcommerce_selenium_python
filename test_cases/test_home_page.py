import pytest
from page_objects.home_page import HomePage
from time import sleep

@pytest.mark.usefixtures("setup_login")
class TestHomePage:
    def test_common_statistics(self):
        home_page = HomePage(self.driver)
        home_page.click_link_text(home_page.link_order_moreinfo_xpath)
        sleep(5)