import random
import time

from selenium.webdriver import Keys
from generator.generator import generate_data_person
from locators.elements_page_locators import (TextBoxPageLocators, CheckboxPageLocators, RadioButtonPageLocators,
                                             WebTablesPageLocators, ButtonsPageLocators)
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
                checkbox_input = self.element_is_present(
                    (locator[0], locator[1] + "/input"))  # Ищем input ("xpath", "//label[@id=1]"+"/input")
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


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def choice_yes_radio_buttons(self):
        self.elements_is_clickable(self.locators.YES_RADIOBUTTON).click()
        self.checked_radio_buttons_true("yesRadio")

    def choice_no_radio_buttons(self):
        self.elements_is_clickable(self.locators.NO_RADIOBUTTON).click()
        assert self.element_is_present(self.locators.NO_RADIOBUTTON_STATUS).is_selected() is False, "No is selected!"

    def choice_impressive_radio_buttons(self):
        self.elements_is_clickable(self.locators.IMPRESSIVE_RADIOBUTTON).click()
        self.checked_radio_buttons_true("impressiveRadio")

    def checked_radio_buttons_true(self, radio_button_id):
        radiobuttons = self.elements_are_present(self.locators.RADIO_BUTTON_LIST_STATUS)
        count_checked = 0
        id_checked = []
        for radio_button in radiobuttons:
            if radio_button.get_attribute("id") == radio_button_id:  # yesRadio impressiveRadio noRadio
                assert radio_button.is_selected() is True, f"{radio_button_id} is not selected!"
            if radio_button.is_selected():
                count_checked += 1
                id_checked.append(radio_button.get_attribute("id"))

        assert count_checked == 1, f"Selected is {id_checked}"


