from pages.price_page import PricePage
from libs.base_page import BasePage
from libs.base_object import BaseFlow

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

import time
import allure

class PriceFlow(PricePage):
    def __init__(self, driver):
        super().__init__()
        self.page = BasePage(driver)
        self.object = BaseFlow(driver)
        self.driver = driver
    
    @allure.step("Basic price option Verification")
    def select_basic_price(self):
        is_fly_button_present = self.page.click_element_wait(self.FLY_BUTTON)
        if not is_fly_button_present:
            raise NoSuchElementException(f"The one-way trip flight option is not visible or does not exist.")
            
        self.page.click_element(self.FLY_BUTTON)
        self.page.click_element(self.BASIC_PRICE_BUTTON)
        self.object.validate_http_status(self.driver.current_url)
        print('basic price')
    
    @allure.step("Flex price option Verification")
    def select_flex_price(self):
        try:
            is_fly_button_present = self.page.click_element_wait(self.FLY_BUTTON)
            if not is_fly_button_present:
                raise NoSuchElementException(f"The round trip flight option is not visible or does not exist.")
                
            self.page.click_element(self.FLY_BUTTON)
            self.page.click_element(self.FLEX_PRICE_BUTTON)
            self.object.validate_http_status(self.driver.current_url)
            
            allure.attach(self.driver.get_screenshot_as_png(), name="Flex price verification", attachment_type=allure.attachment_type.PNG)
            print(f"The Flex option loaded correctly")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error verification: {str(e)}")
    
    
    def validate_type_fly(self, fly):                
        if fly == 'Ida':
            self.select_basic_price() 
        else:
            self.select_flex_price()
    
    @allure.step("Flight Verification")    
    def select_continue(self):
        try:
            self.page.click_element(self.CONTINUE_BUTTON)
            self.object.validate_http_status(self.driver.current_url)
            
        except ElementNotInteractableException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="ElementNotInteractableException screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"The element is not interactive or not enabled to continue with flight options.")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error interacting with the element: {e.msg}")
            