from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from robot.libraries.BuiltIn import BuiltIn
import sys,os,time
import inspect
import logging
from robot.api import logger
from GUI.WebClients.SWC.pom.MeetNowPage import MeetNowPage
from GUI.WebClients.SWC.pom.RosterListPage import RosterListPage
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("automation.log", mode="a", encoding="utf-8")
    ]
)
logger = logging.getLogger()
logger_bg = logger
logger_main = logger
file_handler = logging.FileHandler(r'E:\Backupwin11\Launch-auto\LOGS\SWC_client.log', mode='w')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
class SWC_Clients:
    def __init__(self, browser, client, portal_info, use_local_driver=True):
        self.browser            = browser.lower()
        self.client_ip          = client.get("host", "localhost")
        self.client_port        = client.get("port", "4444")
        self.portal_url         = portal_info.get('portal_address')
        self.portal_username    = portal_info.get('portal_username')
        self.portal_password    = portal_info.get('portal_password')
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
        logging.info('%s' %self.portal_url)
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
            logging.info(f"Navigating to URL: {self.portal_url}")
            self.driver.get(self.portal_url) 
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
            logging.info(f"Navigating to URL: {self.portal_url}")
            self.driver.get(self.portal_url)
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
            logging.info(f"Navigating to URL: {self.portal_url}")
            self.driver.get(self.portal_url) 
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

    def sign_in_portal(self, user_name=None, password=None, adfs_name=None):
        try:
            '''
                * Function name: sign_in_portal 
                * Description: This function is used to LogIn web portal
                * Parameters:  
                    + user_name: LogIn ID
                    + password: password
                * Ex: sign_in_portal  auto2016000  RAPtor1234
            '''

            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            point = getattr(self, "point", None)
            if point != None and point.is_alive():
                logger = logger_bg
                logger.info('Status is sub thread so log background will be write after back to main thread')
            else:
                logger = logger_main
            logger.info('Start function sign_in_portal')
            # BuiltIn().should_be_true(self.switch_window('unified_portal'),'Switch to main window failed')
            # logger.info('Switch to unified portal window')
            BuiltIn().should_be_true(MeetNowPage.click_txt_sign_in(self.driver),'Click to sign in text failed')
            self.driver_platform.handle_popup_sign_in_on_portal()
            BuiltIn().should_be_true(MeetNowPage.enter_user_name_password(self.driver, user_name, password), 'Enter user name and password failed')
            BuiltIn().should_be_true(MeetNowPage.click_btn_sign_in(self.driver),'Click to sign in button failed')
            logger.info('Verify sign_in_portal')
            time.sleep(2)
            name_display = MeetNowPage.get_user_name(self.driver)
            logger.info('Display name: %s' % name_display)
            if adfs_name is None:
                if user_name in name_display:
                    logger.info('Sign_in_portal successfully')
                    self.result_parallel_execute = "PASSED"
                    return True
            else:
                if adfs_name in name_display:
                    logger.info('Sign_in_portal successfully')
                    self.result_parallel_execute = "PASSED"
                    return True
            self.result_parallel_execute = "FAILED"
            self.fail('Wrong display name after sign in user %s' % user_name)
        except Exception as e:
            self.result_parallel_execute = "FAILED"
            logger.exception("Sign in portal failed")
            raise

    def verify_sign_in_portal(self, user_name, password):
        try:
            if self.sign_in_portal(user_name, password):
                return True
            else:
                return False
        except:
            logger.info('Function exception: '+str(sys.exc_info()))
            return False
    
    def verify_in_meeting(self, my_name):
        try:
            ''' 
                * Function name: verify_in_meeting 
                * Description: This function is used to verify new participant to join the meeting
                * Parameters:  
                    + my_name: display name participant after join meeting
                * Author: Hao Nguyen
                * Date: Feb, 2019
                * Ex: verify_in_meeting  auto2016000
                * Modify by: 
                * Date
            '''
            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            logger.info('Start verify_in_meeting')
            WebDriverWait(self.driver, 20).until(EC.number_of_windows_to_be(2))
            self.switch_window('conference_window')
            time_out = 60
            past_time = int(time.time())
            current_time = past_time
            while(current_time-past_time < time_out):
                logger.info('Wait for loading roster participant %s second' % int(current_time-past_time))
                current_time = int(time.time())
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.db_btn.ng-binding#dismissBtn'))
                    )
                    logger.info('Found dismiss pop up')
                    self.driver.find_element(By.CSS_SELECTOR, 'button.db_btn.ng-binding#dismissBtn').click()
                except:
                    logger.info('Dismiss button not found')
                if RosterListPage.find_participant_in_roster_list(self.driver, my_name):
                    try:
                        logger.info('Handle unblock video!')
                        self.handle_popup_during_meeting()
                        self.handle_unblock_video()
                    except:
                        pass
                    logger.info('verify_in_meeting susccessfuly')
                    self.result_parallel_execute = "PASSED"
                    return True
            self.result_parallel_execute = "FAILED"
            self.fail('verify_in_meeting unsusccessfuly')
        except:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: '+str(sys.exc_info()))

    def sign_out(self):
        try:
            '''
                * Function name: sign_out_portal 
                * Description: This function is used to logout web portal 
                * Parameters:  None
                * Author: Dong Nguyen
                * Date: Feb, 2019
                * Ex: sign_out_portal
                * Modify by: 
                * Date
            '''
            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            if self.point != None and self.point.is_alive():
                logger = logger_bg
                logger.info('Status is sub thread so log background will be write after back to main thread')
            else:
                logger = logger_main
            logger.info('Start function sign_out_portal')
            self.assertTrue(self.switch_window('unified_portal'),'Switch to main window failed')
            self.assertTrue(MeetNowPage.MeetNowPage().click_btn_txt_user_name(self.driver), 'click to user name failed')
            self.assertTrue(MeetNowPage.MeetNowPage().click_btn_sign_out(self.driver), 'Click signout button failed')
            logger.info('verify sign_out_portal')
            self.assertTrue(MeetNowPage.MeetNowPage().wait_for_btn_sign_in(self.driver, 20), 'Not found sign in button')
            logger.info('Sign_out_portal susccessfuly')
            self.result_parallel_execute = "PASSED"
            return True
        except:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: '+str(sys.exc_info()))
