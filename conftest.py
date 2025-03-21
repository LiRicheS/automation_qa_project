import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()


@pytest.fixture(scope='function')
def driver():
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--incognito')
    # options.page_load_strategy = 'eager'
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    # driver.quit() опционален, так как мы используем service, а он отвечает за открытие и закрытие браузера
