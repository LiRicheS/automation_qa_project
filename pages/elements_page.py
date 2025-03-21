import random

from generator.generator import generate_data_person
from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import CheckboxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    """ Filling all fields """

    def fill_all_fields(self):
        person_info = next(generate_data_person())  # Создаётся объект класса с заполненными полями благодаря yield
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return full_name, email, current_address, permanent_address

    """ Get text from fields """

    def get_text_from_fields(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]  # ('Name:Fomin Ivan')
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
        # Если не split , то возвращает кортеж ('Name':'Fomin Ivan'..)


class CheckBoxPage(BasePage):
    locators = CheckboxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def check_selected_checkboxes(self):
        selected_items = []
        for result in self.elements_are_present(self.locators.RESULT_CHECKED):
            selected_items.append(result.text)
            # Получаем список "desktop notes commands office..."

        for name, locator in self.locators.STATUS_CHECKBOXES_DICT.items():
            if name in selected_items:  # Если название чекбокса есть в выходных данных
                checkbox_input = self.element_is_present((locator[0], locator[1] + "/input"))  # Ищем input
                assert checkbox_input.is_selected(), f"Ошибка: чекбокс '{name}' не выбран!"

    def choice_random_checkbox(self):
        items_list = self.elements_are_visible(self.locators.ITEMS_LIST)
        count = 21
        while count > 0:
            item = items_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                self.check_selected_checkboxes()
                self.go_to_element(item)
                count -= 1
            else:
                break

    # Крч идея в чём, мы получаем, выходные названия. И дальше смотрим они есть в in @for label, если да.
    # То мы чекаем //label//input он должен вернуть True, если нет, то ошибка, что не выбран.
