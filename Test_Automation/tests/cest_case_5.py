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
from objects.header_flow import HeaderFlow
from objects.booking_flow import BookingFlow

@pytest.mark.usefixtures("setup")
class TestHeader():
    
    def test_home(self, base_url):
        #Home
        event = BookingFlow(self.driver, base_url)
        event.select_one_way_trip()
        event.language_validation('Español')
        event.country_validation(' Estados Unidos ')
        
    def test_header(self):
        #Header
        event = HeaderFlow(self.driver)
        #First validation site
        event.validate_navbar_link('Reservar')
        #Second validation Site
        event.validate_navbar_button(index_button=0)
        #third validation Site
        event.validate_navbar_button(index_button=1)
        
        