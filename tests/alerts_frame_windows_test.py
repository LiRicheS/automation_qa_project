import random
import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage


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


class TestFramesPage:
    def test_check_frame1(self, driver):
        frames_page = FramesPage(driver, "https://demoqa.com/frames")
        frames_page.open()

        result_info = frames_page.check_frame(iframe_name='frame1')
        assert result_info['width'] == '500px', "Frame width is not 500px"
        assert result_info['height'] == '350px', "Frame height is not 350px"
        assert result_info['h1_text'] == 'This is a sample page', "Frame h1_text is not a sample page"

    def test_check_frame2(self, driver):
        frames_page = FramesPage(driver, "https://demoqa.com/frames")
        frames_page.open()

        result_info = frames_page.check_frame(iframe_name='frame2')
        assert result_info['width'] == '100px', "Frame width is not 100px"
        assert result_info['height'] == '100px', "Frame height is not 100px"
        assert result_info['h1_text'] == 'This is a sample page', "Frame h1_text is not a sample page"

