from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from robot.api import logger

from Utility.Utility import Utility

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ModeratorPage:
    """Page Object for iView Login and Logout flows"""


    CLOSE_POPUP_MICROPHONE_BUTTON = "//div[contains(@class,'header-close-button')]"
    TERMINATE_MEETING_BUTTON = "#terminateMeetingMenuItem"
    MENU_CONTROLS_BUTTON = "//div[@title='Meeting Controls']"
    SUBMIT_BUTTON = "//div[contains(text(), 'Yes')]"

    def __init__(self, driver):
        """
        Initialize page object with driver instance
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def handle_meeting_controls(self):
        """
        Handle the close popup microphone button
        """
        try:
            Utility.click_element_by_xpath(
                self.driver,
                ModeratorPage.MENU_CONTROLS_BUTTON
            )
            logging.info('Meeting controls button clicked')
            return True
        
        except Exception as e:
            logging.error(f"Error during handle the meeting controls button: {e}")
            raise
    
    def handle_terminate_meeting(self):
        """
        Handle the terminate meeting button
        """
        try:
            Utility.click_element_by_css(
                self.driver,
                ModeratorPage.TERMINATE_MEETING_BUTTON
            )
            logging.info('Terminate meeting button clicked')
            Utility.click_element_by_xpath(
                self.driver,
                ModeratorPage.SUBMIT_BUTTON
            )
            logging.info('Submit button clicked')
            return True
        
        except Exception as e:
            logging.error(f"Error during handle the terminate meeting button: {e}")
            raise