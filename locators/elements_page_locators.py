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


class RadioButtonPageLocators:
    RADIO_BUTTON_LIST_STATUS = (By.XPATH, "//input[@name='like']")
    YES_RADIOBUTTON = (By.XPATH, "//label[@for='yesRadio']")
    # YES_RADIOBUTTON_STATUS = (By.XPATH, "//input[@id='yesRadio']")

    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[@for='impressiveRadio']")
    # IMPRESSIVE_RADIOBUTTON_STATUS = (By.XPATH, "//input[@id='impressiveRadio']")

    NO_RADIOBUTTON = (By.XPATH, "//label[@for='noRadio']")
    NO_RADIOBUTTON_STATUS = (By.XPATH, "//input[@id='noRadio']")


class WebTablesPageLocators:
    # control_button
    ADD_PERSON_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")

    # ADD_PERSON_FIELD
    FIRSTNAME_FIELD = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_FIELD = (By.XPATH, "//input[@id='lastName']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='userEmail']")
    AGE_FIELD = (By.XPATH, "//input[@id='age']")
    SALARY_FIELD = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_FIELD = (By.XPATH, "//input[@id='department']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    # tables_people
    FULL_PEOPLE_LIST = (By.XPATH, "//div[@class='rt-tr-group']")

    SEARCH_FIELD = (By.XPATH, "//input[@id='searchBox']")
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = (By.XPATH, ".//ancestor::div[@class='rt-tr-group']")

    SELECT_BUTTON_ROWS = (By.CSS_SELECTOR, "span[class='select-wrap -pageSizeOptions']")
    COUNT_ROWS_VALUE = (By.XPATH, "//option")
    SELECT = (By.CSS_SELECTOR, "select[aria-label='rows per page']")


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.XPATH, "//button[@id='doubleClickBtn']")
    INFO_DCBTN = (By.XPATH, "//p[@id='doubleClickMessage']")

    RIGHT_CLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    INFO_RCB = (By.XPATH, "//p[@id='rightClickMessage']")

    CLICK_BUTTON = (By.XPATH, "(//button[contains(text(),'Click Me')])[3]")
    INFO_CLICKBTN = (By.XPATH, "//p[@id='dynamicClickMessage']")


class LinksPageLocators:
    # links that open in new tab
    HOME_LINK = (By.XPATH, "//a[@id='simpleLink']")
    DYNAMIC_LINK = (By.XPATH, "//a[@id='dynamicLink']")

    # links that send an api call
    CREATED_LINK = (By.XPATH, "//a[@id='created']")
    NO_CONTENT_LINK = (By.XPATH, "//a[@id='no-content']")
    MOVED_LINK = (By.XPATH, "//a[@id='moved']")
    BAD_REQUEST_LINK = (By.XPATH, "//a[@id='bad-request']")
    UNAUTHORIZED_LINK = (By.XPATH, "//a[@id='unauthorized']")
    FORBIDDEN_LINK = (By.XPATH, "//a[@id='forbidden']")
    NOT_FOUND_LINK = (By.XPATH, "//a[@id='invalid-url']")

    LIST_CHECK_STATUS_API_LINK = (By.XPATH, "//p//b")  # ['status-code', 'Message']


class UploadDownloadPageLocators:
    DOWNLOAD_BUTTON = (By.XPATH, "//a[@id='downloadButton']")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOAD_PATH_INFO = (By.XPATH, "//p[@id='uploadedFilePath']")
