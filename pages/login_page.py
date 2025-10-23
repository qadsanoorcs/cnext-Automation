from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    TERMS_CHECKBOX = (By.XPATH, "//label[contains(., 'Accetto')]")
    REMEMBER_CHECKBOX = (By.XPATH, "//label[contains(., 'Ricordami')]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, email, password, checkbox_labels=None):
        try:
            # Fill email
            email_input = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
            email_input.clear()
            email_input.send_keys(email)
            print("✅ Email entered")
            
            # Fill password
            password_input = self.driver.find_element(*self.PASSWORD_INPUT)
            password_input.clear()
            password_input.send_keys(password)
            print("✅ Password entered")
    
            # SIMPLIFIED CHECKBOX HANDLING
            try:
                # Try the specific checkbox locators from your class
                self.driver.find_element(*self.TERMS_CHECKBOX).click()
                print("✅ Clicked terms checkbox")
            except Exception as e:
                print(f"⚠️ Could not click terms checkbox: {e}")
        
            try:
                self.driver.find_element(*self.REMEMBER_CHECKBOX).click()
                print("✅ Clicked remember me checkbox")
            except Exception as e:
                print(f"⚠️ Could not click remember me checkbox: {e}")
        
            # Click login
            self.driver.find_element(*self.LOGIN_BUTTON).click()
            print("✅ Login button clicked")
            
        except Exception as e:
            print(f"❌ Login process failed: {e}")
            raise

    def is_logged_in(self, timeout_seconds=15):
        try:
            WebDriverWait(self.driver, timeout_seconds).until(
                lambda d: "profile" in d.current_url.lower()
            )
            return True
        except Exception:
            return False

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def accept_terms(self):
        self.driver.find_element(*self.TERMS_CHECKBOX).click()

    def remember_me(self):
        self.driver.find_element(*self.REMEMBER_CHECKBOX).click()

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()