from homework_24.pages.base_page import BasePage
from selenium.webdriver.common.by import By

delete_button = (By.ID, "delete")

class ContactDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)