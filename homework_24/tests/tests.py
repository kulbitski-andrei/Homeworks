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
    page_object = LoginPage(browser)
    page_object.complete_login(const.EMAIL, const.PASSWORD)
    page_object = ContactListPage(browser)
    page_object.click_add_contact()
    page_object = AddContactPage(browser)

    page_object.complete_add_new_contact(const.FIRST_NAME, const.LAST_NAME,
                                         const.BIRTHDATE, const.EMAIL_ADDRESS,
                                         const.PHONE, const.STREET1,
                                         const.STREET2, const.CITY,
                                         const.STATE_PROVINCE,
                                         const.POSTAL_CODE, const.COUNTRY)
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
    page_object.complete_login(const.EMAIL, const.PASSWORD)
    page_object = ContactListPage(browser)
    page_object.open_contact()
    page_object = ContactDetailsPage(browser)
    page_object.click_edit_contact()
    page_object = EditContactPage(browser)
    time.sleep(1)  # This one is really needed!
    page_object.complete_edit_contact(const.EDIT_FIRST_NAME,
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
    logger.info("TEST 2: Executed")


@pytest.mark.delete_contact
def test_delete_contact(browser):
    """
    Test the deletion of an existing contact.
    """
    logger.info("TEST 3: DELETE CONTACT. Executing...")
    page_object = LoginPage(browser)
    page_object.complete_login(const.EMAIL, const.PASSWORD)
    page_object = ContactListPage(browser)
    contact_count_before_delete = len(page_object.locate_contact_rows())
    logger.info("Contact count: %s", contact_count_before_delete)
    page_object.open_contact()
    page_object = ContactDetailsPage(browser)
    page_object.click_delete_contact()
    alert = browser.switch_to.alert
    alert.accept()
    page_object = ContactListPage(browser)
    contact_count_after_delete = len(page_object.locate_contact_rows())
    logger.info("Contact count: %s", contact_count_after_delete)
    assert contact_count_before_delete - contact_count_after_delete == 1
    logger.info("TEST 3: Executed")
