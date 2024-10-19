from libs.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

class HomePage():
 
    ONE_WAY_CHECKBOX = (By.ID, "journeytypeId_1")
    ONE_WAY_LABEL = (By.XPATH, "//label[@for='journeytypeId_1']/span[text()='Solo ida']")
    
    LANGUAGE_DROPDOWN = (By.XPATH, "//ul[@class='options-list options-list--type-list']")
    LANGUAGE_BUTTON = (By.XPATH, "//div[@class='language-selector']")
    LANGUAGE_TEXT = (By.XPATH, "//span[@class='button_label']")
    
    POS_BUTTON = (By.XPATH, "//button[@id='pointOfSaleSelectorId']")
    COUNTRY_LIST = (By.XPATH, '//ul[@class="points-of-sale_list"]')
    CLOSE_COUNTRY_LIST_BUTTON = (By.XPATH, '//BUTTON[@class="points-of-sale_header_close-button"]')
    
    ORIGIN_SATATION_SPAN =  (By.XPATH, "//SPAN[@id='originStationSelected']")
    CONTROL_INPUT = (By.CLASS_NAME, "control_field_input")
    DATE_INPUT = (By.CLASS_NAME, "input-date-picker")
    DATE_CALENDAR = (By.CLASS_NAME, "ngb-dp-month")
    
    PASSENGER_BUTTON = (By.XPATH, "//button[@class='control_field_button']")  
    OPTIONS_LIST = (By.ID, "paxControlSearchId") 
    OPTIONS_LIST_MINUS_BUTTON = (By.CLASS_NAME, "ui-num-ud_button minus") 
    OPTIONS_LIST_PLUS_BUTTON = (By.CLASS_NAME, "ui-num-ud_button plus") 
    OPTION_LIST_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'control_options_selector_action_button') and span[contains(text(), 'Confirmar')]]")
    OPTIONS_LIST_INPUTS = (By.XPATH, "//div[@class='ui-num-ud_input']/input")
    SEARCH_BUTTON = (By.XPATH, "//button[@id='searchButton']")
                
    def get_country_button(self, pos):
        return (By.XPATH, "//button[@class='points-of-sale_list_item_button']/span[text()='{pos}']")

    def get_day_button(self, date):
        return (By.XPATH, f"//span[@class='custom-day_day' and normalize-space(text())='{date}']")
    
class PassengerInfoPage():
    passengers = []
    