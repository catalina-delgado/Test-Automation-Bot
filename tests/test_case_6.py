import pytest
from libs.base_page import BasePage
from objects.footer_flow import FooterFlow
from objects.booking_flow import BookingFlow

@pytest.mark.usefixtures("setup")
class TestFooter():
    
    def test_home(self, base_url):
        #Home
        event = BookingFlow(self.driver, base_url)
        event.validate_language('Español')
        event.validate_country('Estados Unidos')
        
    def test_footer(self):
        #Footer
        event = FooterFlow(self.driver)
                
        #First validation site
        event.scroll_to_footer()
        event.validate_footer_link(index=0)
        
        #Second validation Site
        event.scroll_to_footer()
        event.validate_footer_link(index=1)
        
        #third validation Site
        event.scroll_to_footer()
        event.validate_footer_link(index=2)
        event.close_redirected_window()
       
        #third validation Site
        event.scroll_to_footer()
        event.validate_footer_link(index=3)
        
        