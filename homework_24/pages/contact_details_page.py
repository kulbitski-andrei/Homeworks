from homework_24.pages.base_page import BasePage
from selenium.webdriver.common.by import By

edit_button = (By.ID, "edit-contact")
delete_button = (By.ID, "delete")


class ContactDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_contact(self):
        edit_contact_element = self.find_element(edit_button)
        edit_contact_element.click()

    def click_delete_contact(self):
        delete_contact_element = self.find_element(delete_button)
        delete_contact_element.click()
