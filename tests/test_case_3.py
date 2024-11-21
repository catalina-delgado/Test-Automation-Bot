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
        