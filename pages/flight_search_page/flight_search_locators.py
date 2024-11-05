from selenium.webdriver.common.by import By


###################### date choice locators ###############################################################
DEPARTING_INPUT_FILED = (By.XPATH, "//div[@data-react-toolbox='date-picker']//label[text()='Departing']")
RETURNING_INPUT_FILED = (By.XPATH, "//div[@data-react-toolbox='date-picker']//label[text()='Returning']")
ACTIVATED_CALENDAR_DAYS_BUTTONS = (By.CSS_SELECTOR, "div[data-react-toolbox='day']"
                                                    ":not([class*='theme__disabled___2N4Gy'])")
OK_BUTTON = (By.XPATH, "//button[text()='Ok']")
CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
DEPARTURE_DATE_FILED = (By.XPATH, "//div[@data-react-toolbox='date-picker']"
                                  "//label[text()='Departing']/preceding-sibling::input")
RETURN_DATE_FILED = (By.XPATH, "//div[@data-react-toolbox='date-picker']"
                                  "//label[text()='Returning']/preceding-sibling::input")
#################### Passengers choice  locators ###########################################################
ADULTS_INPUT_FILED = (By.XPATH, "//label[text()='Adults (18+)']//preceding-sibling::input")
ADULTS_NUMBER_DROP_DOWN_BUTTONS = (By.XPATH, "//label[text()='Adults (18+)']//parent::div//"
                                             "following-sibling::ul[contains(@class,'WhiteDropDown')]//li")
CHILDREN_INPUT_FILED = (By.XPATH, "//label[contains(text(),'Children')]//preceding-sibling::input")
CHILDREN_NUMBER_DROP_DOWN_BUTTONS = (By.XPATH, "//label[contains, (text(),'Children')]//parent::div//"
                                             "following-sibling::ul[contains(@class,'WhiteDropDown')]//li")

#####################            Others          ############################################################
SELECT_DESTINATION_BTN = (By.XPATH, "//button[contains(text(), 'Select Destination')]")