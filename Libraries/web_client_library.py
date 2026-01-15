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
    def create_web_client(self, browser, client, iview, use_local_driver=True):
        """
        Create Web_Clients instance and store it internally

        browser: chrome / firefox / edge
        client:  &{CLIENT}
        iview:   &{IVIEW}
        """

        module = importlib.import_module("GUI.Web_function.Web_clients")
        WebClients = getattr(module, "Web_Clients")

        self.web_client = WebClients(
            browser,
            client,
            iview,
            use_local_driver=use_local_driver
        )

        BuiltIn().log("Web Client created successfully", level="INFO")

    @keyword("Call Web Client Method")
    def call_web_client_method(self, method_name, *args):
        """
        Call ANY method from Web_Clients dynamically

        Examples:
        Call Web Client Method    sign_in
        Call Web Client Method    open_settings
        Call Web Client Method    pressing_option_custom_branding
        """

        if not self.web_client:
            raise RuntimeError("Web Client is not initialized. Call 'Create Web Client' first.")

        return getattr(self.web_client, method_name)(*args)

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