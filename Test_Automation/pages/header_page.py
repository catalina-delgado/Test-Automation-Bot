from libs.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

class HeaderPage():
    NAVBAR = (By.XPATH, "//nav[normalize-space(@aria-label)='Main navigation']")
    NAVBAR_BUTTON = (By.XPATH, "//button[@class='main-header_nav-primary_item_link']//span[@class='button_label']")
    SUBMENU = (By.XPATH, "//nav[@class='main-header_primary-nav_submenu_column_nav']")
    SUBMENU_OPTION = (By.XPATH, "//li[@class='main-header_primary-nav_submenu_item']//a[@class='main-header_primary-nav_submenu_item--n3']")
    # main-header_primary-nav_submenu_item
    
    def get_submenu(self, index):
        return (By.XPATH, f"//primary-nav-sub-menu-custom[@id='primary-nav-sub-menu-{index}']")

    
    def get_item_link(self, item):
        return (By.XPATH, f"//li[@class='main-header_nav-primary_item main-header_nav-primary_item--']//span[normalize-space(text())='{item}']")
    
