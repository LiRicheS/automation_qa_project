import random
import time

from pages.forms_page import FormsPage


class TestPracticeForm:

    def test_fill_fields(self, driver):
        form_page = FormsPage(driver, "https://demoqa.com/automation-practice-form")
        form_page.open()
        fields_data = form_page.filling_all_fields_form()
        result_table = form_page.get_info_table_result_fill()
        print(" ")
        print(fields_data)
        print(result_table)

        assert fields_data == result_table, "Filling all fields failed"
        time.sleep(2)
