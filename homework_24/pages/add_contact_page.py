from homework_24.pages.base_page import BasePage
from selenium.webdriver.common.by import By

first_name_field = (By.ID, "firstName")

class AddContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        first_name_input = self.find_element(first_name_field)
        first_name_input.send_keys(first_name)