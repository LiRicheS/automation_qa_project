from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait

"""Теперь нам нужно реализовать нашу, базовую страницу. Она будет использовать нам драйвер.
Это класс, от которого будут наследоваться, все остальные наши страницы.
"""


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.action = ActionChains(driver)

    """ Get and opened specified URL """
    def open(self):
        self.driver.get(self.url)

    """ Waiting, until element is visible """
    def element_is_visible(self, locator: Tuple[str, str], timeout: int = 5, message=None):  # locator = ("xpath", "//a[@id=2]")
        # возвращает веб-элемент
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator), message=message)
        # visibility_of_element_located : Ожидает, что элемент станет видимым.

    """ Waiting, until are elements is visible """
    def elements_are_visible(self, locator: Tuple[str, str], timeout: int = 5):
        # возвращает веб-элемент
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        # visibility_of_all_elements_located : Ожидает, что элементЫ станут видимыми.

    """ Waiting, until element is invisible """
    def element_is_invisible(self, locator: Tuple[str, str], timeout: int = 5):
        # возвращает веб-элемент
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        # invisibility_of_element_located : Ожидает, что элемент станет невидимым.

    """ Waiting, until element is present """
    def element_is_present(self, locator: Tuple[str, str], timeout: int = 5):
        # возвращает веб-элемент
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        # presence_of_element_located : Ожидает, что элемент будет присутствовать в DOM

    """ Waiting, until are elements is present """
    def elements_are_present(self, locator: Tuple[str, str], timeout: int = 5):
        # возвращает веб-элемент
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        # presence_of_all_elements_located : Ожидает, что элементЫ будут присутствовать в DOM

    """ Waiting, until are element is clickable """
    def elements_is_clickable(self, locator: Tuple[str, str], timeout: int = 5):
        # возвращает веб-элемент
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        # element_to_be_clickable : Ожидает, что элемент станет кликабельным.

    """ Scroll to element """
    def go_to_element(self, element: WebElement):
        return self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        # Позволяет проскролить к нужному нам, веб-элементу

    """ Refresh page"""
    def refresh_page(self):
        return self.driver.refresh()

    def close_tab(self):
        return self.driver.close()

    """ Get All Open Window-Tab"""
    def get_all_open_window_tab(self):
        return self.driver.window_handles

    """ Switch to Window-Tab"""
    def switch_to_window(self, window):
        self.driver.switch_to.window(window)

    """ Get Current URL Page"""
    def get_current_url(self):
        return self.driver.current_url

    """ Get Current Handle Page"""
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    """ Get window size"""
    def get_window_size(self):
        return self.driver.get_window_size()

    """ Alert is present"""
    def alert_is_present(self, timeout: int = 5):
        return wait(self.driver, timeout).until(EC.alert_is_present())

    """ Switch to alert """
    def switch_to_alert(self):
        return self.driver.switch_to.alert
