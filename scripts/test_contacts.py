from time import sleep

import pytest

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file


class TestContacts:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("name,phone", analyze_with_file("contacts_data", "test_new_contacts", "name", "phone"))
    def test_new_contacts(self, name, phone):
        self.page.contact_list.click_new_contact()
        self.page.new_contact.click_local_save()
        self.page.new_contact.input_name(name)
        self.page.new_contact.input_phone(phone)
        self.page.new_contact.click_back()
        sleep(10)
        self.page.new_contact.press_back()
        sleep(2)
        assert self.page.contact_list.is_name_in_contacts_name_feature(name)

