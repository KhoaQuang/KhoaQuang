import sys, os
import importlib
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class WebClientLibrary:
    """
    Thin wrapper library for GUI.Web_function.web_clients.Web_Clients
    """

    def __init__(self, launch_auto=None):
        """
        launch_auto: optional, used to add project root into sys.path
        """
        launch_auto = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )
        if launch_auto not in sys.path:
            sys.path.insert(0, launch_auto)

        self.web_client = None

    @keyword("Create Web Client")
    def create_web_client(self, browser, client, iview=None, portal=None, use_local_driver=True):
        """
        Create Web_Clients instance and store it internally.

        Args:
            browser: chrome / firefox / edge
            client:  &{CLIENT}
            portal:  &{PORTAL}
            iview:   &{IVIEW}
        """

        if iview:
            module_path = "GUI.WebClients.IVIEW.functions.Web_clients"
            class_name = "Web_Clients"
            args = (browser, client, iview)
        elif portal:
            module_path = "GUI.WebClients.SWC.functions.SWC_client"
            class_name = "SWC_Clients"
            args = (browser, client, portal)
        elif iview and portal:
            raise ValueError("Provide only one: 'iview' or 'portal'")
        else:
            raise ValueError("Either 'iview' or 'portal' must be provided.")

        module = importlib.import_module(module_path)
        client_class = getattr(module, class_name)

        self.web_client = client_class(
            *args,
            use_local_driver=use_local_driver
        )

        BuiltIn().log("Web Client created successfully", level="INFO")

    @keyword("Call Web Client Method")
    def call_web_client_method(self, method_name, *args):
        """
        Examples:
        Call Web Client Method    sign_in
        Call Web Client Method    open_settings
        """

        if not self.web_client:
            BuiltIn().fail("Web Client is not initialized. Call 'Create Web Client' first.")

        try:
            method = getattr(self.web_client, method_name)
            result = method(*args)

            if result is False:
                BuiltIn().fail(f"Method '{method_name}' returned False")

            BuiltIn().log(f"Method '{method_name}' executed successfully", level="INFO")
            return result

        except Exception as e:
            BuiltIn().log(f"Error calling method '{method_name}': {e}", level="ERROR")
            BuiltIn().fail(f"Call Web Client Method '{method_name}' failed")

    @keyword("Safe Quit Browser")
    def safe_quit_browser(self):
        """ALWAYS safe to call in teardown"""
        try:
            if self.web_client:
                self.web_client.quit()
                BuiltIn().log("Browser closed", level="INFO")
        except Exception as e:
            BuiltIn().log(
                f"Ignore error during quit: {e}",
            )
        finally:
            self.web_client = None