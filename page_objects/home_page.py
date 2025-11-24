from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    link_order_moreinfo_xpath = "//a[@class='small-box-footer' and contains(@href, 'Order')]"
    link_return_request_xpath = "//a[@class='small-box-footer' and contains(@href, 'ReturnRequest')]"
    link_registered_customers_xpath = "//a[@class='small-box-footer' and contains(@href, 'Customer')]"
    link_low_stock_xpath = "//a[@class='small-box-footer' and contains(@href, 'LowStock')]"

    def click_link_text(self, link_text):
        self.driver.find_element(By.XPATH, link_text).click()


