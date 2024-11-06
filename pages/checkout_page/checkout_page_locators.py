from selenium.webdriver.common.by import By

NAME_FILED = (By.XPATH, "//span[text()='Name']//preceding-sibling::input")
EMAIL_ADDRESS_FILED = (By.XPATH, "//span[text()='Email Address']//preceding-sibling::input")
SOCIAL_SECURITY_NUM_FILED = (By.XPATH, "//span[text()='Social Security Number']//preceding-sibling::input")
PHONE_NUM_FILED = (By.XPATH, "//span[text()='Phone Number']//preceding-sibling::input")
PROMO_CODE_FILED = (By.CSS_SELECTOR, "input[name='promo']")
APPLY_BTN = (By.CSS_SELECTOR, "[class*='apply-button']")
PAY_BTN = (By.CSS_SELECTOR, "[class*='pay-button']")
AGREE_WITH_TERMS_CHECKBOX = (By.CSS_SELECTOR, "div[class*='check']")
PRICE_PER_TRAVELER = (By.XPATH, "//div[contains(text(), 'traveler')]/following-sibling::div")
TRAVELERS_NUM_FILED = (By.XPATH, "//div[contains(text(), 'traveler')]")
TOTAL_PRICE_FILED = (By.CSS_SELECTOR, "[class*='OrderSummary__price'] strong")