class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    def add_new_persons(self, count=1):
        data = []
        while count != 0:
            add_person = next(generate_data_person())
            first_name = add_person.first_name
            last_name = add_person.last_name
            email = add_person.email
            age = add_person.age
            salary = add_person.salary
            department = add_person.department

            self.elements_is_clickable(self.locators.ADD_PERSON_BUTTON).click()

            assert self.element_is_visible(self.locators.FIRSTNAME_FIELD).get_attribute("value") == "", "Firstname is not empty!"
            self.element_is_visible(self.locators.FIRSTNAME_FIELD).send_keys(first_name)

            assert self.element_is_visible(self.locators.LASTNAME_FIELD).get_attribute("value") == "", "lastName is not empty!"
            self.element_is_visible(self.locators.LASTNAME_FIELD).send_keys(last_name)

            assert self.element_is_visible(self.locators.EMAIL_FIELD).get_attribute("value") == "", "email is not empty!"
            self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)

            assert self.element_is_visible(self.locators.AGE_FIELD).get_attribute("value") == "", "age is not empty!"
            self.element_is_visible(self.locators.AGE_FIELD).send_keys(age)

            assert self.element_is_visible(self.locators.SALARY_FIELD).get_attribute("value") == "", "salary is not empty!"
            self.element_is_visible(self.locators.SALARY_FIELD).send_keys(salary)

            assert self.element_is_visible(self.locators.DEPARTMENT_FIELD).get_attribute("value") == "", "department is not empty!"
            self.element_is_visible(self.locators.DEPARTMENT_FIELD).send_keys(department)

            self.elements_is_clickable(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            data.append([first_name, last_name, age, email, salary, department])
        return data

    def get_all_people(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for person in people_list:
            data.append(person.text.splitlines())  #name\nlast_name\n => ['name', 'last_name']
        return data

    def search_people_in_table(self, key_words):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_words)

    def checked_search_people_in_table(self):
        delete_buttons = self.elements_are_present(self.locators.DELETE_BUTTON)
        row_data = []
        for delete_button in delete_buttons:
            row = delete_button.find_element(*self.locators.ROW_PARENT)
            row_data.append(tuple(row.text.splitlines()))
        return row_data

    def update_info_person(self):
        edit_buttons = self.elements_are_present(self.locators.EDIT_BUTTON)
        edit_button = edit_buttons[random.randint(0, len(edit_buttons) - 1)]
        self.go_to_element(edit_button)
        before_row_person = edit_button.find_element(*self.locators.ROW_PARENT).text.splitlines()
        row_person = before_row_person.copy()
        edit_button.click()

        person_info_for_create = next(generate_data_person())
        first_name = person_info_for_create.first_name
        last_name = person_info_for_create.last_name
        email = person_info_for_create.email
        age = person_info_for_create.age
        salary = person_info_for_create.salary
        department = person_info_for_create.department

        field = random.randint(0, 5)
        if field == 0:
            self.element_is_visible(self.locators.FIRSTNAME_FIELD).clear()
            self.element_is_visible(self.locators.FIRSTNAME_FIELD).send_keys(first_name)
            self.elements_is_clickable(self.locators.SUBMIT_BUTTON).click()
            row_person[field] = first_name

        elif field == 1:
            self.element_is_visible(self.locators.LASTNAME_FIELD).clear()
            self.element_is_visible(self.locators.LASTNAME_FIELD).send_keys(last_name)
            self.elements_is_clickable(self.locators.SUBMIT_BUTTON).click()
            row_person[field] = last_name

        elif field == 2:
            self.element_is_visible(self.locators.AGE_FIELD).clear()
            self.element_is_visible(self.locators.AGE_FIELD).send_keys(age)
            self.elements_is_clickable(self.locators.SUBMIT_BUTTON).click()
            row_person[field] = age

        elif field == 3:
            self.element_is_visible(self.locators.EMAIL_FIELD).clear()
            self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
            self.elements_is_clickable(self.locators.SUBMIT_BUTTON).click()
            row_person[field] = email

        elif field == 4:
            self.element_is_visible(self.locators.SALARY_FIELD).clear()
            self.element_is_visible(self.locators.SALARY_FIELD).send_keys(salary)
            self.elements_is_clickable(self.locators.SUBMIT_BUTTON).click()
            row_person[field] = salary

        elif field == 5:
            self.element_is_visible(self.locators.DEPARTMENT_FIELD).clear()
            self.element_is_visible(self.locators.DEPARTMENT_FIELD).send_keys(department)
            self.elements_is_clickable(self.locators.SUBMIT_BUTTON).click()
            row_person[field] = department

        return [before_row_person, row_person]

    def delete_person(self):
        delete_buttons = self.elements_are_present(self.locators.DELETE_BUTTON)
        delete_button = delete_buttons[random.randint(0, len(delete_buttons) - 1)]
        self.go_to_element(delete_button)
        row_person_info = delete_button.find_element(*self.locators.ROW_PARENT).text.splitlines()
        delete_button.click()
        return row_person_info

    def change_count_rows(self):
        list_options_value = ("5", "10", "20", "25", "50", "100")
        # random_count = str(list_options_value[random.randint(0, len(list_options_value)-1)])
        list_option = self.elements_are_present(self.locators.COUNT_ROWS_VALUE)

        for index, option in enumerate(list_option):
            self.go_to_element(self.elements_is_clickable(self.locators.SELECT_BUTTON_ROWS))
            self.elements_is_clickable(self.locators.SELECT_BUTTON_ROWS).click()
            option.click()
            assert int(list_options_value[index]) == len(self.elements_are_present(self.locators.FULL_PEOPLE_LIST)), f"Choised rows is not {list_options_value[index]}"


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_double_click_button(self):
        double_click_button = self.elements_is_clickable(self.locators.DOUBLE_CLICK_BUTTON)
        self.go_to_element(double_click_button)

        (self.action
         .double_click(double_click_button)
         .perform())

        assert self.element_is_visible(self.locators.INFO_DCBTN).text == "You have done a double click", "No double click button"

    def click_on_right_click_button(self):
        right_click_button = self.elements_is_clickable(self.locators.RIGHT_CLICK_BUTTON)
        self.go_to_element(right_click_button)

        (self.action
         .context_click(right_click_button)
         .perform())
        assert self.element_is_visible(
            self.locators.INFO_RCB).text == "You have done a right click", "No right click button"

    def click_on_dynamic_click_button(self):
        click_button = self.elements_is_clickable(self.locators.CLICK_BUTTON)
        click_button.click()
        assert self.element_is_visible(self.locators.INFO_CLICKBTN).text == "You have done a dynamic click", "No dynamic click button"
        id_button = click_button.get_attribute("id")
        self.refresh_page()
        assert id_button != self.elements_is_clickable(self.locators.CLICK_BUTTON).get_attribute("id"), "No refresh id click button"