# Caso automatizado 4: Verificar cambio de POS (País)
# • Seleccionar 3 POS (Otros países, España, Chile).
# • Verificar que cada cambio de POS se hace correctamente.

import pytest
from libs.base_page import BasePage
from objects.booking_flow import BookingFlow
from objects.price_flow import PriceFlow

@pytest.mark.usefixtures("setup")
class TestChangePOS():
    #Home
    def test_spanish_languages(self, base_url):
        event = BookingFlow(self.driver, base_url)
        event.country_validation(' Brasil ')
        
    def test_spain_country(self, base_url):
        event = BookingFlow(self.driver, base_url)
        event.country_validation(' España ')
        
    def test_chile_country(self, base_url):
        event = BookingFlow(self.driver, base_url)
        event.country_validation(' Chile ')
        