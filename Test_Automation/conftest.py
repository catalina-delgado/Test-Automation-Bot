import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on: chrome or firefox")

@pytest.fixture(scope="class")
def setup(request):
    path_to_chromedriver = "C:\\Users\\Public\\Documents\\chromedriver-win64\\chromedriver.exe"
    browser = request.config.getoption("--browser")

    # chrome_service = ChromeService()
    # driver = webdriver.Chrome(service=chrome_service)
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser {browser} is not supported.")
    
    request.cls.driver = driver
    yield
    driver.quit()