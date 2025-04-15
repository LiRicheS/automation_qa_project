import random

from selenium.webdriver.common.by import By


class FormsPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    MOBILE_NUMBER = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput']")

    SUBJECT = (By.XPATH, "//input[@id='subjectsInput']")
    SUBJECT_SELECT = (By.XPATH, "//div[@id='react-select-2-option-0']")
    SUBJECT_STATUS = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue subjects-auto-complete__multi-value']")

    # Gender
    num_gender = random.randint(1, 3)
    GENDER = (By.XPATH, f"//label[@for='gender-radio-{num_gender}']")
    GENDER_STATUS = (By.XPATH, f"//input[@id='gender-radio-{num_gender}']")

    # Hobbies
    num_hobbies = random.randint(1, 3)
    HOBBIES_STATUS = (By.XPATH, f"//input[@id='hobbies-checkbox-{num_hobbies}']")
    HOBBIES_CHECKBOX = (By.XPATH, f"//label[@for='hobbies-checkbox-{num_hobbies}']")

    # READING_STATUS = (By.XPATH, "//input[@id='hobbies-checkbox-2']")
    # READING_CHECKBOX = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    #
    # MUSIC_STATUS = (By.XPATH, "//input[@id='hobbies-checkbox-3']")
    # MUSIC_CHECKBOX = (By.XPATH, "//label[@for='hobbies-checkbox-3']")

    PICTURE_FILE_BUTTON = (By.XPATH, "//input[@id='uploadPicture']")

    CURRENT_ADDRESS = (By.XPATH, "//textarea[@placeholder='Current Address']")

    # State
    num_states = random.randint(0, 3)
    SELECT_STATES = (By.XPATH, "(//div[@class=' css-1wa3eu0-placeholder'])[1]")
    RANDOM_SELECT_STATE = (By.XPATH, f"//div[@id='react-select-3-option-{num_states}']")
    # NCR = (By.XPATH, "//div[@id='react-select-3-option-0']")
    # UTTAR_PRADESH = (By.XPATH, "//div[@id='react-select-3-option-1']")
    # HARYANA = (By.XPATH, "//div[@id='react-select-3-option-2']")
    # RAJASTHAN = (By.XPATH, "//div[@id='react-select-3-option-3']")

    # City
    num_city = random.randint(0, 1)
    SELECT_CITY = (By.XPATH, "//div[@class=' css-yk16xz-control']")
    RANDOM_SELECT_CITY = (By.XPATH, f"//div[@id='react-select-4-option-{num_city}']")

    # DELHI = (By.XPATH, "//div[@id='react-select-4-option-0']")
    # GURGAON = (By.XPATH, "//div[@id='react-select-4-option-1']")
    # NOIDA = (By.XPATH, "//div[@id='react-select-4-option-2']")

    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    # Tables result fillings
    TABLE_RESULT = (By.XPATH, "//div[@class='table-responsive']//td[2]")

