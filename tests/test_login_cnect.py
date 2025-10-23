import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_cnext_login(driver):
    driver.get("https://alpha.cnext.revdev.it/")

    login = LoginPage(driver)
    login.enter_email("admin@cnext.com")
    login.enter_password("Secure@CNext88$")
    login.accept_terms()
    login.remember_me()
    login.click_login()

    time.sleep(5)  # wait to observe the login
    assert "profile" in driver.current_url.lower()
