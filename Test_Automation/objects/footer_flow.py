from pages.footer_page import FooterPage
from libs.base_page import BasePage
from libs.base_object import BaseFlow

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

import time
import allure

class FooterFlow(FooterPage):
    def __init__(self, driver):
        super().__init__()
        self.page = BasePage(driver)
        self.object = BaseFlow(driver)
        self.driver = driver

    def scroll_to_footer(self):
        is_footer_present = self.page.select_element_wait(self.FOOTER)
        self.page.scroll_to_element(self.FOOTER)
        
    def close_redirected_window(self):
        original_window = self.driver.current_window_handle
        all_open_windows = self.driver.window_handles
        self.driver.switch_to.window(all_open_windows[-1])
        self.driver.close()
        self.driver.switch_to.window(original_window)
        
    @allure.step("Verificar enlace")
    def validate_footer_link(self, index=0):  
        try:
            navfooter = self.page.find_element(self.NAVFOOTER)
            submenus = navfooter.find_elements(By.TAG_NAME, 'ul')
            submenu = submenus[index]
            submenu_links = submenu.find_elements(By.TAG_NAME, 'a')
            link = submenu_links[0]
            link_text = link.text
            link.click()
           
            self.object.validate_http_status(self.driver.current_url)

            self.object.wait_for_new_page()
            allure.attach(self.driver.get_screenshot_as_png(), name="Link verification", attachment_type=allure.attachment_type.PNG)
            print(f"El primer enlace de {link_text} cargó correctamente")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error al verificar el enlace: {str(e)}")
