"""PYTEST TEST CASES"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from homework_24.pages.login_page import LoginPage
from homework_24.pages.contact_list_page import ContactListPage
from homework_24.pages.contact_details_page import ContactDetailsPage
from homework_24.pages.edit_contact_page import EditContactPage
from homework_24.pages.add_contact_page import AddContactPage
from homework_24.test_data.constants import *
from log_dir.log_setup import logger

@pytest.fixture
def browser():
    """
    Fixture to set up and tear down the browser instance for each test.
    """
    logger.info("Setting up browser ...")
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(5)
    chrome_browser.get(URL)
    yield chrome_browser
    chrome_browser.quit()


@pytest.mark.create_new_contact
def test_create_new_contact(browser):
    """
    Test the creation of a new contact.
    """
    logger.info("TEST 1: CREATE NEW CONTACT. Executing...")
    page_object = LoginPage(browser)
    page_object.complete_login(EMAIL, PASSWORD)
    time.sleep(1)
    page_object = ContactListPage(browser)
    page_object.click_add_contact()
    time.sleep(1)
    page_object = AddContactPage(browser)

    page_object.complete_add_new_contact(FIRST_NAME, LAST_NAME, BIRTHDATE,
                                         EMAIL_ADDRESS, PHONE, STREET1, STREET2,
                                         CITY, STATE_PROVINCE, POSTAL_CODE, COUNTRY)
    page_object = ContactListPage(browser)
    assert page_object.locate_contact_row() is not None
    logger.info("TEST 1: Executed")


@pytest.mark.edit_contact
def test_edit_contact(browser):
    """
    Test the editing of an existing contact.
    """
    logger.info("TEST 2: EDIT CONTACT. Executing...")
    page_object = LoginPage(browser)
    page_object.complete_login(EMAIL, PASSWORD)
    time.sleep(1)
    page_object = ContactListPage(browser)
    page_object.open_contact()
    time.sleep(1)
    page_object = ContactDetailsPage(browser)
    page_object.click_edit_contact()
    time.sleep(1)
    page_object = EditContactPage(browser)
    page_object.complete_edit_contact(EDIT_FIRST_NAME, EDIT_LAST_NAME,
                                      EDIT_BIRTHDATE, EDIT_EMAIL_ADDRESS,
                                      EDIT_PHONE, EDIT_STREET1, EDIT_STREET2,
                                      EDIT_CITY, EDIT_STATE_PROVINCE,
                                      EDIT_POSTAL_CODE, EDIT_COUNTRY)
    page_object = ContactDetailsPage(browser)
    time.sleep(1)  # This one is really needed!
    assert page_object.locate_first_name().text == "RICARDO"
    assert page_object.locate_last_name().text == "DIAZ"
    assert page_object.locate_birthdate().text == "1999-12-12"
    assert page_object.locate_email_address().text == "hello@world.com"
    assert page_object.locate_phone().text == "0987654321"
    assert page_object.locate_street1().text == "BOULEVARD OF BROKEN DREAMS"
    assert page_object.locate_street2().text == "80-180"
    assert page_object.locate_city().text == "KYOTO"
    assert page_object.locate_state_province().text == "HAMPSHIRE"
    assert page_object.locate_postal_code().text == "200205"
    assert page_object.locate_country().text == "FRANCE"
    time.sleep(5)
    logger.info("TEST 2: Executed")


@pytest.mark.delete_contact
def test_delete_contact(browser):
    """
    Test the deletion of an existing contact.
    """
    logger.info("TEST 3: DELETE CONTACT. Executing...")
    page_object = LoginPage(browser)
    page_object.complete_login(EMAIL, PASSWORD)
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
    page_object = ContactListPage(browser)
    # assert page_object.locate_contact_row() is None
    logger.info("TEST 3: Executed")
