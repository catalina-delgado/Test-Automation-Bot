# Caso automatizado 2: Realizar booking Round-trip(Ida y vuelta) realizando las
# siguientes validaciones en cada página.
# • Home: Seleccionar idioma, pos, origen, destino y 1 pasajero de
# cada tipo (Adulto, Joven, Niño e Infante).
# • Select flight: Seleccionar tarifa Basic (Ida) y Flex (Vuelta).
# • Passengers: Ingresar la información de los pasajeros.
# • Services: Seleccionar Avianca Lounges y en caso de que no esté
# disponible el servicio, seleccionar cualquiera.
# • Seatmap: Seleccionar asiento Plus, Economy, Premium y Economy
# (Si hay disponibilidad).
# • Payments: Realizar pago con tarjeta utilizando información fake
# (No importa que el pago sea rechazado).

import pytest
from libs.base_page import BasePage
from objects.booking_flow import BookingFlow
from objects.price_flow import PriceFlow

@pytest.mark.usefixtures("setup")
class TestBookingTwoWay():
    
    def test_home(self, base_url):
        #Home
        event = BookingFlow(self.driver, base_url)
        event.select_two_way_trip()
        event.language_validation('Español')
        event.country_validation('Colombia')

        texts_for_inputs = ['Manizales', 'Barrancabermeja']
        event.fill_inputs(texts_for_inputs)
        
        dates_for_inputs = ['24', '28']
        event.select_date_input(dates_for_inputs)
        event.passenger_validation()
        
    def test_price(self):
        #Price
        event = PriceFlow(self.driver)
        event.wait_for_new_page()
        event.validate_type_fly('Ida')
        event.validate_type_fly('Vuelta')
        event.select_continue()
        