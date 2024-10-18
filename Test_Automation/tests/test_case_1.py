import pytest
from objects.base_page import BasePage

@pytest.mark.usefixtures("setup")
class TestBookingOneWay:
    
    def test_booking_one_way(self):
        page = BasePage(self.driver)
        page.load_page("https://nuxqa6.avtest.ink/es/")
        
        # validation title
        assert "avianca" in page.get_title()
        