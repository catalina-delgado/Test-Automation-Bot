from libs.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

class FooterPage():
    FOOTER = (By.XPATH, "//footer[normalize-space(@aria-label)='Site']")
    NAVFOOTER = (By.XPATH, "//div[@class='main-footer_nav']")
    SUBMENU_OPTION = (By.XPATH, "//a[@role='button']")
    
    #ng-tns-c30-14 -  Descubre y compra 
    #ng-tns-c30-15 -  Sobre nosotros 
    #ng-tns-c30-16 -  Nuestros Portales
    #ng-tns-c30-17 -  Enlaces rápidos
    
    def get_submenu(self):
        # return (By.XPATH, f"//ibe-main-footer-nav-custom[@class='ng-tns-c30-14']")
        return (By.XPATH, "//div[@class='main-footer_nav']")

    def get_item_link(self, item):
        return (By.XPATH, f"//li[@class='main-header_nav-primary_item main-header_nav-primary_item--']//span[normalize-space(text())='{item}']")
    
