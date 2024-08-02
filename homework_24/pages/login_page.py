from homework_24.pages.base_page import BasePage
from selenium.webdriver.common.by import By

email_field = (By.ID, "email")
password_field = (By.ID, "password")
submit_button = (By.ID, "submit")

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        email_input = self.find_element(email_field)
        email_input.send_keys(email)
