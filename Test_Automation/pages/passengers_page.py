from libs.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

class PricePage():
        
    OPTION_PRICE_BUTTON = (By.XPATH, "//button[contains(@class, 'journey_price_button') and span[contains(text(), ' Seleccionar de tarifa ')]]")
             
    
    def get_country_button(self, pos):
        return (By.XPATH, "//button[@class='points-of-sale_list_item_button']/span[text()='{pos}']")

    def get_day_button(self, date):
        return (By.XPATH, f"//span[@class='custom-day_day' and normalize-space(text())='{date}']")
     