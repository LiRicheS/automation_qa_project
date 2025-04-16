import random
import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestBrowserWindowsPage:
    def test_open_new_tab(self, driver):
        browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        browser_windows_page.open()

        result = browser_windows_page.open_new_tab()

        assert result['main_tab'] != result['open_tab'], "New tab is not opened"
        assert result['open_tab_url'] == "https://demoqa.com/sample", "Url new-page is don`t match '...demoqa.com/sample'"
        assert result['text_h1'] == "This is a sample page", "Text in h1 is don`t match 'This is a sample page'"

    def test_open_new_window(self, driver):
        browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        browser_windows_page.open()

        result = browser_windows_page.open_new_window()

        assert result['main_window'] != result['open_window'], "New window is not opened"
        assert result['open_window_url'] == "https://demoqa.com/sample", "Url new-page is don`t match '...demoqa.com/sample'"
        assert result['text_h1'] == "This is a sample page", "Text in h1 is don`t match 'This is a sample page'"
        assert result['is_different_size'] is True, "It seems the page was opened as a tab, not a separate window"

    def test_open_new_window_message(self, driver):
        browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        browser_windows_page.open()

        result = browser_windows_page.open_new_window_message()

        assert result['main_window'] != result['open_window'], "New window is not opened"


class TestAlertsPage:

    def test_button_to_see_alert(self, driver):
        alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
        alerts_page.open()

        assert alerts_page.click_button_to_see_alert() is True, "Alert is not open or confirmed"

    def test_button_alert_appear_after_5_seconds(self, driver):
        alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
        alerts_page.open()

        assert alerts_page.click_button_alert_will_appear_after_5_seconds() is True, "Alert is didn`t appear after 5 seconds"

    def test_button_alert_to_confirm(self, driver):
        alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
        alerts_page.open()

        result_is_accept = alerts_page.click_button_alert_to_confirm(confirm="accept")
        assert result_is_accept[0] == result_is_accept[1], "Alert is didn`t confirm"

        result_is_dismiss = alerts_page.click_button_alert_to_confirm(confirm="dismiss")
        assert result_is_dismiss[0] == result_is_dismiss[1], "Alert is didn`t unconfirm"

    def test_button_alert_to_fill_text_prompt(self, driver):
        alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
        alerts_page.open()

        result = alerts_page.click_button_alert_to_fill_text()
        assert result[0] == result[1], "Alert is didn`t fill text"

