"""PYTEST TEST CASES"""

import time
import pytest
from homework_24.pages.login_page import LoginPage
from homework_24.pages.contact_list_page import ContactListPage
from homework_24.pages.contact_details_page import ContactDetailsPage
from homework_24.pages.edit_contact_page import EditContactPage
from homework_24.pages.add_contact_page import AddContactPage
import homework_24.test_data.constants as const
from log_dir.log_setup import logger


@pytest.mark.create_new_contact
def test_create_new_contact(browser):
    """
    Test the creation of a new contact.
    """
    logger.info("TEST 1: CREATE NEW CONTACT. Executing...")
    current_page = LoginPage(browser)
    current_page.complete_login(const.EMAIL, const.PASSWORD)
    current_page = ContactListPage(browser)
    current_page.click_add_contact()
    current_page = AddContactPage(browser)
    current_page.complete_add_new_contact(const.FIRST_NAME, const.LAST_NAME,
                                         const.BIRTHDATE, const.EMAIL_ADDRESS,
                                         const.PHONE, const.STREET1,
                                         const.STREET2, const.CITY,
                                         const.STATE_PROVINCE,
                                         const.POSTAL_CODE, const.COUNTRY)
    current_page = ContactListPage(browser)
    assert current_page.locate_contact_row() is not None
    logger.info("TEST 1: Executed")


@pytest.mark.edit_contact
def test_edit_contact(browser):
    """
    Test the editing of an existing contact.
    """
    logger.info("TEST 2: EDIT CONTACT. Executing...")
    current_page = LoginPage(browser)
    current_page.complete_login(const.EMAIL, const.PASSWORD)
    current_page = ContactListPage(browser)
    current_page.open_contact()
    current_page = ContactDetailsPage(browser)
    current_page.click_edit_contact()
    current_page = EditContactPage(browser)
    time.sleep(1)  # This one is really needed!
    current_page.complete_edit_contact(const.EDIT_FIRST_NAME,
                                      const.EDIT_LAST_NAME,
                                      const.EDIT_BIRTHDATE,
                                      const.EDIT_EMAIL_ADDRESS,
                                      const.EDIT_PHONE,
                                      const.EDIT_STREET1,
                                      const.EDIT_STREET2,
                                      const.EDIT_CITY,
                                      const.EDIT_STATE_PROVINCE,
                                      const.EDIT_POSTAL_CODE,
                                      const.EDIT_COUNTRY)
    current_page = ContactDetailsPage(browser)
    time.sleep(1)  # This one is really needed!
    assert current_page.locate_first_name().text == "RICARDO"
    assert current_page.locate_last_name().text == "DIAZ"
    assert current_page.locate_birthdate().text == "1999-12-12"
    assert current_page.locate_email_address().text == "hello@world.com"
    assert current_page.locate_phone().text == "0987654321"
    assert current_page.locate_street1().text == "BOULEVARD OF BROKEN DREAMS"
    assert current_page.locate_street2().text == "80-180"
    assert current_page.locate_city().text == "KYOTO"
    assert current_page.locate_state_province().text == "HAMPSHIRE"
    assert current_page.locate_postal_code().text == "200205"
    assert current_page.locate_country().text == "FRANCE"
    logger.info("TEST 2: Executed")


@pytest.mark.delete_contact
def test_delete_contact(browser):
    """
    Test the deletion of an existing contact.
    """
    logger.info("TEST 3: DELETE CONTACT. Executing...")
    current_page = LoginPage(browser)
    current_page.complete_login(const.EMAIL, const.PASSWORD)
    current_page = ContactListPage(browser)
    contact_count_before_delete = len(current_page.locate_contact_rows())
    logger.info("Contact count: %s", contact_count_before_delete)
    current_page.open_contact()
    current_page = ContactDetailsPage(browser)
    current_page.click_delete_contact()
    alert = browser.switch_to.alert
    alert.accept()
    current_page = ContactListPage(browser)
    contact_count_after_delete = len(current_page.locate_contact_rows())
    logger.info("Contact count: %s", contact_count_after_delete)
    assert contact_count_before_delete - contact_count_after_delete == 1
    logger.info("TEST 3: Executed")
