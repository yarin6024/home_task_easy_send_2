from selenium.webdriver.common.by import By

DESTINATIONS_CARDS = (By.XPATH, "//div[@data-react-toolbox='card']")
DESTINATIONS_NAME_FILED = (By.XPATH, "//div[@data-react-toolbox='card']//*[contains(@class, 'title')]")
LUNCH_DESTINATION_BTN = (By.XPATH, "//li[text()='Launch']/ancestor::div[@data-react-toolbox='dropdown']"
                                   "//input[contains(@class, 'BlackDropDown')]")
PLANET_COLOR_BTN = (By.XPATH, "//li[text()='Planet color']/ancestor::div[@data-react-toolbox='dropdown']"
                    "//input[contains(@class, 'BlackDropDown')]")
DESTINATIONS_BUTTONS = (By.XPATH, "//li[text()='Launch']//following-sibling::li")
PLANET_COLOR_BUTTONS = (By.XPATH, "//li[text()='Planet color']//following-sibling::li")
BOOK_BUTTONS = (By.CSS_SELECTOR, "[class*='BookButton']")
PRICE_FILED = (By.CSS_SELECTOR, "[class*='price-tag']")
PRICE_SLIDER = (By.CSS_SELECTOR, "[class*='Slider__progress']")
PRICE_RANGES_IN_SLIDER = (By.CSS_SELECTOR, "[class*='Gallery__price-filter'] input[type='text']")
OPTION_PLANET_COLOR_IN_DROP_DOWN_OPTIONS = (By.XPATH, "//li[text()='Planet color']")
OPTION_LAUNCH_IN_DROP_DOWN_OPTIONS = (By.XPATH, "//li[text()='Launch']")