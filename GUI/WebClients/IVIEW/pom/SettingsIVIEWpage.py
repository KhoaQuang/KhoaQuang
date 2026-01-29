from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from selenium.common.exceptions import TimeoutException

from Utility.Utility import Utility

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SettingsIVIEWpage:
    """Page Object for iView Settings flows"""
    
    SETTINGS_BUTTON = (By.ID, "icm_setting")
    USER_PORTAL = (By.XPATH, "//div[contains(@id, 'leftBarPanel')]//a[contains(@id, 'menuForm:menu1021Link')]")
    USER_PORTAL_TITLE = (By.XPATH, "//div[contains(@id, 'rightContentSubPanel')]")
    Custom_Branding_Option = (By.XPATH, "//div[contains(@id,'upcsgTabs')]//a[contains(@class,'customBranding_tab')]")
    Organization_TITLE = (By.XPATH, "//span[normalize-space()='Organization']")
    BUTTON_ADVANCED_BRANDING = (By.XPATH,"//label[normalize-space()='Enable advanced branding']")
    TEXT_ADJUSTMENT = (By.XPATH, "//div[@class='v-captiontext' and text()='Text adjustment']")

    
    def __init__(self, driver):
        """
        Initialize page object with driver instance
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

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
            custom_branding_portal = self.wait.until(EC.element_to_be_clickable(self.Custom_Branding_Option))
            logging.info("Custom branding option is visible")
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", custom_branding_portal)
            custom_branding_portal.click()
            logging.info("Custom branding option clicked successfully")
            logging.info("Waiting for Custom Branding content")
            logging.info(f"Waiting for title locator: {self.Organization_TITLE}")
            logging.info("Custom Branding content loaded")
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
            logging.info(f"Total iframes after clicking tab: {len(iframes)}")

            for idx, iframe in enumerate(iframes):
                logging.info(f"Iframe {idx} src={iframe.get_attribute('src')}")

        except Exception as e:
            logging.error(f"Error opening custom branding option: {e}")
            return False

    def open_section_if_needed(self):
        wait = WebDriverWait(self.driver, 20)
        tab_xpath = "//div[contains(@id,'upcsgTabs')]//a[contains(@class,'customBranding_tab')]"
        logging.info("Opening Custom Branding tab")
        tab = wait.until(EC.element_to_be_clickable((By.XPATH, tab_xpath)))
        self.driver.execute_script("arguments[0].click();", tab)
        time.sleep(2)  
        Utility.switch_to_iframe_by_src(self.driver, "#!Branding")
        wait.until(
            EC.presence_of_element_located(
                (self.BUTTON_ADVANCED_BRANDING)
            )
        )
        logging.info("Custom Branding content loaded successfully")

    def enable_advanced_branding(self):
        try:
            logging.info("Attempting to enable advanced branding")
            self.open_section_if_needed()
            wait = WebDriverWait(self.driver, 20)
            label = wait.until(
                EC.visibility_of_element_located(
                    (self.BUTTON_ADVANCED_BRANDING)
                )
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", label
            )

            checkbox = label.find_element(By.XPATH, "//label[normalize-space()='Enable advanced branding']")

            if not checkbox.is_selected():
                logging.info("Button Enable advanced branding is not selected, clicking it now")
                self.driver.execute_script("arguments[0].click();", checkbox)
                logging.info("Advanced branding enabled")
            else:
                logging.info("Advanced branding already enabled")

            self.driver.switch_to.default_content()
            Utility.switch_to_iframe_by_src(self.driver, "#!Branding")
            WebDriverWait(self.driver, 30).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

            WebDriverWait(self.driver, 30).until(
                lambda d: "Text Adjustment" in d.page_source
            )

            elements = self.driver.find_elements(By.XPATH, self.TEXT_ADJUSTMENT)
            logging.info(f"Text Adjustment elements found: {len(elements)}")

            if not elements:
                BuiltIn().fail("Text Adjustment UI not rendered after enabling branding")

            text_adjustment = elements[0]
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                text_adjustment
            )
            self.driver.execute_script("arguments[0].click();", text_adjustment)
            logging.info("Text adjustment option clicked successfully")
            return True

        except Exception as e:
            self.driver.switch_to.default_content()
            logging.exception("Enable advanced branding crashed")
            BuiltIn().fail(f"Enable advanced branding failed: {e}")