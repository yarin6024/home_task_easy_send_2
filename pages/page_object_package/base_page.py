from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.page_object_package.driver import Driver


class BasePage:
    def __init__(self):
        self.driver = Driver().get_driver()
        self.logger = None
        self.wait = WebDriverWait(self.driver, 10)  # Adjust the wait time as needed

    def get_wait(self, timeout:int = 10) -> WebDriverWait:
        if timeout!= 10:
            self.wait = WebDriverWait(self.driver, timeout)
        return self.wait

    def click(self, locator, timeout:int = 12):
        self.get_wait(timeout).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self,locator, keys:str, clear:bool = True, timeout:int = 10):
        element = self.get_wait(timeout).until(EC.element_to_be_clickable(locator))
        if clear:
            element.clear()
        element.send_keys(keys)

    def find_element(self, locator, timeout:int = 10) -> WebElement:
        return self.get_wait(timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout: int=10, visibility:bool =False) -> [WebElement]:
        return self.get_wait(timeout).until(visibility_of_all_elements_located(locator)
                                            if visibility else EC.presence_of_all_elements_located(locator))

    def do_element_exist(self, locator, timeout=10) -> bool:
        try:
            self.find_element(locator, timeout)
        except TimeoutException:
            return False
        return True
