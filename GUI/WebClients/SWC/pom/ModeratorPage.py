from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from robot.api import logger
from Utility.Toggle_Util import ToggleUtil

from Utility.Utility import Utility

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ModeratorPage:
    """Page Object for iView Login and Logout flows"""

    def __init__(self, driver):
        """
        Initialize page object with driver instance
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.CLOSE_POPUP_MICROPHONE_BUTTON = "//div[contains(@class,'header-close-button')]"
        self.TERMINATE_MEETING_BUTTON = "#terminateMeetingMenuItem"
        self.MENU_CONTROLS_BUTTON = "//div[@title='Meeting Controls']"
        self.SUBMIT_BUTTON = "//div[contains(text(), 'Yes')]"
        self.BECOME_MODERATOR_BUTTON = "becomeModeratorMenuItem"
        self.MUTE_ALL_PARTICIPANTS = "toggleMuteAllMenuItem"
        self.MUTE = "muteParticipantMenu"
        self.TICK_MUTE_ALL_BUTTON = " "
        self.ENTER_MODERATOR_PIN_LABEL = "//span[contains(text(), 'Enter Moderator PIN')]"
        self.MODERATOR_PIN_INPUT = "pinCode"
        self.ENTER_BUTTON = "//div[contains(text(), 'Enter')]"

    def handle_meeting_controls(self):
        """
        Handle the close popup microphone button
        """
        try:
            Utility.click_element_by_xpath(
                self.driver,
                self.MENU_CONTROLS_BUTTON
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
                self.TERMINATE_MEETING_BUTTON
            )
            logging.info('Terminate meeting button clicked')
            Utility.click_element_by_xpath(
                self.driver,
                self.SUBMIT_BUTTON
            )
            logging.info('Submit button clicked')
            return True
        
        except Exception as e:
            logging.error(f"Error during handle the terminate meeting button: {e}")
            raise

    def become_moderator(self, moderator_pin):
        """
        Handle the close popup microphone button
        """
        try:
            become_moderator = Utility.find_element(
                self.driver,
                self.BECOME_MODERATOR_BUTTON,
                by=By.ID,
                name="Become moderator button" 
            )
            become_moderator.click()
            logging.info('Become moderator button clicked')
            Utility.is_element_visible_by_xpath(
                self.driver,
                self.ENTER_MODERATOR_PIN_LABEL,
                name="Enter moderator pin label"    
            )
            logging.info('Verified on enter moderator pin label')
            enter_pin_mod = Utility.find_element(
                self.driver,
                self.MODERATOR_PIN_INPUT,
                by=By.ID,
                name="Moderator PIN input field"
            )
            enter_pin_mod.click()
            enter_pin_mod.clear()
            enter_pin_mod.send_keys(moderator_pin)
            logging.info('Moderator PIN entered successfully')
            Utility.click_element_by_xpath(
                self.driver,
                self.ENTER_BUTTON
            )
            return True
        
        except Exception as e:
            logging.error(f"Error during handle the become moderator button: {e}")
            raise

    def mute_all_participants(self):
        try:
            mute = Utility.find_element(
                self.driver,
                self.MUTE,
                by=By.ID,
                name="Mute button" 
            )
            mute.click()
            logging.info('Mute button clicked')
            Utility.is_element_visible_by_xpath(
                self.driver,
                self.MUTE_ALL_PARTICIPANTS,
                name="Mute All Participants label"    
            )
            logging.info('Verified on Mute All Participants label')
            mute_all_partipants = Utility.find_element(
                self.driver,
                self.MUTE_ALL_PARTICIPANTS,
                by=By.ID,
                name="Mute All Participants button"
            )
            mute_all_partipants.click()
            logging.info('Pressed button Mute All Participants successfully')
            tick_el = Utility.find_element(
                self.driver,
                By.XPATH,
                self.TICK_MUTE_ALL_BUTTON
            )
            if ToggleUtil.is_tick_enabled(tick_el, "active"):
                logging.info("Tick is ENABLED")
            else:
                logging.info("Tick is DISABLED")
                raise
            return True
        
        except Exception as e:
            logging.error(f"Error during handle the become moderator button: {e}")
            raise