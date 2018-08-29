from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactListPage(BaseAction):
    new_contact_button = By.XPATH, "//*[@content-desc='添加新联系人']"
    contacts_name_feature = By.ID, "com.android.contacts:id/cliv_name_textview"

    def click_new_contact(self):
        self.click(self.new_contact_button)

    def is_name_in_contacts_name_feature(self, name):

        for element in self.find_elements(self.contacts_name_feature):
            if name in element.text:
                return True
        return False
