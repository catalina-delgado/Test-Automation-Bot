from pages.price_page import PricePage
from libs.base_page import BasePage

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

import time
import allure

class PriceFlow(PricePage):
    def __init__(self, driver):
        super().__init__()
        self.page = BasePage(driver)
        self.driver = driver

    def wait_for_new_page(self):
        time.sleep(5)
        print(f"Redirigido a la página")
    
    def validate_http_status(self, url):
        try:
            print(f"Verificando la URL: {url}")  # Añadir un mensaje de log
            status_code = self.page.get_status_code(url)
            print(f"Código de estado recibido: {status_code}")  # Log del código de estado

            status_code = self.page.get_status_code(url)
            assert status_code == 200, f"HTTP Error: status code {status_code}"
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="HTTP Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"HTTP Error: {e}")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Unexpected Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Ocurrió un error inesperado al validar el status HTTP: {str(e)}")

    def select_basic_price(self):
        
        is_fly_button_present = self.page.click_element_wait(self.FLY_BUTTON)
        if not is_fly_button_present:
            raise NoSuchElementException(f"La opción para vuelo de ida no es visible o no existe.")
            
        self.page.click_element(self.FLY_BUTTON)
        self.page.click_element(self.BASIC_PRICE_BUTTON)
        self.validate_http_status(self.driver.current_url)
        print('basic price')
    
    def select_flex_price(self):
        is_fly_button_present = self.page.click_element_wait(self.FLY_BUTTON)
        if not is_fly_button_present:
            raise NoSuchElementException(f"La opción para vuelo de vuelta no es visible o no existe.")
            
        self.page.click_element(self.FLY_BUTTON)
        self.page.click_element(self.FLEX_PRICE_BUTTON)
        self.validate_http_status(self.driver.current_url)
        print('basic price')
       
    def validate_type_fly(self, fly):
        try:                  
            if fly == 'Ida':
                self.select_basic_price() 
            else:
                self.select_flex_price()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error interactuando con el elemento: {str(e)}")
        
    def select_continue(self):
        try:
            self.page.click_element(self.CONTINUE_BUTTON)
            self.validate_http_status(self.driver.current_url)
            
        except ElementNotInteractableException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="ElementNotInteractableException screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"El elemento no es interactuable o no está habilitado para continuar con las opciones de vuelo")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error interactuando con el elemento: {e.msg}")
            