import pytest
from libs.base_page import BasePage
from objects.booking_flow import BookingFlow
from objects.price_flow import PriceFlow

@pytest.mark.usefixtures("setup")
class TestChangePOS():
    #Home
    
    def test_brazil_country(self, base_url):
        event = BookingFlow(self.driver, base_url)
        
        event.validate_country('Brasil')
        event.object.wait_for_new_page(timeout=1)
        
        event.validate_country('España')
        event.object.wait_for_new_page(timeout=1)
        
        event.validate_country('Chile')
        event.object.wait_for_new_page(timeout=1)
        