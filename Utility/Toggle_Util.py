from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time


class ToggleUtil:

    @staticmethod
    def is_enabled(checkbox_input):
        """
        checkbox_input: <input type="checkbox">
        """
        return checkbox_input.is_selected()

    @staticmethod
    def enable(driver, checkbox_input, click_element=None, timeout=10, name="Checkbox"):
        """
        Enable checkbox if not enabled

        checkbox_input : input[type=checkbox]
        click_element  : label / span / container để click (nếu click input không được)
        """

        if ToggleUtil.is_enabled(checkbox_input):
            logging.info(f"[{name}] already enabled")
            return

        logging.info(f"[{name}] is disabled → enabling...")

        target = click_element if click_element else checkbox_input
        driver.execute_script("arguments[0].click();", target)

        WebDriverWait(driver, timeout).until(
            lambda d: checkbox_input.is_selected()
        )

        logging.info(f"[{name}] enabled successfully")

    @staticmethod
    def disable(driver, checkbox_input, click_element=None, timeout=10, name="Checkbox"):
        """
        Disable checkbox if enabled
        """

        if not ToggleUtil.is_enabled(checkbox_input):
            logging.info(f"[{name}] already disabled")
            return

        logging.info(f"[{name}] is enabled → disabling...")

        target = click_element if click_element else checkbox_input
        driver.execute_script("arguments[0].click();", target)

        WebDriverWait(driver, timeout).until(
            lambda d: not checkbox_input.is_selected()
        )

        logging.info(f"[{name}] disabled successfully")
