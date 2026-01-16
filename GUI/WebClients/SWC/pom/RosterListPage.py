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

class RosterListPage:
    """Page Object for iView Login and Logout flows"""
    
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

    def find_participant_in_roster_list(driver, participant_name):
        """
        Find a participant in the roster list by name.
        
        Args:
            driver: Selenium WebDriver instance
            participant_name: Name of the participant to find in the roster list"""
        try:
            logging.info(f"Searching for participant: {participant_name}")
            roster_list = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "rosterList"))
            )
            participants = roster_list.find_elements(By.CLASS_NAME, "participant-name")
            for participant in participants:
                if participant.text.strip() == participant_name:
                    logging.info(f"Participant '{participant_name}' found in roster list.")
                    return True
            logging.info(f"Participant '{participant_name}' not found in roster list.")
            return False
        except Exception as e:
            logging.error(f"Error while searching for participant '{participant_name}': {e}")
            return False