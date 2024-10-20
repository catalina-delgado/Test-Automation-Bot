from pages.header_page import HeaderPage
from libs.base_page import BasePage
from libs.base_object import BaseFlow

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

import time
import allure

class HeaderFlow(HeaderPage):
    def __init__(self, driver):
        super().__init__()
        self.page = BasePage(driver)
        self.object = BaseFlow(driver)
        self.driver = driver

    def load_element(self):
        # is_navbar_present = self.page.select_element_wait(self.NAVBAR)
        element = self.page.find_element(self.NAVBAR)
        
    @allure.step("Verificar enlace")
    def validate_navbar_link(self, item_link):  
        try:
            is_navbar_present = self.page.select_element_wait(self.NAVBAR)
            ITEM_LINK = self.get_item_link(item_link)
            is_item_link_present = self.page.select_element_wait(ITEM_LINK)
            is_item_link_clickable = self.page.click_element_wait(ITEM_LINK)
            self.page.click_element(ITEM_LINK)
            self.object.validate_http_status(self.driver.current_url)

            self.object.wait_for_new_page()
            allure.attach(self.driver.get_screenshot_as_png(), name="Link verification", attachment_type=allure.attachment_type.PNG)
            print(f"El enlace {item_link} cargó correctamente")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error al verificar el enlace: {str(e)}")
    
    def validate_navbar_button(self, index_button=0):  
        try:
            is_navbar_present = self.page.select_element_wait(self.NAVBAR)
            is_navbar_button_visible = self.page.visible_element_wait(self.NAVBAR_BUTTON)
            navbar_buttons = self.page.find_elements(self.NAVBAR_BUTTON)
            
            button = navbar_buttons[index_button]
            button_text = button.text
            button.click()
            SUBMENU = self.get_submenu(index_button+1)
            submenu_options = self.page.find_elements(SUBMENU)
            option = submenu_options[0]
            option.click()
            # self.driver.execute_script("arguments[0].click();", option)

            self.object.validate_http_status(self.driver.current_url)

            self.object.wait_for_new_page()
            allure.attach(self.driver.get_screenshot_as_png(), name="Link verification", attachment_type=allure.attachment_type.PNG)
            print(f"El primer enlace de {button_text} cargó correctamente")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error al verificar el enlace: {str(e)}")
    
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
            