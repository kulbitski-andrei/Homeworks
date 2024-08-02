import time
from log_dir.log_setup import logger
import pytest
from homework_24.pages.login_page import LoginPage
from homework_24.pages.contact_list_page import ContactPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

email = "hello.world@gmail.com"
password = "password_password"

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
    time.sleep(10)


def test_create_new_contact(browser):
    page_object = LoginPage(browser)
    time.sleep(1)
    page_object.complete_login(email, password)
    time.sleep(1)
    page_object = ContactPage(browser)
    time.sleep(1)
    page_object.click_add_contact()
    time.sleep(10)




