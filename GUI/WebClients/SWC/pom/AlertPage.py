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

class AlertPage:
    """Page Object for iView Login and Logout flows"""


    CLOSE_POPUP_MICROPHONE_BUTTON = "//div[contains(@class,'header-close-button')]"
    CLOSE_POPUP_VIDEO_BUTTON = "//div[contains(@class,'header-close-button')]"

    def __init__(self, driver):
        """
        Initialize page object with driver instance
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def handle_close_popup_microphone(self):
        """
        Handle the close popup microphone button
        """
        try:
            Utility.click_element_by_xpath(
                self.driver,
                AlertPage.CLOSE_POPUP_MICROPHONE_BUTTON
            )
            logging.info('Close popup microphone button clicked')
            return True
        
        except Exception as e:
            logging.error(f"Error during handle the close popup microphone button: {e}")
            raise

    def handle_close_popup_video(self):
        """
        Handle the close popup microphone button
        """
        try:
            Utility.click_element_by_xpath(
                self.driver,
                AlertPage.CLOSE_POPUP_VIDEO_BUTTON
            )
            logging.info('Close popup video button clicked')
            return True
        
        except Exception as e:
            logging.error(f"Error during handle the close popup video button: {e}")
            raise        