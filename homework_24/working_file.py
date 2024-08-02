import time
from log_dir.log_setup import logger
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from homework_24.pages.login_page import LoginPage

user_name_field = (By.ID, "email")
password_field = (By.ID, "password")
submit_button = (By.ID, "submit")

@pytest.fixture
def enter_username(self, name):
    username_textbox = self.find_element(user_name_field)
    username_textbox.send_keys(By.ID, "email")

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
def test_login_valid_credentials(browser):
    logger.info("PERFORMING FIRST TEST")
    page = LoginPage(browser)
    time.sleep(1)
    username_textbox = browser.find_element(By.ID, "email")

    username_textbox.send_keys("Hello@world.ru")
    time.sleep(10)