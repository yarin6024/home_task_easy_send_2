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


# Configur logger
logging.basicConfig(
    filename='test_log.log',  # Log file name
    level=logging.INFO,       # Logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a logger object
logger = logging.getLogger(__name__)
