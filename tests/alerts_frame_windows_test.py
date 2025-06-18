import random
import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, ModalsDialogsPage


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


class TestNestedFramesPage:

    def test_check_frames(self, driver):
        nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
        nested_frames_page.open()

        result_info = nested_frames_page.check_nested_frame()
        assert result_info['parent_text'] == "Parent frame", "Nested frame is not a parent frame"
        assert result_info['child_text'] == "Child Iframe", "Nested frame is not a child frame"


class TestModalsDialogsPage:

    def test_small_modal(self, driver):
        modals_dialogs_page = ModalsDialogsPage(driver, "https://demoqa.com/modal-dialogs")
        modals_dialogs_page.open()
        result = modals_dialogs_page.check_modal_dialogs(modal="small")

        assert result['small_title'] == "Small Modal", "Modal-title is not match"
        assert result['small_text'] == "This is a small modal. It has very less content", "Modal-text is not match"
        # print(result['status_is_close'])

    def test_large_modal(self, driver):
        modals_dialogs_page = ModalsDialogsPage(driver, "https://demoqa.com/modal-dialogs")
        modals_dialogs_page.open()
        result = modals_dialogs_page.check_modal_dialogs(modal="large")

        assert result['large_title'] == "Large Modal", "Modal-title is not match"
        assert result['large_text'] == "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", "Modal-text is not match"
        # print(result['status_is_close'])
