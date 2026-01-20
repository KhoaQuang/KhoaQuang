from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from Utility.Utility import Utility

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MeetNowPage:
    """Page Object for iView Login and Logout flows"""
    
    USERNAME_INPUT = (By.NAME, "login")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = "//button[contains(text(),'Sign in')]"
    LOGOUT_BUTTON = (By.ID, "logoutForm:log_out")
    XPATH_TXT_SIGN_IN = "//span[contains(text(),'Sign in')]"
    
    def __init__(self, driver):
        """
        Initialize page object with driver instance
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_txt_sign_in(self):
        """
        Sign in to the application
        """
        try:
            Utility.is_element_present_by_xpath(
                self.driver,
                MeetNowPage.XPATH_TXT_SIGN_IN
            )
            logger.info('Verified on text sign in')
            return True
        except Exception as e:
            logging.error(f"Error during clicking sign in text: {e}")
            raise

    def enter_user_name_password(self, username, password):    
        try:
            logging.info("Attempting to sign in")
            username_el = self.wait.until(
                EC.visibility_of_element_located(self.USERNAME_INPUT)
            )
            username_el.click()
            username_el.clear()
            username_el.send_keys(username)
            logging.debug(f"Entered username: {username}")
            password_el = self.wait.until(
                EC.visibility_of_element_located(self.PASSWORD_INPUT)
            )
            password_el.clear()
            password_el.send_keys(password)
            logging.debug("Entered password")
            login_btn = self.driver.find_element(*self.LOGIN_BUTTON)
            login_btn.click()
            logging.debug("Clicked login button")
            
            self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
            logging.info("Successfully signed in - logout button detected")
            
        except Exception as e:
            logging.error(f"Error during sign in: {e}")
            Utility.take_screenshot(
                driver=self.driver,
                filename="enter_user_name_password.png"
            )
            raise