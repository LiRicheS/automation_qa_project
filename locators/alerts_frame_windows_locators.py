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
