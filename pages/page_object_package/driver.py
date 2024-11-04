from selenium.webdriver.ie.webdriver import WebDriver

from pages.page_object_package.driver_handler import DriverHandler

class Driver:
    def __init__(self):
        self.base_class = DriverHandler.get_instance()

    def get_driver(self) -> WebDriver:
        return self.base_class.driver

    def set_driver(self, driver):
        self.base_class.set_driver(driver)