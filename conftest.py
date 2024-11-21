import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on: chrome or firefox")

@pytest.fixture(scope="session")
def base_url():
    return "https://nuxqa3.avtest.ink/es/"

@pytest.fixture(scope="class")
def setup(request):
    path_to_chromedriver = "C:/Users/Catalina/Documents/FLYR/Test_Automation/drivers/chromedriver.exe"
    path_to_geckodriver = "C:/Users/Catalina/Documents/FLYR/Test_Automation/drivers/geckodriver.exe"
    path_to_firefox_binary = "C:/Program Files/Mozilla Firefox/firefox.exe"
 
    driver = browser = request.config.getoption("--browser")

    if browser == "chrome":
        chrome_service = ChromeService(path_to_chromedriver)
        chrome_options = ChromeOptions()
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    elif browser == "firefox":
        firefox_options = FireOptions()
        firefox_options.binary_location = path_to_firefox_binary

        gecko_service = FirefoxService(path_to_geckodriver)
        driver = webdriver.Firefox(service=gecko_service, options=firefox_options)
    else:
        raise ValueError(f"Browser {browser} is not supported.")
    
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()