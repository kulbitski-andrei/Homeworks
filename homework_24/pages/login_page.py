"""LOGIN PAGE"""

from selenium.webdriver.common.by import By
from homework_24.pages.base_page import BasePage

email_field = (By.ID, "email")
password_field = (By.ID, "password")
submit_button = (By.ID, "submit")


class LoginPage(BasePage):
    """Login Page class"""
    def __init__(self, driver):
        """
        Initialize the LoginPage with a web driver.
        """
        super().__init__(driver)

    def enter_text(self, text, field):
        """
        Enter the text into the field.
        """
        input_var = self.find_element(field)
        input_var.send_keys(text)

    def click_submit(self):
        """
        Click the submit button to log in.
        """
        submit_element = self.find_element(submit_button)
        submit_element.click()

    def complete_login(self, email, password):
        """
        Complete the login process by entering the email
        and password and submitting the form.
        """
        self.enter_text(email, email_field)
        self.enter_text(password, password_field)
        self.click_submit()
