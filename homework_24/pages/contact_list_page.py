from homework_24.pages.base_page import BasePage
from selenium.webdriver.common.by import By

add_contact_button = (By.ID, "add-contact")
contact_row = (By.XPATH, "//tr[@class=\"contactTableBodyRow\"][1]")

class ContactListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_add_contact(self):
        add_contact_element = self.find_element(add_contact_button)
        add_contact_element.click()

    def open_contact(self):
        open_contact = self.find_element(contact_row)
        open_contact.click()
