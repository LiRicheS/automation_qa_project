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


class CheckboxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    ITEMS_LIST = (By.XPATH, "//span[@class='rct-title']")
    RESULT_CHECKED = (By.XPATH, "//span[@class='text-success']")

    STATUS_CHECKBOXES_DICT = {
        'home': (By.XPATH, "//label[@for='tree-node-home']"),

        'desktop': (By.XPATH, "//label[@for='tree-node-desktop']"),

        'notes': (By.XPATH, "//label[@for='tree-node-notes']"),

        'commands': (By.XPATH, "//label[@for='tree-node-commands']"),

        'documents': (By.XPATH, "//label[@for='tree-node-documents']"),

        'workspace': (By.XPATH, "//label[@for='tree-node-workspace']"),

        'react': (By.XPATH, "//label[@for='tree-node-react']"),

        'angular': (By.XPATH, "//label[@for='tree-node-angular']"),

        'veu': (By.XPATH, "//label[@for='tree-node-veu']"),

        'office': (By.XPATH, "//label[@for='tree-node-office']"),

        'public': (By.XPATH, "//label[@for='tree-node-public']"),

        'private': (By.XPATH, "//label[@for='tree-node-private']"),

        'classified': (By.XPATH, "//label[@for='tree-node-classified']"),

        'general': (By.XPATH, "//label[@for='tree-node-general']"),

        'downloads': (By.XPATH, "//label[@for='tree-node-downloads']"),

        'wordFile': (By.XPATH, "//label[@for='tree-node-wordFile']"),

        'excelFile': (By.XPATH, "//label[@for='tree-node-excelFile']"),
    }





