import time

from pages.elements_page import TextBoxPage


class TestTextBox:
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
        text_box_page.open()  # driver.get(URL)
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields() # Filling all fields data
        output_full_name, output_email, output_curr_addr, output_perm_addr = text_box_page.get_text_from_fields()

        assert full_name == output_full_name, "Full name does not match"
        assert email == output_email, "Email does not match"
        assert current_address == output_curr_addr, "Current address does not match"
        assert permanent_address == output_perm_addr, "Permanent address does not match"
        # Ещё вариант input_data == output_data, но это не слишком читабельно, если будет ошибка.
