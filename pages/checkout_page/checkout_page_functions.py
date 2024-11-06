import re

from pages.checkout_page.checkout_page_locators import NAME_FILED, EMAIL_ADDRESS_FILED, SOCIAL_SECURITY_NUM_FILED, \
    PHONE_NUM_FILED, PRICE_PER_TRAVELER, TRAVELERS_NUM_FILED, TOTAL_PRICE_FILED, PROMO_CODE_FILED, APPLY_BTN, \
    AGREE_WITH_TERMS_CHECKBOX, PAY_BTN
from pages.page_object_package.base_page import BasePage
from pages.page_object_package.driver import Driver


class CheckoutProcess:
    def __init__(self):
        self.base_page = BasePage()
        self.driver = Driver().get_driver()

    def file_passenger_info(self):
        self.base_page.send_keys(locator=NAME_FILED, keys="Yarin Shetrit")
        self.base_page.send_keys(locator=EMAIL_ADDRESS_FILED, keys="yarin1710@gmail.com")
        self.base_page.send_keys(locator=SOCIAL_SECURITY_NUM_FILED, keys="123366559")
        self.base_page.send_keys(locator=PHONE_NUM_FILED, keys="0546080090")

    def check_price_fields(self):
        price_per_passenger = float(self.base_page.find_element(PRICE_PER_TRAVELER).text.replace("$", ""))
        travelers_num = int(re.search(r'\d+',self.base_page.find_element(TRAVELERS_NUM_FILED).text).group())
        total_price = float(self.base_page.find_element(TOTAL_PRICE_FILED).text.replace("$", ""))
        assert (price_per_passenger * travelers_num) == total_price

    def enter_promo_code(self):
        assert not self.base_page.find_element(APPLY_BTN).is_enabled()
        self.base_page.send_keys(PROMO_CODE_FILED, keys='5674322')
        self.base_page.click(APPLY_BTN)

    def total_checkout_process(self):
        self.file_passenger_info()
        self.check_price_fields()
        self.enter_promo_code()
        assert not self.base_page.find_element(PAY_BTN).is_enabled()
        self.base_page.click(AGREE_WITH_TERMS_CHECKBOX)
        self.base_page.click(PAY_BTN)