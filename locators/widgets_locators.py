from selenium.webdriver.common.by import By


class AccordianPageLocators:
    ACCORDIAN_1 = (By.XPATH, "//div[@id='section1Heading']")
    ACCORDIAN_SECTION_1 = (By.XPATH, "//div[@id='section1Content']")

    ACCORDIAN_2 = (By.XPATH, "//div[@id='section2Heading']")
    ACCORDIAN_SECTION_2 = (By.XPATH, "//div[@id='section2Content']")

    ACCORDIAN_3 = (By.XPATH, "//div[@id='section3Heading']")
    ACCORDIAN_SECTION_3 = (By.XPATH, "//div[@id='section3Content']")


