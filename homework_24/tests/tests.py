import time
from homework_24.log_setup import logger
import pytest
from homework_24.pages.login_page import LoginPage
from homework_24.pages.contact_list_page import ContactListPage
from homework_24.pages.contact_details_page import ContactDetailsPage
from homework_24.pages.edit_contact_page import EditContactPage
from homework_24.pages.add_contact_page import AddContactPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from homework_24.test_data.constants import *


@pytest.fixture
def browser():
    logger.info("Setting up browser ...")
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(5)
    chrome_browser.get(url)
    yield chrome_browser
    chrome_browser.quit()


@pytest.mark.create_new_contact
def test_create_new_contact(browser):
    logger.info("TEST 1: CREATE NEW CONTACT. Executing...")
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
    logger.info("TEST 1: Executed")


@pytest.mark.edit_contact
def test_edit_contact(browser):
    logger.info("TEST 2: EDIT CONTACT. Executing...")
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
    logger.info("TEST 2: Executed")


@pytest.mark.delete_contact
def test_delete_contact(browser):
    logger.info("TEST 3: DELETE CONTACT. Executing...")
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
    time.sleep(1)
    alert.accept()
    time.sleep(1)
    logger.info("TEST 3: Executed")
