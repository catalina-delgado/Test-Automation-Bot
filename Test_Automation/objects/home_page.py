from base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    LANGUAGE_DROPDOWN = (By.ID, "language-selector")
    ORIGIN_INPUT = (By.ID, "origin")
    DESTINATION_INPUT = (By.ID, "destination")
    SEARCH_BUTTON = (By.ID, "search-flight")

    def select_language(self, language):
        self.select_dropdown_by_text(self.LANGUAGE_DROPDOWN, language)

    def enter_origin(self, origin):
        self.type(self.ORIGIN_INPUT, origin)

    def enter_destination(self, destination):
        self.type(self.DESTINATION_INPUT, destination)

    def search_flights(self):
        self.click(self.SEARCH_BUTTON)
