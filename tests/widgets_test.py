import random
import time

from pages.widgets_page import AccordianPage


class TestAccordianPage:

    def test_click_accordian_section_present(self, driver):
        accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
        accordian_page.open()

        result = accordian_page.click_accordian()
        assert result['is_section_visible'] is True, "Accordian section should be visible"
        assert result['is_section_invisible'] is True, "Accordian section should be invisible"
