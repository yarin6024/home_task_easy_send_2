import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def driver(request: pytest.FixtureRequest) -> WebDriver:
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    web_driver.get(request.param['url'])
    with web_driver:
        yield web_driver
