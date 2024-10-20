from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

import logging
import requests


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        
    def load_page(self, url):
        self.driver.get(url)
        
    def get_title(self):
        return self.driver.title

    def open(self, url):
        self.driver.get(url)
        
    def find_element(self, by_locator):
        return self.driver.find_element(*by_locator)
    
    def find_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def click_element(self, by_locator):
        self.driver.find_element(*by_locator).click()
        
    def get_elements(self, by_locator):
        return self.driver.find_elements(*by_locator).text
    
    def type(self, by_locator, text):
        self.driver.find_element(*by_locator).send_keys(text)

    def get_text(self, by_locator):
        return self.driver.find_element(*by_locator).text
        
    def click_element_wait(self, by_locator):
        try:
            # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(by_locator))
            return True
        except TimeoutException:
            return False

    
    def select_element_wait(self, by_locator):
        # Espera y selecciona el elemento 
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator))
        return element
    
    def visible_element_wait(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element
        
    def press_tap_hey(self, by_locator):
        actions.move_to_element(self.driver.find_element(*by_locator)).send_keys('\ue004').perform()
        
    def enter_text_element_input(self, by_locator, texts):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
            input_value = element.get_attribute('value')
            if input_value:
                self.driver.execute_script("arguments[0].value = '';", element)  # Limpiar el valor del input
                element.send_keys(text)
            else:
                element.clear()
                element.send_keys(text)
        except:
            elements = self.driver.find_elements(*by_locator)
            for element, text in zip(elements, texts):
                self.driver.execute_script("arguments[0].removeAttribute('hidden');", element)
                element.clear()
                element.send_keys(text)
                self.actions.move_to_element(element).send_keys('\ue004').perform()
        
    def select_picker_element_input(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
            input_value = element.get_attribute('value')
            if input_value:
                self.driver.execute_script("arguments[0].value = '';", element)  # Limpiar el valor del input
            else:
                element.clear()
        except:
            elements = self.driver.find_elements(*by_locator)
            for element in elements:
                element.click()
                # self.driver.execute_script("arguments[0].removeAttribute('hidden');", element)
                # element.clear()
                # element.send_keys(text)
                # self.actions.move_to_element(element).send_keys('\ue004').perform()
    
    def click_element_js(self, by_locator):
        try:
            print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            print('cliclando con js')
            # self.driver.execute_script("arguments[0].click();", element)
            element.click()
            return True
        except Exception as e:
            logging.error(f"Error haciendo clic con JS: {e}")
            return False
        
    def get_status_code(self, url):
        try:
            response = requests.get(url)
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Error al hacer la solicitud: {e}")
            return 