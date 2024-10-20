from pages.home_page import HomePage
from libs.base_page import BasePage

import time

class BookingFlow(HomePage):
    def __init__(self, driver, base_url):
        super().__init__()
        self.page = BasePage(driver)
        self.page.load_page(base_url)
        self.driver = driver
    
    def wait_for_new_page(self):
        time.sleep(5)
        # print(f"Redirigido a la página")
    
    def select_one_way_trip(self):
        # Validar si el checkbox tiene un label que dice "Solo ida"
        one_way_label = self.page.select_element_wait(self.ONE_WAY_LABEL)
        assert "Solo ida" in one_way_label.text, "El label no dice 'Solo ida'"

        # Seleccionar el checkbox si no está seleccionado
        checkbox = self.page.select_element_wait(self.ONE_WAY_CHECKBOX)
        if not checkbox.is_selected():
            self.page.click_element(self.ONE_WAY_CHECKBOX)
    
    def select_two_way_trip(self):
        # Validar si el checkbox tiene un label que dice "Solo ida"
        two_way_label = self.page.select_element_wait(self.TWO_WAY_LABEL)
        assert "Ida y vuelta" in two_way_label.text, "El label no dice 'Ida y Vuelta'"

        # Seleccionar el checkbox si no está seleccionado
        checkbox = self.page.select_element_wait(self.TWO_WAY_CHECKBOX)
        if not checkbox.is_selected():
            self.page.click_element(self.TWO_WAY_CHECKBOX)
    
    def language_validation(self, language):
        is_language_button_present = self.page.select_element_wait(self.LANGUAGE_BUTTON)
        is_language_button_clickable = self.page.click_element_wait(self.LANGUAGE_BUTTON)
        self.page.click_element(self.LANGUAGE_BUTTON)
        
        is_language_dropdown_present = self.page.select_element_wait(self.LANGUAGE_DROPDOWN)
        dropdown = self.page.visible_element_wait(self.LANGUAGE_DROPDOWN)
        
        is_option_language_button_present = self.page.select_element_wait(self.LANGUAGE_OPTION_BUTTON)
        is_option_language_button_clickable = self.page.click_element_wait(self.LANGUAGE_OPTION_BUTTON)
        language_options = self.page.find_elements(self.LANGUAGE_OPTION_BUTTON)
        languaje_labels = self.page.find_elements(self.LANGUAGE_LABEL)

        for option, label in zip(language_options, languaje_labels):
            if label.text == language:
                option.click() 
                break
    
    def country_validation(self, pos):
        is_language_button_present = self.page.select_element_wait(self.POS_BUTTON)
        is_language_button_clickable = self.page.click_element_wait(self.POS_BUTTON)
        self.page.click_element(self.POS_BUTTON)
        is_list_country_present = self.page.select_element_wait(self.COUNTRY_LIST)
        
        def country_selected(pos):
            selected_country = self.page.get_text(self.LANGUAGE_TEXT)
            return selected_country == pos
        
        is_country_selected = country_selected(pos)
        self.page.click_element(self.CLOSE_COUNTRY_LIST_BUTTON)

    def fill_inputs(self, texts):
        is_origin_inputs_present = self.page.enter_text_element_input(self.CONTROL_INPUT, texts)
    
    def select_date_input(self, dates):
        located_date_inputs = self.page.find_elements(self.DATE_INPUT)
        for located_date_input, date in zip(located_date_inputs, dates):
            located_date_input.click()
            
            is_calendar_visible = self.page.visible_element_wait(self.DATE_CALENDAR)
            self.page.click_element(self.get_day_button(date))
           
    def validate_http_status(self, url):
        status_code = self.page.get_status_code(url)
        assert status_code == 200, f"HTTP Error: status code {status_code}"
        
    def passenger_validation(self):
        options_list_minus_buttons = self.page.find_elements(self.OPTIONS_LIST_MINUS_BUTTON)
        options_list_plus_buttons = self.page.find_elements(self.OPTIONS_LIST_PLUS_BUTTON)
        options_list_inputs = self.page.find_elements(self.OPTIONS_LIST_INPUTS)
        
        # is_button_submit_cliclable=self.page.click_element_wait(self.OPTION_LIST_SUBMIT_BUTTON)
        # if is_button_submit_cliclable:
        #     submit_button = self.page.find_element(self.OPTION_LIST_SUBMIT_BUTTON)
        # else:
        #     self.page.click_element_js(self.OPTION_LIST_SUBMIT_BUTTON)
        #     print('cliclando con js')
            
        # for minus, plus, input in zip(options_list_minus_buttons, options_list_plus_buttons, options_list_inputs):
        #     plus.click()
            
        #     if init(input.get_attribute("value"))== 0:
        #         plus.click()
        #     elif init(input.get_attribute("value")) > 1:
        #         minus.click()
            
        #     print('vslor del input',input.get_attribute("value"))
        
        self.page.click_element(self.OPTION_LIST_SUBMIT_BUTTON)
        self.page.click_element(self.SEARCH_BUTTON)
        self.validate_http_status(self.driver.current_url)
