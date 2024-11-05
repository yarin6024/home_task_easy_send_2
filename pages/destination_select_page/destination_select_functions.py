import random
import time

from selenium.webdriver import ActionChains

from pages.destination_select_page.destination_select_locators import PRICE_SLIDER, PRICE_RANGES_IN_SLIDER, PRICE_FILED, \
    DESTINATIONS_NAME_FILED, LUNCH_DESTINATION_BTN, DESTINATIONS_BUTTONS, PLANET_COLOR_BTN, PLANET_COLOR_BUTTONS, \
    OPTION_PLANET_COLOR_IN_DROP_DOWN_OPTIONS, BOOK_BUTTONS, OPTION_LAUNCH_IN_DROP_DOWN_OPTIONS
from pages.page_object_package.base_page import BasePage
from pages.page_object_package.driver import Driver


class SelectDestination:
    def __init__(self):
        self.base_page = BasePage()
        self.driver = Driver().get_driver()

    def move_price_slider(self):
        price_slider = self.base_page.find_element(PRICE_SLIDER)
        action = ActionChains(self.driver)
        action.click_and_hold(price_slider).move_by_offset(20, 0).release().perform()

    def check_price_change(self):
        self.move_price_slider()
        price_ranges_in_slider = self.base_page.find_elements(PRICE_RANGES_IN_SLIDER)
        price_ranges_value = [float(price_range.get_attribute("value").replace("$", "")) for price_range in price_ranges_in_slider]
        lowest_price = min(price_ranges_value)
        highest_price = max(price_ranges_value)
        price_fields = self.base_page.find_elements(PRICE_FILED)
        for current_price_field in price_fields:
            destination_price = float(current_price_field.text.replace("$", ""))
            assert destination_price >= lowest_price
            assert destination_price <= highest_price

    def check_destination_drop_down(self):
        self.base_page.click(LUNCH_DESTINATION_BTN)
        destinations_drop_down_options = self.base_page.find_elements(DESTINATIONS_BUTTONS)
        chosen_destination = random.choice(destinations_drop_down_options)
        chosen_destination_name = chosen_destination.text
        chosen_destination.click()
        destinations_cards_name = self.base_page.find_elements(DESTINATIONS_NAME_FILED)
        for destination_card_name in destinations_cards_name:
            assert destination_card_name.text == chosen_destination_name
        self.base_page.click(LUNCH_DESTINATION_BTN)
        self.base_page.click(OPTION_LAUNCH_IN_DROP_DOWN_OPTIONS)

    def check_destination_color_drop_down(self):
        self.base_page.click(PLANET_COLOR_BTN)
        planet_color_options = self.base_page.find_elements(PLANET_COLOR_BUTTONS)
        random.choice(planet_color_options).click()
        self.base_page.click(PLANET_COLOR_BTN)
        self.base_page.click(OPTION_PLANET_COLOR_IN_DROP_DOWN_OPTIONS)

    def click_on_random_book_btn(self):
        book_buttons = self.base_page.find_elements(BOOK_BUTTONS)
        random.choice(book_buttons).click()

    def book_destination(self):
        self.check_destination_color_drop_down()
        self.check_destination_drop_down()
        self.check_price_change()
        self.click_on_random_book_btn()


