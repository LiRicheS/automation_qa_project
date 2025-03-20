from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait

"""Теперь нам нужно реализовать нашу, базовую страницу. Она будет использовать нам драйвер.
Это класс, от которого будут наследоваться, все остальные наши страницы.
"""


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    """ Get and opened specified URL """
    def open(self):
        self.driver.get(self.url)

    """ Waiting, until element is visible """
    def element_is_visible(self, locator: Tuple[str, str], timeout: int = 5):  # locator = ("xpath", "//a[@id=2]")
        # возвращает веб-элемент
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
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





