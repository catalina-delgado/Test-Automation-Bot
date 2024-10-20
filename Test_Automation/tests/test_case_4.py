# Caso automatizado 4: Verificar cambio de POS (País)
# • Seleccionar 3 POS (Otros países, España, Chile).
# • Verificar que cada cambio de POS se hace correctamente.
# Caso automatizado 5: Redirecciones Header
# • Utilizar las opciones del Navbar para acceder a 3 sitios diferentes.
# • Verificar que la url de los sitios cargan correctamente de acuerdo
# con el idioma y sitio seleccionado.
# Caso automatizado 6: Redirecciones Footer
# • Utilizar los links del footer para acceder a 4 sitios diferentes.
# • Verificar que la url de los sitios cargan correctamente de acuerdo
# con el idioma y sitio seleccionado.


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
        