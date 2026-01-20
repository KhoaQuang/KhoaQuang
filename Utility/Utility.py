from datetime import datetime
import logging
import os
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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