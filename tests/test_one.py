import pytest

from pages.checkout_page.checkout_page_functions import CheckoutProcess
from pages.destination_select_page.destination_select_functions import SelectDestination
from pages.flight_search_page.flight_search_functions import SearchFlight
from pages.page_object_package.driver import Driver


@pytest.mark.parametrize('driver', [{"url": "https://demo.testim.io/checkout"}], indirect=True)
def test_base_process(driver):
    Driver().set_driver(driver)
    SearchFlight().search_random_flight()
    SelectDestination().book_destination()
    CheckoutProcess().total_checkout_process()



