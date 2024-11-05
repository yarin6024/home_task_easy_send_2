from selenium.webdriver.common.by import By


###################### date choice locators ###############################################################
DEPARTING_INPUT_FILED = (By.XPATH, "//div[@data-react-toolbox='date-picker']//label[text()='Departing']/preceding-sibling::input")
RETURNING_INPUT_FILED = (By.XPATH, "//div[@data-react-toolbox='date-picker']//label[text()='Returning']/preceding-sibling::input")
ACTIVATED_CALENDAR_DAYS_BUTTONS = (By.CSS_SELECTOR, "div[data-react-toolbox='day']"
                                                    ":not([class*='theme__disabled___2N4Gy'])")
OK_BUTTON = (By.XPATH, "//button[text()='Ok']")
CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
DEPARTURE_DATE_FILED = (By.XPATH, "//div[@data-react-toolbox='date-picker']"
                                  "//label[text()='Departing']/preceding-sibling::input")
RETURN_DATE_FILED = (By.XPATH, "//div[@data-react-toolbox='date-picker']"
                                  "//label[text()='Returning']/preceding-sibling::input")
#################### Passengers choice  locators ###########################################################
ADULTS_INPUT_FILED = (By.XPATH, "//input[@value='Adults (18+)']")
ADULTS_NUMBER_DROP_DOWN_BUTTONS = (By.XPATH, "//input[@value='Adults (18+)']//parent::div"
                                             "//following-sibling::ul[contains(@class,'WhiteDropDown')]//li")
CHILDREN_INPUT_FILED = (By.XPATH, "//input[contains(@value,'Children')]")
CHILDREN_NUMBER_DROP_DOWN_BUTTONS = (By.XPATH, "//input[contains(@value,'Children')]//parent::div//"
                                             "following-sibling::ul[contains(@class,'WhiteDropDown')]//li")

#####################            Others          ############################################################
SELECT_DESTINATION_BTN = (By.XPATH, "//button[contains(text(), 'Select Destination')]")