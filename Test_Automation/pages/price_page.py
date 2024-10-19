from libs.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

class PricePage():
        
    OPTION_PRICE_BUTTON = (By.XPATH, "//button[@class='journey_price_button ng-tns-c12-2 ng-star-inserted']")
    SELECT_PRICE_BUTTON = (By.XPATH, "//div[normalize-space(@aria-label)='Click to select basic fare']")  
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(@class, 'button btn-next')]/span[contains(normalize-space(text()), 'Continuar')]")


     
    