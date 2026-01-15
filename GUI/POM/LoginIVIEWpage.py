"""
LoginIVIEWpage.py - Page Object Model (POM) for iView Meeting/Login page
Contains all element locators and page interaction methods
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from robot.api import logger

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LoginIVIEWpage:
    """Page Object for iView Login and Logout flows"""
    
    # Element locators (By.ID)
    USERNAME_INPUT = (By.ID, "loginForm:username")
    PASSWORD_INPUT = (By.ID, "loginForm:password")
    LOGIN_BUTTON = (By.ID, "loginForm:submitText")
    LOGOUT_BUTTON = (By.ID, "logoutForm:log_out")
    
    def __init__(self, driver):
        """
        Initialize page object with driver instance
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def sign_in(self, username, password):
        """
        Sign in to the application
        """
        try:
            logging.info("Attempting to sign in")
            # Wait for username field and fill it
            username_el = self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
            username_el.click()
            username_el.clear()
            username_el.send_keys(username)
            logging.debug(f"Entered username: {username}")
            password_el = self.driver.find_element(*self.PASSWORD_INPUT)
            password_el.send_keys(password)
            logging.debug("Entered password")
            login_btn = self.driver.find_element(*self.LOGIN_BUTTON)
            login_btn.click()
            logging.debug("Clicked login button")
            
            # Wait for logout button to confirm successful login
            self.wait.until(EC.presence_of_element_located(self.LOGOUT_BUTTON))
            logging.info("Successfully signed in - logout button detected")
            
        except Exception as e:
            logging.error(f"Error during sign in: {e}")
            raise
    
    def sign_out(self):
        """
        Sign out from the application
        """
        try:
            logging.info("Attempting to sign out")
            # Wait for logout button to be clickable and click it
            logout_btn = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
            logout_btn.click()
            logging.info("Successfully signed out")
            
        except Exception as e:
            logging.error(f"Error during sign out: {e}")
            raise