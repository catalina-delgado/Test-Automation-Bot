from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def load_page(self, url):
        self.driver.get(url)
        
    def get_title(self):
        return self.driver.title

    def open(self, url):
        self.driver.get(url)

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def type(self, by_locator, text):
        self.driver.find_element(*by_locator).send_keys(text)

    def get_text(self, by_locator):
        return self.driver.find_element(*by_locator).text
