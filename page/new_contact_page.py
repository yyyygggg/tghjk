from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewContactPage(BaseAction):
    local_save_button = By.XPATH, "//*[@text='本地保存']"
    back_button = By.XPATH, "//*[@content-desc='向上导航']"
    name = By.XPATH, "//*[@text='姓名']"
    phone = By.XPATH, "//*[@text='电话']"

    def click_local_save(self):
        self.click(self.local_save_button)

    def input_name(self, text):
        self.input(self.name, text)

    def input_phone(self, text):
        self.input(self.phone, text)

    def click_back(self):
        self.click(self.back_button)
