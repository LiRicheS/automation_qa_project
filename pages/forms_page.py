import random
import time
from datetime import datetime

import requests
import os
from selenium.webdriver import Keys

from locators.forms_page_locators import FormsPageLocators
from generator.generator import generate_data_person
from pages.base_page import BasePage


class FormsPage(BasePage):
    locators = FormsPageLocators()

    def filling_all_fields_form(self):
        person = next(generate_data_person())
        first_name = person.first_name
        last_name = person.last_name
        email = person.email
        phone = person.phone
        # date_of_birth = str(person.date_of_birth)
        current_address = person.current_address

        self.go_to_element(self.element_is_visible(self.locators.FIRST_NAME))
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)

        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)

        self.go_to_element(self.element_is_visible(self.locators.GENDER))
        self.element_is_visible(self.locators.GENDER).click()
        gender = self.element_is_visible(self.locators.GENDER).text
        assert self.element_is_present(self.locators.GENDER_STATUS).is_selected() is True, "GENDER STATUS NOT FOUND"

        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(phone)
        date_of_birthday = datetime.strptime(self.element_is_visible(self.locators.DATE_OF_BIRTH).get_attribute('value'), '%d %b %Y')
        date_of_birthday = date_of_birthday.strftime('%d %B,%Y')
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(date_of_birth)
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.ENTER)

        self.go_to_element(self.element_is_visible(self.locators.SUBJECT))
        self.element_is_visible(self.locators.SUBJECT).send_keys("M")
        self.element_is_visible(self.locators.SUBJECT_SELECT).click()
        subject = self.element_is_visible(self.locators.SUBJECT_STATUS).text

        self.go_to_element(self.element_is_visible(self.locators.HOBBIES_CHECKBOX))
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX).click()
        hobbies = self.element_is_visible(self.locators.HOBBIES_CHECKBOX).text
        assert self.element_is_present(self.locators.HOBBIES_STATUS).is_selected() is True, f"HOBBIES STATUS NOT FOUND"

        self.upload_file()
        picture = "example.json"

        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)

        self.go_to_element(self.element_is_visible(self.locators.SELECT_STATES))
        self.element_is_visible(self.locators.SELECT_STATES).click()
        state = self.element_is_visible(self.locators.RANDOM_SELECT_STATE).text
        self.element_is_present(self.locators.RANDOM_SELECT_STATE).click()

        self.element_is_visible(self.locators.SELECT_CITY).click()
        city = self.element_is_visible(self.locators.RANDOM_SELECT_CITY).text
        self.element_is_visible(self.locators.RANDOM_SELECT_CITY).click()

        self.go_to_element(self.element_is_visible(self.locators.SUBMIT_BUTTON))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        return first_name + " " + last_name, email, gender, phone, date_of_birthday, subject, hobbies, picture, current_address, state + " " + city

    def get_info_table_result_fill(self):
        result_list = self.elements_are_visible(self.locators.TABLE_RESULT)
        data = []
        for result in result_list:
            data.append(result.text)
        return tuple(data)

    def upload_file(self):
        file_path = str(os.path.join(os.getcwd(), "uploads", "example.json"))
        upload_button = self.element_is_present(self.locators.PICTURE_FILE_BUTTON)
        upload_button.send_keys(file_path)

        # assert self.element_is_visible(self.locators.UPLOAD_PATH_INFO).text == "C:\\fakepath\\example.json", "No upload path info"
