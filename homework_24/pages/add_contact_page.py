from homework_24.pages.base_page import BasePage
from selenium.webdriver.common.by import By

first_name_field = (By.ID, "firstName")
last_name_field = (By.ID, "lastName")
birthdate_field = (By.ID, "birthdate")
phone_field = (By.ID, "phone")
street1_field = (By.ID, "street1")
street2_field = (By.ID, "street2")
city_field = (By.ID, "city")
state_province_field = (By.ID, "stateProvince")
postal_code_field = (By.ID, "postalCode")
country_field = (By.ID, "country")
submit_button = (By.ID, "submit")


class AddContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        first_name_input = self.find_element(first_name_field)
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_input = self.find_element(last_name_field)
        last_name_input.send_keys(last_name)

    def enter_birthdate(self, birthdate):
        birthdate_input = self.find_element(birthdate_field)
        birthdate_input.send_keys(birthdate)

    def enter_phone(self, phone):
        phone_input = self.find_element(phone_field)
        phone_input.send_keys(phone)

    def enter_street1(self, street1):
        street1_input = self.find_element(street1_field)
        street1_input.send_keys(street1)

    def enter_street2(self, street2):
        street2_input = self.find_element(street2_field)
        street2_input.send_keys(street2)

    def enter_city(self, city):
        city_input = self.find_element(city_field)
        city_input.send_keys(city)

    def enter_state_province(self, state_province):
        state_province_input = self.find_element(state_province_field)
        state_province_input.send_keys(state_province)

    def enter_postal_code(self, postal_code):
        postal_code_input = self.find_element(postal_code_field)
        postal_code_input.send_keys(postal_code)

    def enter_country(self, country):
        country_input = self.find_element(country_field)
        country_input.send_keys(country)

    def click_submit(self):
        submit_form_button = self.find_element(submit_button)
        submit_form_button.click()

    def complete_add_new_contact(self, first_name, last_name, birthdate,
                                 phone, street1, street2, city,
                                 state_province, postal_code, country):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_birthdate(birthdate)
        self.enter_phone(phone)
        self.enter_street1(street1)
        self.enter_street2(street2)
        self.enter_city(city)
        self.enter_state_province(state_province)
        self.enter_postal_code(postal_code)
        self.enter_country(country)
        self.click_submit()
