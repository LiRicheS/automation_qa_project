from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # forms_fields
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit"]')

    # created_form
    CREATED_FULL_NAME = (By.XPATH, "(//div[@id='output']//p)[1]")
    CREATED_EMAIL = (By.XPATH, "(//div[@id='output']//p)[2]")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "(//div[@id='output']//p)[3]")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "(//div[@id='output']//p)[4]")


