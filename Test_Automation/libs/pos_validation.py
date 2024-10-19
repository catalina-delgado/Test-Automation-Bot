class LanguageValidationPage(by_locator):
    
    def __init__(self, driver):
        self.driver = driver
    
    def is_country_list_present(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(by_locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_country_list_clickable(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(by_locator)
            )
            return True
        except TimeoutException:
            return False
    
    def get_available_countries(self):
        self.driver.find_element(*by_locator).click()
        OPTIONS = self.driver.find_elements(By.XPATH, "//li[@class='points-of-sale_list_item']")
        return [option.text for option in OPTIONS]
    
    def validate_countries(self, expected_languages):
        AVAILABLE_LANGUAJES = self.get_available_languages()
        for language in expected_languages:
            if language not in AVAILABLE_LANGUAJES:
                return False
        return True
    
    def is_language_selected(self, language):
        SELECTED_OPTION = self.driver.find_element(By.XPATH, "//li[@class='list_item--active']").text
        return selected_language == language
