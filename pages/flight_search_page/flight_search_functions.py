import random
from enum import Enum

from pages.flight_search_page.flight_search_locators import DEPARTING_INPUT_FILED, ACTIVATED_CALENDAR_DAYS_BUTTONS, \
    OK_BUTTON, DEPARTURE_DATE_FILED, CANCEL_BUTTON, RETURNING_INPUT_FILED, RETURN_DATE_FILED, ADULTS_INPUT_FILED, \
    ADULTS_NUMBER_DROP_DOWN_BUTTONS, CHILDREN_INPUT_FILED, CHILDREN_NUMBER_DROP_DOWN_BUTTONS, SELECT_DESTINATION_BTN
from pages.page_object_package.base_page import BasePage
from pages.page_object_package.driver import Driver

class TripType(Enum):
    DEPARTURE = "Departure"
    RETURN = "Return"

class PassengerType(Enum):
    ADULT = "Adult"
    CHILD = "Child"

class SearchFlight:
    def __init__(self):
        self.base_page = BasePage()
        self.driver = Driver().get_driver()

    def choose_certain_date(self, current_chosen_day: int = -1):
        activated_days_buttons = self.base_page.find_elements(ACTIVATED_CALENDAR_DAYS_BUTTONS)
        activated_days_buttons = [button for date, button in enumerate(activated_days_buttons)
                                  if date != current_chosen_day]
        activated_days_buttons[random.randint(0, len(activated_days_buttons))].click()

    def choose_date(self, trip_type: TripType):
        self.base_page.click(DEPARTING_INPUT_FILED if trip_type == TripType.DEPARTURE else RETURNING_INPUT_FILED)
        self.choose_certain_date()
        self.base_page.click(OK_BUTTON)

    def get_current_date(self, trip_type: TripType) -> str:
        return self.base_page.find_element(DEPARTURE_DATE_FILED).get_attribute("value")\
            if trip_type == TripType.DEPARTURE \
            else self.base_page.find_element(RETURN_DATE_FILED).get_attribute("value")

    def get_current_return_sate(self) -> str:
        return self.base_page.find_element(RETURN_DATE_FILED).get_attribute("value")

    def change_departure_date(self, trip_type: TripType, negative_test: bool = False):
        before_change_date = self.get_current_date(trip_type)
        current_day_date = int(before_change_date.split()[0])
        self.choose_certain_date(current_chosen_day=current_day_date)
        if negative_test:
            self.base_page.click(CANCEL_BUTTON)
            assert self.get_current_date(trip_type)  == before_change_date
        else:
            self.base_page.click(OK_BUTTON)
            assert self.get_current_date(trip_type) != before_change_date

    def choose_passengers_num(self, passenger_type: PassengerType):
        self.base_page.click(ADULTS_INPUT_FILED if passenger_type == PassengerType.ADULT else CHILDREN_INPUT_FILED)
        passengers_num_buttons = self.base_page.find_elements(
            ADULTS_NUMBER_DROP_DOWN_BUTTONS if passenger_type == PassengerType.ADULT
            else CHILDREN_NUMBER_DROP_DOWN_BUTTONS)
        passengers_num_buttons[random.randint(1, len(passengers_num_buttons))].click()

    def search_random_flight(self):
        self.choose_date(trip_type=TripType.DEPARTURE)
        self.choose_date(trip_type=TripType.RETURN)
        self.choose_passengers_num(passenger_type=PassengerType.ADULT)
        self.choose_passengers_num(passenger_type=PassengerType.CHILD)
        self.base_page.click(SELECT_DESTINATION_BTN)




