from selenium.webdriver.ie.webdriver import WebDriver


class DriverHandler:
    __instance = None

    @staticmethod
    def get_instance():
        if DriverHandler.__instance is None:
            DriverHandler.__instance = DriverHandler()
        return DriverHandler.__instance

    def __init__(self):
        self.driver = None

    def set_driver(self, driver):
        self.driver = driver

    def get_driver(self) -> WebDriver:
        return self.driver


