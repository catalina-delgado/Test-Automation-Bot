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
    def test_spanish_languages(self, base_url):
        event = BookingFlow(self.driver, base_url)
        event.language_validation('Español')
        
    def test_english_languages(self, base_url):
        event = BookingFlow(self.driver, base_url)
        event.language_validation(' English ')
        
    def test_french_languages(self, base_url):
        event = BookingFlow(self.driver, base_url)
        event.language_validation(' Français ')
        
    def test_portuguese_language(self, base_url):
        event = BookingFlow(self.driver, base_url)
        event.language_validation(' Português ')
        