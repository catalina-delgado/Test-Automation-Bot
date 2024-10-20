# Caso automatizado 3: Verificar cambio de idioma
# • Seleccionar los 4 idiomas (Español, Inglés, Francés, Portuguese).
# • Verificar que cada cambio de idioma se hace correctamente.

import pytest
from libs.base_page import BasePage
from objects.booking_flow import BookingFlow
from objects.price_flow import PriceFlow

@pytest.mark.usefixtures("setup")
class TestChangeLanguage():
    #Home
    def test_languages(self, base_url):
        event = BookingFlow(self.driver, base_url)
        
        event.validate_language('Español')
        event.object.wait_for_new_page(timeout=1)
        
        event.validate_language('English')
        event.object.wait_for_new_page()
        event.object.wait_for_new_page(timeout=1)
        
        event.validate_language('Français')
        event.object.wait_for_new_page()
        event.object.wait_for_new_page(timeout=1)
        
        event.validate_language('Português')
        event.object.wait_for_new_page(timeout=1)
        