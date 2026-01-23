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
    
    USERNAME_INPUT = (By.NAME, "login")
    PASSWORD_INPUT = (By.NAME, "password")
    SIGN_IN_BUTTON = "//button[contains(text(),'Sign in')]"
    AVATAR_USER_BUTTON = "//div[contains(@class,'avatar')]"
    SIGN_OUT_BUTTON = "//button[contains(text(),'Sign out')]"
    XPATH_TXT_SIGN_IN = "//span[contains(text(),'Sign in')]"
    VERIFY_USER_PORTAL_TEXT = (By.CSS_SELECTOR, "span.user-name")
    BACK_TO_IVIEW_DASHBOARD = (By.XPATH, "//div[contains(@class,'join-page')]")
    MEETING_ID_INPUT = (By.XPATH, "//input[contains(@formcontrolname, 'meetingId')]")
    JOIN_MEETING_BUTTON = "//span[contains(text(),'Join with Browser')]"
    
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
            Utility.click_element_by_xpath(
                self.driver,
                MeetNowPage.XPATH_TXT_SIGN_IN
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
            Utility.is_element_present_by_xpath(
                self.driver,
                MeetNowPage.AVATAR_USER_BUTTON
            )
            logger.info('Verified on avatar user button')
            Utility.click_element_by_xpath(
                self.driver,
                MeetNowPage.AVATAR_USER_BUTTON
            )
            logger.info('Clicked avatar user button')
            Utility.click_element_by_xpath(
                self.driver,
                MeetNowPage.SIGN_OUT_BUTTON
            )
            Utility.is_element_present_by_xpath(
                self.driver,
                MeetNowPage.XPATH_TXT_SIGN_IN
            )
            logger.info('Verified on sign in button')
            return True
        
        except Exception as e:
            logging.error(f"Error during clicking sign in text: {e}")
            raise

    def enter_user_name_password(self, userportal, password):    
        try:
            logging.info("Attempting to sign in")
            self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
            logging.info(f"URL: {self.driver.current_url}")
            if not userportal:
                raise ValueError("Username (userportal) is None or empty")
            if not password:
                raise ValueError("Password is None or empty")
            username_el = self.wait.until(
                EC.presence_of_element_located(self.USERNAME_INPUT)
            )
            username_el.click()
            username_el.clear()
            logging.info(f"Entered click and clear info")
            username_el.send_keys(userportal)
            logging.info(f"Entered username: {userportal}")
            password_el = self.wait.until(
                EC.presence_of_element_located(self.PASSWORD_INPUT)
            )
            password_el.clear()
            password_el.send_keys(password)
            logging.info("Entered password")
            Utility.click_element_by_xpath(
                self.driver,
                MeetNowPage.SIGN_IN_BUTTON
            )
            logging.info("Clicked Sign in button")
            time.sleep(5)
            Utility.click_element_by_xpath(
                self.driver,
                MeetNowPage.AVATAR_USER_BUTTON
            )
            logging.info("Clicked user avatar button")
            Utility.is_element_present_by_xpath(
                self.driver,
                MeetNowPage.SIGN_OUT_BUTTON
            )
            logging.info("Successfully signed in - sign out button detected")
            self.wait.until(
                EC.presence_of_element_located(self.BACK_TO_IVIEW_DASHBOARD)
            ).click()
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

        user_el = self.wait.until(
            EC.visibility_of_element_located(self.VERIFY_USER_PORTAL_TEXT)
        )
        return user_el.text.strip()
    
    def enter_meeting_id(self, meeting_id):
        try:
            logging.info("Attempting to enter meeting ID")
            meeting_id_input = self.wait.until(
                EC.presence_of_element_located(self.MEETING_ID_INPUT)
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
    def click_join_meeting(self):
        try:
            Utility.click_element_by_xpath(
                self.driver,
                MeetNowPage.JOIN_MEETING_BUTTON
            )
            logging.info("Clicked Join Meeting button successfully")
            return True
        
        except Exception as e:
            logging.error(f"Error clicking Join Meeting button: {e}")
            Utility.take_screenshot(
                driver=self.driver,
                filename="click_join_meeting.png"
            )
            raise