import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, \
    UploadDownloadPage


class TestTextBoxPage:
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()  # driver.get(URL)
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()  # Filling all fields data
        output_full_name, output_email, output_curr_addr, output_perm_addr = text_box_page.get_text_from_fields()
        time.sleep(2)
        assert full_name == output_full_name, "Full name does not match"
        assert email == output_email, "Email does not match"
        assert current_address == output_curr_addr, "Current address does not match"
        assert permanent_address == output_perm_addr, "Permanent address does not match"
        # Ещё вариант input_data == output_data, но это не слишком читабельно, если будет ошибка.


class TestCheckBoxPage:
    def test_checked_all_checkboxes(self, driver):
        checkbox_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        checkbox_page.open()
        checkbox_page.open_full_list()
        checkbox_page.choice_random_checkbox()


class TestRadioButtonPage:

    def test_radio_button(self, driver):
        radiobutton_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
        radiobutton_page.open()
        radiobutton_page.choice_yes_radio_buttons()
        radiobutton_page.choice_no_radio_buttons()
        radiobutton_page.choice_impressive_radio_buttons()


class TestWebTables:

    def test_add_new_person_in_table(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()
        list_added_person = web_tables_page.add_new_persons(count=2)
        table_persons = web_tables_page.get_all_people()
        for new_person in list_added_person:
            assert new_person in table_persons, f"{new_person[0]}-{new_person[1]} was not added to table"

    def test_search_people_in_table(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()
        key_word = web_tables_page.add_new_persons()[0][random.randint(0, 5)]
        web_tables_page.search_people_in_table(key_word)
        list_people_search = web_tables_page.checked_search_people_in_table()
        for people_search in list_people_search:
            if key_word in people_search:
                assert key_word in people_search, f"Search person by {key_word} is not added to table"

    def test_update_person_info_in_table(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()
        before_info_person, update_info_person = web_tables_page.update_info_person()
        table_persons = web_tables_page.get_all_people()
        print(before_info_person)
        print(update_info_person)
        assert update_info_person in table_persons, f"Person is not update was not added to table"

    def test_delete_person_from_table(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()
        deleted_person = web_tables_page.delete_person()
        table_persons = web_tables_page.get_all_people()
        assert deleted_person not in table_persons, f"Person is not deleted was not added to table"

    def test_change_rows_count(self, driver):
        web_tables_page = WebTablesPage(driver, "https://demoqa.com/webtables")
        web_tables_page.open()
        web_tables_page.change_count_rows()


class TestButtonsPage:

    def test_click_double_click_button(self, driver):
        button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
        button_page.open()
        button_page.click_on_double_click_button()

    def test_click_right_click_button(self, driver):
        button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
        button_page.open()
        button_page.click_on_right_click_button()

    def test_click_dynamic_button(self, driver):
        button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
        button_page.open()
        button_page.click_on_dynamic_click_button()


class TestLinksPage:

    def test_link_open_new_window(self, driver):
        links_page = LinksPage(driver, "https://demoqa.com/links")
        links_page.open()
        assert links_page.click_on_link_open_new_tab_button() == "https://demoqa.com/", "No link open new tab"

    def test_link_no_content(self, driver):
        links_page = LinksPage(driver, "https://demoqa.com/links")
        links_page.open()
        info_response = links_page.click_on_link_no_content()
        assert info_response[0] == str(204), "Status code is not 204 in link info"
        assert info_response[1] == "No Content", "Info is not NoContent"


class TestUploadDownloadPage:

    def test_download(self, driver_no_incognito):
        up_down_load_page = UploadDownloadPage(driver_no_incognito, "https://demoqa.com/upload-download")
        up_down_load_page.open()
        up_down_load_page.download_file()

    def test_upload(self, driver_no_incognito):
        up_down_load_page = UploadDownloadPage(driver_no_incognito, "https://demoqa.com/upload-download")
        up_down_load_page.open()
        up_down_load_page.upload_file()
