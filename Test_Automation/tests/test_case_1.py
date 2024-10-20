# Caso automatizado 1: Realizar booking One-way (Solo ida) realizando las
# siguientes validaciones en cada página.
# • Home: Seleccionar idioma, pos, origen, destino y 1 pasajero de
# cada tipo (Adulto, Joven, Niño e Infante).
# • Select flight: Seleccionar tarifa Basic.
# • Passengers: Ingresar la información de los pasajeros.
# • Services: No seleccionar ninguno.
# • Seatmap: Seleccionar asiento economy.
# • Payments: Realizar pago con tarjeta utilizando información fake
# (No importa que el pago sea rechazado).

import pytest
from libs.base_page import BasePage
from objects.booking_flow import BookingFlow
from objects.price_flow import PriceFlow

@pytest.mark.usefixtures("setup")
class TestBookingOneWay():
    
    def test_home(self, base_url):
        #Home
        event = BookingFlow(self.driver, base_url)
        
        event.validate_language('Español')
        event.validate_country('Colombia')
        event.select_one_way_trip()

        texts_for_inputs = ['Manizales', 'Barrancabermeja']
        event.fill_inputs(texts_for_inputs)
        
        event.select_date_input(['30'])
        event.validate_passenger()
        
    def test_price(self):
        #Price
        event = PriceFlow(self.driver)
        event.object.wait_for_new_page()
        event.select_basic_price()
        event.select_continue()
    
        