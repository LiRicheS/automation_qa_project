import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.join(os.getcwd(), "downloads"),
}

@pytest.fixture(scope='function')
def driver():
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.page_load_strategy = 'eager'
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    # driver.quit() опционален, так как мы используем service, а он отвечает за открытие и закрытие браузера


@pytest.fixture(scope='function')
def driver_no_incognito():
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.page_load_strategy = 'eager'
    service = Service(executable_path=ChromeDriverManager().install())
    driver_no_incognito = webdriver.Chrome(service=service, options=options)
    driver_no_incognito.maximize_window()
    yield driver_no_incognito
    # driver.quit() опционален, так как мы используем service, а он отвечает за открытие и закрытие браузера
