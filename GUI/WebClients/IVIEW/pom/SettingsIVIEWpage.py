from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from robot.api import logger

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SettingsIVIEWpage:
    """Page Object for iView Settings flows"""
    
    # Element locators (By.ID)
    SETTINGS_BUTTON = (By.ID, "icm_setting")
    USER_PORTAL = (By.XPATH, "//div[contains(@id, 'leftBarPanel')]//a[contains(@id, 'menuForm:menu1021Link')]")
    USER_PORTAL_TITLE = (By.XPATH, "//div[contains(@id, 'rightContentSubPanel')]")
    Custom_Branding_Option = (By.XPATH, "//div[contains(@id,'upcsgTabs')]//a[contains(@class,'customBranding_tab')]")
    Organization_TITLE = (By.XPATH, "//span[normalize-space()='Organization']")

    
    def __init__(self, driver):
        """
        Initialize page object with driver instance
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    def open_settings(self):
        """
        Open the settings page by clicking the settings button
        """
        try:
            logging.info("Attempting to open settings")
            settings_button = self.wait.until(EC.element_to_be_clickable(self.SETTINGS_BUTTON))
            settings_button.click()
            logging.info("Settings button clicked successfully")
        except Exception as e:
            logging.error(f"Error opening settings: {e}")
            raise


    def open_user_portal(self):
        """
        Open the user portal by clicking the user portal link
        """
        try:
            logging.info("Attempting to open user portal")
            user_portal_link = self.wait.until(EC.element_to_be_clickable(self.USER_PORTAL))
            user_portal_link.click()
            logging.info("User portal link clicked")
            self.wait.until(EC.presence_of_element_located(self.USER_PORTAL_TITLE))
            logging.info("User portal page loaded successfully")
        except Exception as e:
            logging.error(f"Error opening user portal: {e}")
            raise

    def option_custom_branding(self):
        try:
            logging.info("Attempting to open custom branding option") 
            custom_branding_portal = self.wait.until(EC.element_to_be_clickable(self.Custom_Branding_Option))
            logging.info("Custom branding option is visible")
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", custom_branding_portal)
            custom_branding_portal.click()
            logging.info("Custom branding option clicked successfully")
            logging.info("Waiting for Custom Branding content")
            # self.wait.until(EC.presence_of_element_located(self.Organization_TITLE))
            logging.info(f"Waiting for title locator: {self.Organization_TITLE}")
            logging.info("Custom Branding content loaded")
        except Exception as e:
            logging.error(f"Error opening custom branding option: {e}")
            raise

