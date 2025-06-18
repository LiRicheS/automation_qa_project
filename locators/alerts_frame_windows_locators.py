from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    TAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
    WINDOW_BUTTON = (By.XPATH, "//button[@id='windowButton']")
    WINDOW_MESSAGE_BUTTON = (By.XPATH, "//button[@id='messageWindowButton']")
    H1 = (By.XPATH, "//h1")
    WINDOW_MESSAGE_TEXT = (By.XPATH, "//body")


class AlertsPageLocators:
    ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")
    TIMER_ALERT_BUTTON = (By.XPATH, "//button[@id='timerAlertButton']")

    CONFIRM_BUTTON = (By.XPATH, "//button[@id='confirmButton']")
    CONFIRM_ALERT_RESULT = (By.XPATH, "//span[@id='confirmResult']")

    PROMPT_BUTTON = (By.XPATH, "//button[@id='promtButton']")
    PROMPT_ALERT_RESULT = (By.XPATH, "//span[@id='promptResult']")


class FramesPageLocators:
    FIRST_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    SECOND_FRAME = (By.XPATH, "//iframe[@id='frame2']")

    H1_ON_FRAME = (By.XPATH, "//h1[@id='sampleHeading']")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    PARENT_FRAME_TEXT = (By.XPATH, "//body")

    CHILD_FRAME = (By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']")
    CHILD_FRAME_TEXT = (By.XPATH, "//p")


class ModalsDialogsPageLocators:
    BUTTON_SMALL_MODAL = (By.XPATH, "//button[@id='showSmallModal']")
    BUTTON_LARGE_MODAL = (By.XPATH, "//button[@id='showLargeModal']")

    # small modal _ info
    TITLE_SMALL_MODAL = (By.XPATH, "//div[@class='modal-title h4']")
    TEXT_SMALL_MODAL = (By.XPATH, "//div[@class='modal-body']")
    CLOSE_SMALL_MODAL_BUTTON = (By.XPATH, "//button[@id='closeSmallModal']")

    # large modal _ info
    TITLE_LARGE_MODAL = (By.XPATH, "//div[@class='modal-title h4']")
    TEXT_LARGE_MODAL = (By.XPATH, "//div[@class='modal-body']//p")
    CLOSE_LARGE_MODAL_BUTTON = (By.XPATH, "//button[@id='closeLargeModal']")
