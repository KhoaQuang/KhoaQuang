import sys, os
import importlib
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from CONFIG.test_data import TEST_DATA


class WebClientLibrary:
    """
    Thin wrapper library for GUI.Web_function.web_clients.Web_Clients
    """

    def __init__(self, launch_auto=None):
        """
        launch_auto: optional, used to add project root into sys.path
        """
        self.web_clients = {}   # { "A": web_client_A, "B": web_client_B }
        BuiltIn().log(f"INIT WebClientLibrary ID={id(self)}", level="WARN")
        launch_auto = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )
        if launch_auto not in sys.path:
            sys.path.insert(0, launch_auto)

    @keyword("Create Web Client")
    def create_web_client(self, user_key, browser, client, iview=None, portal=None, use_local_driver=True):
        """
        Create Web_Clients instance and store it internally.

        Args:
            user_key: unique identifier for the web client instance
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

        else:
            raise ValueError("Either 'iview' or 'portal' must be provided.")

        module = importlib.import_module(module_path)
        client_class = getattr(module, class_name)

        web_client = client_class(
            *args,
            use_local_driver=use_local_driver
        )

        self.web_clients[user_key] = web_client

        BuiltIn().log(f"Web Client created for user '{user_key}'", level="INFO")

    @keyword("Call Web Client Method")
    def call_web_client_method(self, user_key, method_name, *args):
        """
        Examples:
        Call Web Client Method    sign_in
        Call Web Client Method    open_settings
        """

        if user_key not in self.web_clients:
            BuiltIn().fail(f"Web Client for user '{user_key}' is not initialized.")

        web_client = self.web_clients[user_key]

        try:
            method = getattr(web_client, method_name)
            result = method(*args)

            if result is False:
                BuiltIn().fail(f"Method '{method_name}' returned False")

            BuiltIn().log(
                f"User '{user_key}' executed method '{method_name}' successfully",
                level="INFO"
            )
            return result

        except Exception as e:
            BuiltIn().log(
                f"Error calling method '{method_name}' for user '{user_key}': {e}", level="ERROR"
            )
            BuiltIn().fail(f"Call Web Client Method '{method_name}' failed")

    @keyword("Quit All Browsers")
    def quit_all_browsers(self):

        errors = []

        for user_key, web_client in self.web_clients.items():
            try:
                web_client.quit()
                BuiltIn().log(
                    f"Browser closed for user '{user_key}'",
                    level="INFO"
                )
            except Exception as e:
                errors.append(f"{user_key}: {e}")
                BuiltIn().log(
                    f"Ignore quit error for {user_key}: {e}",
                    level="WARN"
                )

        self.web_clients.clear()

        if errors:
            BuiltIn().log(
                f"Quit errors occurred: {errors}",
                level="WARN"
            )