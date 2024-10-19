from pages.passengers_page import PassengersPage
from libs.base_page import BasePage

import time

class PriceFlow(PassengerPage):
    def __init__(self, driver):
        super().__init__()
        self.page = BasePage(driver)
        self.driver = driver

    def wait_for_new_page(self):
        time.sleep(5)
        print(f"Redirigido a la página")
    
    def validate_http_status(self, url):
        status_code = self.page.get_status_code(url)
        assert status_code == 200, f"HTTP Error: status code {status_code}"

    def select_basic_price(self):
        self.page.click_element(self.OPTION_PRICE_BUTTON)
        self.page.click_element(self.SELECT_PRICE_BUTTON)
        self.validate_http_status(self.driver.current_url)
        print('basic price')
  