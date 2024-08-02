from homework_24.pages.base_page import BasePage
from selenium.webdriver.common.by import By

edit_button = (By.ID, "edit-contact")
delete_button = (By.ID, "delete")

first_name_field = (By.ID, "firstName")
last_name_field = (By.ID, "lastName")
birthdate_field = (By.ID, "birthdate")
email_address_field = (By.ID, "email")
phone_field = (By.ID, "phone")
street1_field = (By.ID, "street1")
street2_field = (By.ID, "street2")
city_field = (By.ID, "city")
state_province_field = (By.ID, "stateProvince")
postal_code_field = (By.ID, "postalCode")
country_field = (By.ID, "country")


class ContactDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_contact(self):
        edit_contact_element = self.find_element(edit_button)
        edit_contact_element.click()

    def click_delete_contact(self):
        delete_contact_element = self.find_element(delete_button)
        delete_contact_element.click()

    def locate_first_name(self):
        return self.find_element(first_name_field)

    def locate_last_name(self):
        return self.find_element(last_name_field)

    def locate_birthdate(self):
        return self.find_element(birthdate_field)

    def locate_email_address(self):
        return self.find_element(email_address_field)

    def locate_phone(self):
        return self.find_element(phone_field)

    def locate_street1(self):
        return self.find_element(street1_field)

    def locate_street2(self):
        return self.find_element(street2_field)

    def locate_city(self):
        return self.find_element(city_field)

    def locate_state_province(self):
        return self.find_element(state_province_field)

    def locate_postal_code(self):
        return self.find_element(postal_code_field)

    def locate_country(self):
        return self.find_element(country_field)
