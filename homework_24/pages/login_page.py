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

    def enter_password(self, password):
        password_input = self.find_element(password_field)
        password_input.send_keys(password)

    def click_submit(self):
        submit_element = self.find_element(submit_button)
        submit_element.click()

    def complete_login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit()
        return
