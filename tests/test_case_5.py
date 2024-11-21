import pytest
from libs.base_page import BasePage
from objects.header_flow import HeaderFlow
from objects.booking_flow import BookingFlow

@pytest.mark.usefixtures("setup")
class TestHeader():
    
    def test_home(self, base_url):
        #Home
        event = BookingFlow(self.driver, base_url)
        event.validate_language('Español')
        event.validate_country('Estados Unidos')
        
    def test_header(self):
        #Header
        event = HeaderFlow(self.driver)
        
        #First site validation to links
        event.validate_navbar_link('Reservar')
        
        #Second site validation to buttons on first option menu
        event.validate_navbar_button(index_button=0)
        
        #third site validation to buttons on first option menu
        event.validate_navbar_button(index_button=1)
        
        