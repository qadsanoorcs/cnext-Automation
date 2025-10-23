# tests/test_login.py
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils import config


@pytest.fixture(scope="function")
def driver():
    # Chrome + Selenium Manager will auto-handle driver in recent selenium versions
    options = Options()
    # options.add_argument("--headless=new")  # uncomment if you prefer headless runs
    options.add_argument("--start-maximized")
    # optionally disable infobars
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    yield driver
    # On teardown, quit
    try:
        driver.quit()
    except Exception:
        pass


def _take_screenshot(driver, name="screenshot"):
    reports_dir = os.path.join(os.getcwd(), "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    filename = os.path.join(reports_dir, f"{name}_{int(time.time())}.png")
    try:
        driver.save_screenshot(filename)
    except Exception:
        pass
    return filename


def test_super_admin_login(driver):
    driver.get(config.BASE_URL)

    login_page = LoginPage(driver)
    creds = config.CREDENTIALS.get("super_admin")

    # Attempt login and click checkboxes mentioned (best-effort)
    login_page.login(
        email=creds["email"],
        password=creds["password"],
        checkbox_labels=config.CHECKBOX_LABELS
    )

    # Wait briefly; then verify
    assert login_page.is_logged_in(timeout_seconds=10), f"Login check failed — see report. Screenshot: {_take_screenshot(driver)}"
