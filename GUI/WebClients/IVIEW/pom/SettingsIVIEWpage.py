from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import TimeoutException

from Utility.Toggle_Util import ToggleUtil
from Utility.Utility import Utility

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SettingsIVIEWpage:
    """Page Object for iView Settings flows"""
    
    def __init__(self, driver):
        """
        Initialize page object with driver instance
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

        self.IFRAMES = "iframe"
        self.SETTINGS_BUTTON = (By.ID, "icm_setting")
        self.USER_PORTAL = (By.XPATH, "//div[contains(@id, 'leftBarPanel')]//a[contains(@id, 'menuForm:menu1021Link')]")
        self.USER_PORTAL_TITLE = (By.XPATH, "//div[contains(@id, 'rightContentSubPanel')]")
        self.Custom_Branding_Option = "//div[contains(@id,'upcsgTabs')]//a[contains(@class,'customBranding_tab')]"
        self.Organization_TITLE = "//span[normalize-space()='Organization']"
        self.BUTTON_ADVANCED_BRANDING = "//label[normalize-space()='Enable advanced branding']"
        self.CHECKBOX_ADVANCED_BRANDING = "//span[contains(@class,'v-checkbox')]//input[@type='checkbox']"
        self.TEXT_ADJUSTMENT = "//div[@class='v-captiontext' and text()='Text adjustment']"

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
            return False


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
            return False

    def option_custom_branding(self):
        try:
            logging.info("Attempting to open custom branding option") 
            custom_branding_portal = Utility.wait_for_clickable(
                self.driver, 
                self.Custom_Branding_Option,
                name="Custom Branding tab",
                by=By.XPATH
            )
            logging.info("Custom branding option is visible")
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", custom_branding_portal)
            custom_branding_portal.click()
            logging.info("Custom branding option clicked successfully")
            Utility.switch_to_iframe_by_src(self.driver, "#!Branding")
            logging.info("Waiting for Custom Branding content")
            logging.info(f"Waiting for title locator: {self.Organization_TITLE}")
            Utility.find_element(self.driver, By.XPATH, self.Organization_TITLE)
            logging.info("Custom Branding content loaded")
            iframes = Utility.find_elements(self.driver, By.TAG_NAME, self.IFRAMES)
            logging.info(f"Total iframes after clicking tab: {len(iframes)}")

            for idx, iframe in enumerate(iframes):
                logging.info(f"Iframe {idx} src={iframe.get_attribute('src')}")

        except Exception as e:
            logging.error(f"Error opening custom branding option: {e}")
            return False
        finally:
            self.driver.switch_to.default_content()
            logging.info("Exited iframe safely")

    def open_section_if_needed(self):
        logging.info("Opening Custom Branding tab")
        tab = Utility.find_element(self.driver, By.XPATH, self.Custom_Branding_Option)
        self.driver.execute_script("arguments[0].click();", tab)
        time.sleep(2)  
        Utility.switch_to_iframe_by_src(self.driver, "#!Branding")
        Utility.find_element(
            self.driver,
            By.XPATH,
            self.BUTTON_ADVANCED_BRANDING
        )
        logging.info("Custom Branding content loaded successfully")

    def enable_advanced_branding(self):
        try:
            logging.info("Attempting to enable advanced branding")
            self.open_section_if_needed()
            label = Utility.find_element(
                self.driver,
                By.XPATH,
                self.BUTTON_ADVANCED_BRANDING,
                name="Enable Advanced Branding Label"
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", label
            )
            checkbox = Utility.find_element(
                self.driver,
                By.XPATH,
                self.CHECKBOX_ADVANCED_BRANDING
            )
            ToggleUtil.log_checkbox_state(checkbox, "Advanced Branding")
            ToggleUtil.enable(
                self.driver,
                checkbox,
                label,
                name="Enable advanced branding"
            )

            self.driver.switch_to.default_content()
            Utility.switch_to_iframe_by_src(self.driver, "#!Branding")
            logging.info("Waiting for Text Adjustment to be clickable")
            text_adjustment = Utility.find_element(self.driver, By.XPATH, self.TEXT_ADJUSTMENT)
            logging.info("Text Adjustment is visible")
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                text_adjustment
            )
            self.driver.execute_script("arguments[0].click();", text_adjustment)
            logging.info("Text adjustment option clicked successfully")
            return True

        except Exception as e:
            logging.exception("Enable advanced branding crashed")
            BuiltIn().fail(f"Enable advanced branding failed: {e}")

        finally:
            self.driver.switch_to.default_content()
            logging.info("Exited iframe safely")