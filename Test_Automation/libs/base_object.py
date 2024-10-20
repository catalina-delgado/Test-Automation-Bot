from libs.base_page import BasePage

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

import time
import allure


class BaseFlow():
    def __init__(self, driver):
        super().__init__()
        self.page = BasePage(driver)
        self.driver = driver

    def wait_for_new_page(self, timeout=5):
        time.sleep(timeout)
    
    def validate_http_status(self, url):
        try:
            print(f"Verifying the URL: {url}")  # Añadir un mensaje de log
            status_code = self.page.get_status_code(url)
            print(f"Status code received: {status_code}")  # Log del código de estado

            status_code = self.page.get_status_code(url)
            assert status_code == 200, f"HTTP Error: status code {status_code}"
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="HTTP Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"HTTP Error: {e}")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Unexpected Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Ocurrió un error inesperado al validar el status HTTP: {str(e)}")

