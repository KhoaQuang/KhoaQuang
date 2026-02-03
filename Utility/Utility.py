from datetime import datetime
import logging
from operator import index
import os
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Utility:
    """
    Common Selenium actions
    Used by IVIEW & SWC
    No assertion, no business logic
    """
    screenshot_dir = os.path.join(os.getcwd(), "Screenshots")

    @staticmethod
    def take_screenshot(driver, filename):
        try:
            os.makedirs(Utility.screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(
                Utility.screenshot_dir,
                f"{timestamp}_{filename}"
            )

            driver.save_screenshot(screenshot_path)
            logging.info(f"Screenshot saved to {screenshot_path}")

        except Exception as e:
            logging.error(f"Error saving screenshot: {e}")

    @staticmethod
    def click_element_by_xpath(driver, xpath, timeout=10):
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()

    @staticmethod
    def click_element_by_css(driver, css, timeout=10):
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css))
        ).click()

    @staticmethod
    def input_text_by_xpath(driver, xpath, text, timeout=10):
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        element.clear()
        element.send_keys(text)

    @staticmethod
    def input_text_by_css(driver, css, text, timeout=10):
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css))
        )
        element.clear()
        element.send_keys(text)

    @staticmethod
    def get_text_by_xpath(driver, xpath, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        ).text

    @staticmethod
    def get_text_by_css(driver, css, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css))
        ).text

    @staticmethod
    def get_element_by_xpath(driver, xpath, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    @staticmethod
    def is_element_present_by_xpath(driver, xpath, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except:
            return False

    @staticmethod
    def is_element_visible_by_css(driver, css, timeout=5):
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css))
            )
            return True
        except Exception:
            return False
        
    @staticmethod
    def switch_to_iframe_by_src(driver, src_keyword, timeout=10):
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )

        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        logging.info(f"Total iframes found: {len(iframes)}")
        for idx, iframe in enumerate(iframes):
            src = iframe.get_attribute("src") or ""
            logging.info(f"Iframe {idx} src={src}")
            if src_keyword in src:
                logging.info(f"Switching to iframe index {idx} with src containing '{src_keyword}'")
                driver.switch_to.frame(iframe)
                return True

        raise TimeoutException(f"Iframe with src containing '{src_keyword}' not found")
    
    @staticmethod
    def find_element(context, by, locator, name="", timeout=10):
        """
        context: WebDriver OR WebElement
        by: By.XPATH / By.ID / ...
        locator: locator string
        name: optional name for logging purposes
        """

        try:
            logging.info(f"Finding element [{name}] ({by}, {locator})")
            wait = WebDriverWait(context, timeout)

            if hasattr(context, "find_element"):
                element = wait.until(
                    lambda d: context.find_element(by, locator)
                )
                logging.info(f"Element [{name}] found successfully")
                return element
            
            else:
                raise TypeError("Context must be WebDriver or WebElement")

        except TimeoutException:
            logging.error(f"Element not found: ({by}, {locator})")
            raise

    @staticmethod
    def find_elements(driver, by, locator, timeout=10, name=None):
        element_name = name or locator
        logging.info(f"Finding elements: {element_name}")

        try:
            WebDriverWait(driver, timeout).until(
                lambda d: len(d.find_elements(by, locator)) > 0
            )
            elements = driver.find_elements(by, locator)
            logging.info(f"Elements FOUND ({len(elements)}): {element_name}")
            return elements

        except TimeoutException:
            logging.error(f"No elements found after {timeout}s: {element_name}")
            return []
    # @staticmethod
    # def _detect_by(locator: str):
    #     if locator.startswith("//") or locator.startswith("(//"):
    #         return By.XPATH
    #     if locator.startswith("#"):
    #         return By.CSS_SELECTOR
    #     if locator.startswith("."):
    #         return By.CSS_SELECTOR
    #     if locator.startswith("name="):
    #         return By.NAME
    #     return By.ID

    @staticmethod
    def wait_for_clickable(context, locator, timeout=30, name=None, by=By.XPATH):
        """
        context : WebDriver or WebElement
        locator : STRING
        by      : default By.XPATH, có thể override
        """

        element_name = name or locator
        logging.info(f"Waiting for element to be clickable: {element_name}")

        try:
            wait = WebDriverWait(context, timeout)
            element = wait.until(
                EC.element_to_be_clickable((by, locator))
            )
            logging.info(f"Element CLICKABLE: {element_name}")
            return element

        except TimeoutException:
            logging.error(f"Element NOT clickable after {timeout}s: {element_name}")
            raise