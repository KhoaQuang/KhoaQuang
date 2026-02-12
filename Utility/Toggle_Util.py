from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from selenium.common.exceptions import TimeoutException


class ToggleUtil:

    @staticmethod
    def is_enabled(checkbox_input):
        """
        checkbox_input: <input type="checkbox">
        """
        return checkbox_input.is_selected()
    
    @staticmethod
    def is_tick_enabled(element, enabled_classes):
        """
        enabled_classes: str | list[str] | tuple[str]
        Example:
            "active"
            ["active", "checked"]
        """
        if isinstance(enabled_classes, str):
            enabled_classes = [enabled_classes]

        class_attr = element.get_attribute("class") or ""

        return any(cls in class_attr.split() for cls in enabled_classes)

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

    @staticmethod
    def log_checkbox_state(element, name="Checkbox"):
        try:
            checked = element.get_attribute("checked")
            aria = element.get_attribute("aria-checked")
            classes = element.get_attribute("class")

            logging.info(
                f"{name} state | checked={checked}, aria-checked={aria}, class={classes}"
            )
        except Exception as e:
            logging.warning(f"Could not read state of {name}: {e}")

    @staticmethod
    def enable_by_class(
        driver,
        element,
        enabled_classes,
        name=None,
        timeout=10
    ):
        label = name or "Class toggle"

        if ToggleUtil.is_tick_enabled(element, enabled_classes):
            logging.info(f"[{label}] already ENABLED ({enabled_classes})")
            return

        logging.info(f"[{label}] NOT enabled → clicking")
        driver.execute_script("arguments[0].click();", element)

        try:
            WebDriverWait(driver, timeout).until(
                lambda d: ToggleUtil.is_tick_enabled(element, enabled_classes)
            )
            logging.info(f"[{label}] ENABLED successfully")

        except TimeoutException:
            logging.error(
                f"[{label}] still NOT enabled after click "
                f"(expected classes: {enabled_classes})"
            )
            raise

    @staticmethod
    def disable_by_class(
        driver,
        element,
        enabled_classes,
        name=None,
        timeout=10
    ):
        label = name or "Class toggle"

        if not ToggleUtil.is_tick_enabled(element, enabled_classes):
            logging.info(f"[{label}] already DISABLED")
            return

        logging.info(f"[{label}] ENABLED → clicking to disable")
        driver.execute_script("arguments[0].click();", element)

        try:
            WebDriverWait(driver, timeout).until(
                lambda d: not ToggleUtil.is_tick_enabled(element, enabled_classes)
            )
            logging.info(f"[{label}] DISABLED successfully")

        except TimeoutException:
            logging.error(
                f"[{label}] still ENABLED after click "
                f"(classes: {enabled_classes})"
            )
            raise
