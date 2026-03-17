import time
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
    
    
    def __init__(self, driver):
        """
        Initialize page object with driver instance
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.USERNAME_INPUT = "login"
        self.PASSWORD_INPUT = "password"
        self.SIGN_IN_BUTTON = "//button[contains(text(),'Sign in')]"
        self.AVATAR_USER_BUTTON = "//div[contains(@class,'avatar')]"
        self.SIGN_OUT_BUTTON = "//button[contains(text(),'Sign out')]"
        self.XPATH_TXT_SIGN_IN = "//span[contains(text(),'Sign in')]"
        self.VERIFY_USER_PORTAL_TEXT = "span.user-name"
        self.BACK_TO_IVIEW_DASHBOARD = "//div[contains(@class,'join-page')]"
        self.MEETING_ID_INPUT = "//input[contains(@formcontrolname, 'meetingId')]"
        self.JOIN_WITH_BROWSER_BUTTON = "//span[contains(text(),'Join with Browser')]"
        self.MEETING_PIN_INPUT = "pinCode"
        self.ENTER_BUTTON = "//div[contains(text(), 'Enter')]"

    def click_txt_sign_in(self):
        """
        Sign in to the application
        """
        try:
            time.sleep(20)
            Utility.is_element_visible_by_xpath(
                self.driver,
                self.XPATH_TXT_SIGN_IN
            )
            logger.info('Verified on text sign in')
            time.sleep(20)
            Utility.click_element_by_xpath(
                self.driver,
                self.XPATH_TXT_SIGN_IN
            )
            return True
        except Exception as e:
            logging.error(f"Error during clicking sign in text: {e}")
            raise

    def click_txt_sign_out(self):
        """
        Sign in to the application
        """
        try:
            Utility.is_element_visible_by_xpath(
                self.driver,
                self.AVATAR_USER_BUTTON
            )
            logger.info('Verified on avatar user button')
            Utility.click_element_by_xpath(
                self.driver,
                self.AVATAR_USER_BUTTON
            )
            logger.info('Clicked avatar user button')
            Utility.click_element_by_xpath(
                self.driver,
                self.SIGN_OUT_BUTTON
            )
            Utility.is_element_visible_by_xpath(
                self.driver,
                self.XPATH_TXT_SIGN_IN
            )
            logger.info('Verified on sign in button')
            return True
        
        except Exception as e:
            logging.error(f"Error during clicking sign in text: {e}")
            raise

    def enter_user_name_password(self, username, password):    
        try:
            logging.info("Attempting to sign in")
            self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
            logging.info(f"URL: {self.driver.current_url}")
            if not username:
                raise ValueError("Username is None or empty")
            if not password:
                raise ValueError("Password is None or empty")
            username_el = Utility.wait_for_clickable(
                self.driver, 
                self.USERNAME_INPUT,
                by=By.NAME
            )
            username_el.click()
            username_el.clear()
            logging.info(f"Entered click and clear info")
            username_el.send_keys(username)
            logging.info(f"Entered username: {username}")
            password_el = Utility.wait_for_clickable(
                self.driver,
                self.PASSWORD_INPUT,
                by=By.NAME
            )
            password_el.click()
            password_el.clear()
            password_el.send_keys(password)
            logging.info("Entered password")
            Utility.click_element_by_xpath(
                self.driver,
                self.SIGN_IN_BUTTON
            )
            logging.info("Clicked Sign in button")
            time.sleep(5)
            Utility.click_element_by_xpath(
                self.driver,
                self.AVATAR_USER_BUTTON
            )
            logging.info("Clicked user avatar button")
            Utility.is_element_visible_by_xpath(
                self.driver,
                self.SIGN_OUT_BUTTON
            )
            logging.info("Successfully signed in - sign out button detected")
            Utility.click_element_by_xpath(
                self.driver,
                self.BACK_TO_IVIEW_DASHBOARD
            )
            logging.info("Navigated back to the iView dashboard")
            return True
            
        except Exception as e:
            logging.error(f"Error during sign in: {e}")
            Utility.take_screenshot(
                driver=self.driver,
                filename="enter_user_name_password.png"
            )
            return False
        
    def get_user_name(self):
        logging.info("Getting user name from Meet Now page")
        user_el = Utility.wait_for_visible_by_css(
            self.driver,
            self.VERIFY_USER_PORTAL_TEXT,
            name="User name text"
        )
        return user_el.text.strip()
    
    def enter_meeting_id(self, meeting_id):
        try:
            logging.info("Attempting to enter meeting ID")
            meeting_id_input = Utility.wait_for_clickable(
                self.driver,
                self.MEETING_ID_INPUT
            )
            meeting_id_input.clear()
            meeting_id_input.send_keys(meeting_id)
            logging.info(f"Entered meeting ID: {meeting_id}")
            return True
        
        except Exception as e:
            logging.error(f"Error entering meeting ID: {e}")
            Utility.take_screenshot(
                driver=self.driver,
                filename="enter_meeting_id.png"
            )
            raise
    def click_join_with_browser_button(self):
        try:
            Utility.click_element_by_xpath(
                self.driver,
                self.JOIN_WITH_BROWSER_BUTTON
            )
            logging.info("Clicked Join with Browser button successfully")
            return True
        
        except Exception as e:
            logging.error(f"Error clicking Join with Browser button: {e}")
            Utility.take_screenshot(
                driver=self.driver,
                filename="click_join_with_browser.png"
            )
            raise

    def enter_meeting_pin(self, meeting_pin):
        try:
            logging.info("Attempting to enter meeting PIN")
            meeting_pin_input = Utility.wait_for_clickable(
                self.driver,
                self.MEETING_PIN_INPUT
            )
            meeting_pin_input.clear()
            meeting_pin_input.send_keys(meeting_pin)
            logging.info(f"Entered meeting PIN: {meeting_pin}")
            return True
        
        except Exception as e:
            logging.error(f"Error entering meeting PIN: {e}")
            Utility.take_screenshot(
                driver=self.driver,
                filename="enter_meeting_pin.png"
            )
            raise