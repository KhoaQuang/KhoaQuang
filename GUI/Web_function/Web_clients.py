from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import sys,os,time
import logging
from robot.api import logger
from GUI.POM.LoginIVIEWpage import LoginIVIEWpage
from GUI.POM.SettingsIVIEWpage import SettingsIVIEWpage
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),   # 👉 in ra terminal
        logging.FileHandler("automation.log", mode="a", encoding="utf-8")
    ]
)
logger = logging.getLogger()
file_handler = logging.FileHandler(r'E:\Backupwin11\Launch-auto\LOGS\Web_clients.log', mode='w')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
class Web_Clients:
    def __init__(self, browser, client, iview_info, use_local_driver=True):
        self.browser = browser.lower()
        self.client_ip  = client.get("host", "localhost")
        self.client_port = client.get("port", "4444")
        self.iview_url          = iview_info.get('iview_address')
        self.iview_username     = iview_info.get('iview_username')
        self.iview_password     = iview_info.get('iview_password')
        self.screenshot_dir     = client.get('screenshot_dir')
        self.driver_dir = r"C:\Auto_Browsers"
        self.use_local_driver = use_local_driver
        if self.browser == "chrome":
            self._setup_chrome()
        elif self.browser == "firefox":
            self._setup_firefox()
        elif self.browser == "edge":
            self._setup_edge()
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")
    def _take_screenshot(self, filename):
        try:
            screenshot_path = os.path.join(self.screenshot_dir, filename)
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Screenshot saved to {screenshot_path}")
        except Exception as e:
            logging.error(f"Error saving screenshot: {e}")
            raise

    def _setup_driver(self, browser_name, service, options):
        try:
            logging.info(f"Setting up {browser_name} driver")
            if self.use_local_driver:
                # Use local driver binary via Service
                logging.info(f"Using local {browser_name} driver at {service.path}")
                if browser_name == "chrome":
                    self.driver = webdriver.Chrome(service=service, options=options)
                elif browser_name == "firefox":
                    self.driver = webdriver.Firefox(service=service, options=options)
                elif browser_name == "edge":
                    self.driver = webdriver.Edge(service=service, options=options)
                else:
                    raise ValueError(f"Unsupported browser for local driver: {browser_name}")
            else:
                logging.info(f"Connecting to Selenium Grid at http://{self.client_ip}:{self.client_port}/wd/hub")
                self.driver = webdriver.Remote(
                    command_executor=f'http://{self.client_ip}:{self.client_port}/wd/hub',
                    options=options
                )
            self.driver.set_window_position(0, 0)
            self.driver.maximize_window()
            logging.info(f"{browser_name} driver setup successfully")
        except Exception as e:
            logging.error(f"Error setting up {browser_name} driver: {e}")
            raise

    def _setup_chrome(self):
        logging.info('%s' %self.iview_url)
        logging.info('Start function _setup_chrome')
        try:
            self.chrome_options = ChromeOptions()
            self.chrome_options.add_argument("--disable-application-cache")
            self.chrome_options.add_argument("--disable-user-media-security=true")
            self.chrome_options.add_argument("--incognito")
            self.chrome_options.add_argument("--disable-usb-discovery")
            self.chrome_options.add_argument("--ignore-certificate-errors")
            driver_path = os.path.join(self.driver_dir, "chromedriver.exe")
            if not os.path.exists(driver_path):
                raise FileNotFoundError(f"ChromeDriver not found at {driver_path}")

            self.service = ChromeService(driver_path)
            self._setup_driver("chrome", self.service, self.chrome_options)
            logging.info(f"Navigating to URL: {self.iview_url}")
            self.driver.get(self.iview_url) 
        except Exception as e:
            logging.error(f"Error setting up Chrome: {e}")
            raise

    def _setup_firefox(self):
        try:
            self.firefox_options = FirefoxOptions()
            self.firefox_options.add_argument("--ignore-certificate-errors")
            self.firefox_options.add_argument("--disable-application-cache")
            self.firefox_options.add_argument("--disable-popup-blocking")
            driver_path = os.path.join(self.driver_dir, "geckodriver.exe")
            if not os.path.exists(driver_path):
                raise FileNotFoundError(f"GeckoDriver not found at {driver_path}")

            self.service = FirefoxService(driver_path)
            self._setup_driver("firefox", self.service, self.firefox_options)
            logging.info("Browser launched successfully.")
            logging.info(f"Navigating to URL: {self.iview_url}")
            self.driver.get(self.iview_url) 
        except Exception as e:
            logging.error(f"Error setting up Firefox: {e}")
            raise

    def _setup_edge(self):
        try:
            self.edge_options = EdgeOptions()
            self.edge_options.add_argument("--disable-application-cache")
            self.edge_options.add_argument("--disable-popup-blocking")
            self.edge_options.add_argument("--ignore-certificate-errors")
            driver_path = os.path.join(self.driver_dir, "msedgedriver.exe")
            if not os.path.exists(driver_path):
                raise FileNotFoundError(f"EdgeDriver not found at {driver_path}")

            self.service = EdgeService(driver_path)
            self._setup_driver("edge", self.service, self.edge_options)
            logging.info("Browser launched successfully.")
            logging.info(f"Navigating to URL: {self.iview_url}")
            self.driver.get(self.iview_url) 
        except Exception as e:
            logging.error(f"Error setting up Edge: {e}")
            raise

    def quit(self):
        try:
            logging.info("Attempting to quit the browser")
            self.driver.quit()
            logging.info("Browser quit successfully")
        except Exception as e:
            logging.error(f"Error quitting the browser: {e}")
            raise
    
    def sign_in(self, id_iview=None, pw_iview=None, admin_login=None):
        """Sign in using MeetNowPage POM"""
        try:
            username = id_iview or self.iview_username
            pwd = pw_iview or self.iview_password
            page = LoginIVIEWpage(self.driver)
            page.sign_in(username, pwd)
        except Exception as e:
            logging.error(f"Error signing in: {e}")
            self._take_screenshot("sign_in_error.png")
            raise

    def sign_out(self):
        """Sign out using MeetNowPage POM"""
        try:
            page = LoginIVIEWpage(self.driver)
            page.sign_out()
        except Exception as e:
            logging.error(f"Error signing out: {e}")
            self._take_screenshot("sign_out_error.png")
            raise

    def open_settings(self):
        """Open settings using SettingsIVIEWpage POM"""
        try:
            page = SettingsIVIEWpage(self.driver)
            page.open_settings()
        except Exception as e:
            logging.error(f"Error opening settings: {e}")
            self._take_screenshot("open_settings_error.png")
            raise

    def open_user_portal(self):
        """Open user portal using SettingsIVIEWpage POM"""
        try:
            page = SettingsIVIEWpage(self.driver)
            page.open_user_portal()
        except Exception as e:
            logging.error(f"Error opening user portal: {e}")
            self._take_screenshot("open_user_portal_error.png")
            raise

    def pressing_option_custom_branding(self):
        try: 
            page = SettingsIVIEWpage(self.driver)
            page.option_custom_branding()
        except Exception as e:
            logging.error(f"Error opening custom branding option: {e}")
            self._take_screenshot("open_custom_branding_error.png")
            raise