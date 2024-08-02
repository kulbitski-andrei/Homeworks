import time
# from log_dir.log_setup import logger
import pytest
from homework_24.pages.login_page import LoginPage
from homework_24.pages.contact_list_page import ContactListPage
from homework_24.pages.contact_details_page import ContactDetailsPage
from homework_24.pages.edit_contact_page import EditContactPage
from homework_24.pages.add_contact_page import AddContactPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

email = "hello.world@gmail.com"
password = "password_password"
first_name = "John"
last_name = "Doe"
birthdate = "2000-01-01"
email_address = "john@doe.com"
phone = "1234567890"
street1 = "123 Main St"
street2 = "Apt 4B"
city = "Springfield"
state_province = "IL"
postal_code = "62704"
country = "USA"

edit_first_name = "RICARDO"
edit_last_name = "DIAZ"
edit_birthdate = "1999-12-12"
edit_email_address = "hello@world.com"
edit_phone = "0987654321"
edit_street1 = "BOOLEVARD OF BROKEN DREAMS"
edit_street2 = "80-180"
edit_city = "Kyoto"
edit_state_province = "AR"
edit_postal_code = "200205"
edit_country = "FRANCE"


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(5)
    chrome_browser.get("""https://thinking-tester-contact-list.herokuapp.com/""")
    yield chrome_browser
    chrome_browser.quit()


@pytest.mark.login
def test_login(browser):
    page_object = LoginPage(browser)
    time.sleep(1)
    page_object.complete_login(email, password)
    time.sleep(5)


@pytest.mark.create_new_contact
def test_create_new_contact(browser):
    page_object = LoginPage(browser)
    page_object.complete_login(email, password)
    time.sleep(1)
    page_object = ContactListPage(browser)
    page_object.click_add_contact()
    time.sleep(1)
    page_object = AddContactPage(browser)
    page_object.complete_add_new_contact(edit_first_name, edit_last_name,
                                         edit_birthdate, edit_email_address,
                                         edit_phone, edit_street1, edit_street2,
                                         edit_city, edit_state_province,
                                         edit_postal_code, edit_country)
    time.sleep(5)

@pytest.mark.edit_contact
def test_edit_contact(browser):
    page_object = LoginPage(browser)
    page_object.complete_login(email, password)
    time.sleep(1)
    page_object = ContactListPage(browser)
    page_object.open_contact()
    time.sleep(1)
    page_object = ContactDetailsPage(browser)
    page_object.click_edit_contact()
    time.sleep(1)
    page_object = EditContactPage(browser)
    page_object.complete_edit_contact(first_name, last_name, birthdate,
                                      email_address, phone, street1, street2,
                                      city, state_province, postal_code, country)
    time.sleep(5)

@pytest.mark.delete_contact
def test_delete_contact(browser):
    page_object = LoginPage(browser)
    page_object.complete_login(email, password)
    time.sleep(1)
    page_object = ContactListPage(browser)
    page_object.open_contact()
    time.sleep(1)
    page_object = ContactDetailsPage(browser)
    time.sleep(1)
    page_object.click_delete_contact()
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(5)
