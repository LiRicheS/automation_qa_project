import random
import time

from selenium.webdriver import Keys

from locators.alerts_frame_windows_locators import (BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators,
                                                    NestedFramesPageLocators, ModalsDialogsPageLocators)

from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException, TimeoutException


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def open_new_tab(self):
        main_tab = self.get_current_window_handle()

        self.go_to_element(self.elements_is_clickable(self.locators.TAB_BUTTON))
        self.element_is_visible(self.locators.TAB_BUTTON).click()
        list_tab = self.get_all_open_window_tab()

        self.switch_to_window(list_tab[1])
        open_tab_url = self.get_current_url()

        open_tab = self.get_current_window_handle()

        text_h1 = self.element_is_present(self.locators.H1).text
        return {
            'main_tab': main_tab,
            'open_tab': open_tab,
            'open_tab_url': open_tab_url,
            'text_h1': text_h1,
        }

    def open_new_window(self):
        main_window = self.get_current_window_handle()
        main_size = self.get_window_size()

        self.go_to_element(self.elements_is_clickable(self.locators.WINDOW_BUTTON))
        self.element_is_visible(self.locators.WINDOW_BUTTON).click()
        list_windows = self.get_all_open_window_tab()

        self.switch_to_window(list_windows[1])

        new_window_size = self.driver.get_window_size()
        is_new_window_different_size = new_window_size != main_size

        current_url = self.get_current_url()
        text_h1 = self.element_is_present(self.locators.H1).text
        current_handle = self.get_current_window_handle()

        return {
            'main_window': main_window,
            'open_window': current_handle,
            'open_window_url': current_url,
            'text_h1': text_h1,
            'is_different_size': is_new_window_different_size
        }

    def open_new_window_message(self):
        main_window = self.get_current_window_handle()

        self.go_to_element(self.elements_is_clickable(self.locators.WINDOW_MESSAGE_BUTTON))
        self.element_is_visible(self.locators.WINDOW_MESSAGE_BUTTON).click()
        list_windows = self.get_all_open_window_tab()

        self.switch_to_window(list_windows[1])
        open_window = self.get_current_window_handle()

        return {
            'main_window': main_window,
            'open_window': open_window,
        }


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def click_button_to_see_alert(self):
        self.go_to_element(self.element_is_visible(self.locators.ALERT_BUTTON))
        self.element_is_visible(self.locators.ALERT_BUTTON).click()

        try:
            alert = self.alert_is_present()
            alert.accept()
            return True

        except NoAlertPresentException:
            # Alert не подтвердился
            return False

    def click_button_alert_will_appear_after_5_seconds(self):
        self.go_to_element(self.element_is_visible(self.locators.TIMER_ALERT_BUTTON))
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()

        try:
            alert = self.alert_is_present(timeout=5)
            alert.accept()
            return True
        except TimeoutException:
            return False

    def click_button_alert_to_confirm(self, confirm="accept"):  # accept/ dismiss
        self.go_to_element(self.element_is_visible(self.locators.CONFIRM_BUTTON))
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        data_result = []

        if confirm == "accept":
            alert = self.alert_is_present()
            self.switch_to_alert()
            alert.accept()

            data_result.append("You selected Ok")

        elif confirm == "dismiss":
            alert = self.alert_is_present()
            self.switch_to_alert()
            alert.dismiss()

            data_result.append("You selected Cancel")

        data_result.append(self.element_is_present(self.locators.CONFIRM_ALERT_RESULT).text)
        return data_result

    def click_button_alert_to_fill_text(self):
        self.go_to_element(self.element_is_visible(self.locators.PROMPT_BUTTON))
        self.element_is_visible(self.locators.PROMPT_BUTTON).click()
        data_result = []

        try:
            alert = self.alert_is_present()
            self.switch_to_alert()
            alert.send_keys("Pavel")
            alert.accept()
            data_result.append("You entered Pavel")
            data_result.append(self.element_is_present(self.locators.PROMPT_ALERT_RESULT).text)
            return data_result

        except NoAlertPresentException:
            # Alert не подтвердился
            return False


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, iframe_name: str) -> dict:
        frame_map = {
            "frame1": self.locators.FIRST_FRAME,
            "frame2": self.locators.SECOND_FRAME
        }

        frame = self.element_is_present(frame_map[iframe_name])
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')

        self.driver.switch_to.frame(frame)
        h1_text = self.element_is_present(self.locators.H1_ON_FRAME).text

        self.driver.switch_to.default_content()

        return {
            "width": width,
            "height": height,
            "h1_text": h1_text
        }


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text

        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text

        result_info = {
            "parent_text": parent_text,
            "child_text": child_text,
        }

        return result_info


class ModalsDialogsPage(BasePage):
    locators = ModalsDialogsPageLocators()

    def check_modal_dialogs(self, modal="small"):
        if modal == "small":
            self.go_to_element(self.element_is_visible(self.locators.BUTTON_SMALL_MODAL))
            self.element_is_visible(self.locators.BUTTON_SMALL_MODAL).click()
            small_title = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
            small_text = self.element_is_visible(self.locators.TEXT_SMALL_MODAL).text
            status_is_close = self.element_is_visible(self.locators.CLOSE_SMALL_MODAL_BUTTON).click()

            result_info = {
                "small_title": small_title,
                "small_text": small_text,
                "status_is_close": status_is_close
            }

            return result_info

        elif modal == "large":
            self.go_to_element(self.element_is_visible(self.locators.BUTTON_LARGE_MODAL))
            self.element_is_visible(self.locators.BUTTON_LARGE_MODAL).click()
            small_title = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
            small_text = self.element_is_visible(self.locators.TEXT_LARGE_MODAL).text
            status_is_close = self.element_is_visible(self.locators.CLOSE_LARGE_MODAL_BUTTON).click()

            result_info = {
                "large_title": small_title,
                "large_text": small_text,
                "status_is_close": status_is_close
            }

            return result_info
