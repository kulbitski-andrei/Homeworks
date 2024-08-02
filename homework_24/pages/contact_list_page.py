from homework_24.pages.base_page import BasePage
from selenium.webdriver.common.by import By

add_contact_button = (By.ID, "add-contact")

class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_add_contact(self):
        add_contact_element = self.find_element(add_contact_button)
        add_contact_element.click()