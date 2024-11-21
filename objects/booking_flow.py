from pages.home_page import HomePage
from libs.base_page import BasePage
from libs.base_object import BaseFlow

import time
import allure

class BookingFlow(HomePage):
    def __init__(self, driver, base_url):
        super().__init__()
        self.page = BasePage(driver)
        self.page.load_page(base_url)
        self.object = BaseFlow(driver)
        self.driver = driver
    
    def select_one_way_trip(self):
        one_way_label = self.page.select_element_wait(self.ONE_WAY_LABEL)
        assert "Solo ida" in one_way_label.text, "Label does not say One way trip"

        checkbox = self.page.select_element_wait(self.ONE_WAY_CHECKBOX)
        if not checkbox.is_selected():
            self.page.click_element(self.ONE_WAY_CHECKBOX)
    
    def select_round_trip(self):
        round_label = self.page.select_element_wait(self.ROUND_LABEL)
        assert "Ida y vuelta" in round_label.text, "Label does not say round trip"

        checkbox = self.page.select_element_wait(self.ROUND_CHECKBOX)
        if not checkbox.is_selected():
            self.page.click_element(self.ROUND_CHECKBOX)
    
    @allure.step("Language Verification")
    def validate_language(self, language):
        try:
            is_language_button_present = self.page.select_element_wait(self.LANGUAGE_BUTTON)
            self.page.click_element(self.LANGUAGE_BUTTON)
            
            is_language_dropdown_present = self.page.select_element_wait(self.LANGUAGE_DROPDOWN)
            dropdown = self.page.visible_element_wait(self.LANGUAGE_DROPDOWN)
            
            is_option_language_button_present = self.page.select_element_wait(self.LANGUAGE_OPTION_BUTTON)
            language_options = self.page.find_elements(self.LANGUAGE_OPTION_BUTTON)
            # print(' '.join(option.text for option in language_options))

            for option in language_options:
                if language in option.text:
                    print(option.text)
                    option.click() 
                    break
                
            allure.attach(self.driver.get_screenshot_as_png(), name="Language verification", attachment_type=allure.attachment_type.PNG)
            print(f"Language verification successful for {language}")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error verification: {str(e)}")
    
    @allure.step("Country Verification")    
    def validate_country(self, pos):
        try:
            is_country_button_present = self.page.select_element_wait(self.POS_BUTTON)
            is_country_button_clickable = self.page.click_element_wait(self.POS_BUTTON)
            self.page.click_element(self.POS_BUTTON)
            
            is_list_country_present = self.page.select_element_wait(self.COUNTRY_LIST)
            is_option_country_button_present = self.page.select_element_wait(self.COUNTRY_OPTION_BUTTON)
            country_options = self.page.find_elements(self.COUNTRY_OPTION_BUTTON)

            for option in country_options:
                if pos in option.text:
                    print(option.text)
                    option.click() 
                    break
        
            self.page.click_element(self.APLY_COUNTRY_LIST_BUTTON)
            allure.attach(self.driver.get_screenshot_as_png(), name="Country verification", attachment_type=allure.attachment_type.PNG)
            print(f"Country verification successful for {pos}")
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error screenshot", attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error verification: {str(e)}")

    def fill_inputs(self, texts):
        is_origin_inputs_present = self.page.enter_text_element_input(self.CONTROL_INPUT, texts)
    
    def select_date_input(self, dates):
        located_date_inputs = self.page.find_elements(self.DATE_INPUT)
        for located_date_input, date in zip(located_date_inputs, dates):
            located_date_input.click()
            
            is_calendar_visible = self.page.visible_element_wait(self.DATE_CALENDAR)
            self.page.click_element(self.get_day_button(date))
    
    def select_button_list(self):
        button_list = self.page.find_element(self.BUTTON_LIST)
        button_list.click()
    
    
    @allure.step("Passenger Verification")          
    def validate_passenger(self):
        # passenger_button = self.page.find_element(self.PASSENGER_BUTTON)
        # passenger_button.click()
        
        # options_list_minus_buttons = self.page.find_elements(self.OPTIONS_LIST_MINUS_BUTTON)
        # options_list_plus_buttons = self.page.find_elements(self.OPTIONS_LIST_PLUS_BUTTON)
        options_list_inputs = self.page.find_elements(self.OPTIONS_LIST_INPUTS)
        
        # container=self.page.find_element(self.SUBMIT_BUTTON_CONTAINER)
        # # if is_button_submit_cliclable:
        # submit_button = self.page.find_element(self.OPTION_LIST_SUBMIT_BUTTON)
        # # else:
        #     self.page.click_element_js(self.OPTION_LIST_SUBMIT_BUTTON)
        #     print('cliclando con js')
            
        # for minus, plus, input in zip(options_list_minus_buttons, options_list_plus_buttons, options_list_inputs):
        #     plus.click()
            
        #     if init(input.get_attribute("value"))== 0:
        #         plus.click()
        #     elif init(input.get_attribute("value")) > 1:
        #         minus.click()
            
        #     print('vslor del input',input.get_attribute("value"))
        
        # self.page.click_element(self.OPTION_LIST_SUBMIT_BUTTON)
        self.page.click_element(self.SEARCH_BUTTON)
        self.object.validate_http_status(self.driver.current_url)
