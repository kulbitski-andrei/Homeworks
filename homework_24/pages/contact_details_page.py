from homework_24.pages.base_page import BasePage
from selenium.webdriver.common.by import By

delete_button = (By.ID, "delete")


class ContactDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_delete_contact(self):
        delete_contact_element = self.find_element(delete_button)
        delete_contact_element.click()

