from asyncio import timeout
from xml.dom.xmlbuilder import Options
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
from GUI.WebClients.SWC.pom.AlertPage import AlertPage
from GUI.WebClients.SWC.pom.MeetNowPage import MeetNowPage
from GUI.WebClients.SWC.pom.RosterListPage import RosterListPage
from GUI.WebClients.SWC.pom.ModeratorPage import ModeratorPage
from Utility.Utility import Utility
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

    def _setup_driver(self, browser_name, service, options):
        try:
            logging.info(f"Setting up {browser_name} driver")
            if self.use_local_driver:
                logging.info(f"Using local {browser_name} driver at {service.path}")
                if browser_name == "chrome":
                    if service is not None:
                        self.driver = webdriver.Chrome(service=service, options=options)
                    else:
                        logging.info("Using Selenium Manager for Chrome driver")
                        self.driver = webdriver.Chrome(options=options)
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

    # def _setup_chrome(self):
    #     logging.info('%s' %self.portal_url)
    #     logging.info('Start function _setup_chrome')
    #     try:
    #         self.chrome_options = ChromeOptions()
    #         self._configure_media_permission("chrome", self.chrome_options)
    #         self.chrome_options.add_argument("--disable-application-cache")
    #         self.chrome_options.add_argument("--disable-user-media-security=true")
    #         self.chrome_options.add_argument("--incognito")
    #         self.chrome_options.add_argument("--disable-usb-discovery")
    #         self.chrome_options.add_argument("--ignore-certificate-errors")
    #         driver_path = os.path.join(self.driver_dir, "chromedriver.exe")
    #         if not os.path.exists(driver_path):
    #             raise FileNotFoundError(f"ChromeDriver not found at {driver_path}")

    #         self.service = ChromeService(driver_path)
    #         self._setup_driver("chrome", self.service, self.chrome_options)
    #         logging.info(f"Navigating to URL: {self.portal_url}")
    #         self.driver.get(self.portal_url) 
    #     except Exception as e:
    #         logging.error(f"Error setting up Chrome: {e}")
    #         raise

    def _setup_chrome(self):
        logging.info('Start function _setup_chrome')
        try:
            self.chrome_options = ChromeOptions()
            self.chrome_options.add_argument("--disable-application-cache")
            self.chrome_options.add_argument("--disable-user-media-security=true")
            self.chrome_options.add_argument("--incognito")
            self.chrome_options.add_argument("--disable-usb-discovery")
            self.chrome_options.add_argument("--ignore-certificate-errors")
            driver_path = os.path.join(self.driver_dir, "chromedriver.exe")

            if os.path.exists(driver_path):
                logging.info(f"Using local ChromeDriver: {driver_path}")
                self.service = ChromeService(driver_path)
                self._setup_driver("chrome", self.service, self.chrome_options)

            else:
                logging.warning("Local ChromeDriver not found. Switching to Selenium Manager (CI mode).")
                logging.info("Running Chrome setup with CI fallback")
                self.chrome_options.add_argument("--headless=new")
                self.chrome_options.add_argument("--no-sandbox")
                self.chrome_options.add_argument("--disable-dev-shm-usage")
                self._setup_driver("chrome", None, self.chrome_options)

            logging.info(f"Navigating to URL: {self.portal_url}")
            self.driver.get(self.portal_url)

        except Exception as e:
            logging.error(f"Error setting up Chrome: {e}")
            raise

    def _setup_firefox(self):
        try:
            self.firefox_options = FirefoxOptions()
            self._configure_media_permission("firefox", self.firefox_options)
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
            self._configure_media_permission("edge", self.edge_options)
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

    def _configure_media_permission(self, browser_name, options):
        if browser_name in ("chrome", "edge"):
            options.add_argument("--use-fake-ui-for-media-stream")
            options.add_argument("--use-fake-device-for-media-stream")

            prefs = {
                "profile.default_content_setting_values.media_stream_mic": 1,
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.content_settings.exceptions.media_stream_mic.*.setting": 1,
            }
            options.add_experimental_option("prefs", prefs)

        elif browser_name == "firefox":
            options.set_preference("permissions.default.microphone", 1)
            options.set_preference("permissions.default.camera", 1)
            options.set_preference("media.navigator.permission.disabled", 1)
            options.set_preference("media.navigator.streams.fake", 1)

    def sign_in_portal(self, username=None, password=None):
        try:
            '''
                * Function name: sign_in_portal 
                * Description: This function is used to LogIn web portal
                * Parameters:  
                    + userportal: LogIn ID
                    + password: password
                * Ex: sign_in_portal  khoa  AvayaMcspv_1234$
            '''

            if username is None:
                username = self.portal_username
            if password is None:
                password = self.portal_password

            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            point = getattr(self, "point", None)
            if point != None and point.is_alive():
                logger = logger_bg
                logger.info('Status is sub thread so log background will be write after back to main thread')
            else:
                logger = logger_main
            logger.info('Start function sign_in_portal')
            MeetNowPage(self.driver).click_txt_sign_in()
            BuiltIn().should_be_true(
                MeetNowPage(self.driver).enter_user_name_password(username, password),
                'Enter user name and password failed'
            )
            logger.info('Verify sign_in_portal')
            time.sleep(2)

        except Exception:
            self.result_parallel_execute = "FAILED"
            logger.exception("Sign in portal failed")
            raise

    def verify_sign_in_portal(self, user_name):
        try:
            actual_name = MeetNowPage(self.driver).get_user_name().lower()
            logger.info(f'Display name: {actual_name}')

            if user_name == actual_name or user_name in actual_name:
                logger.info('Sign_in_portal successfully')
                self.result_parallel_execute = "PASSED"
                return True
            else:
                raise AssertionError(
                    f'Sign_in_portal failed. Expected user: {user_name}, Actual: {actual_name}'
                )

        except Exception:
            logger.exception('Verify sign in portal error')
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: '+str(sys.exc_info()))
    
    def start_my_meeting(self):
        try:
            '''
                * Function name: start_my_meeting 
                * Description: This function is used to start my meeting via web portal 
                * Parameters:  
                    + display_name: display name participant after start meeting
            '''

            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            logger = logger_main
            logger.info('Start function start_my_meeting')
            meet_page = MeetNowPage(self.driver)
            logger.info("Clicking join with browser button...")
            meet_page.click_join_with_browser_button()
            WebDriverWait(self.driver, 20).until(EC.number_of_windows_to_be(2))
            logger.info("Waiting for conference window to open...")
            original_window = self.driver.current_window_handle
            logger.info(f'Original portal window: {original_window}') 
            WebDriverWait(self.driver, 20).until(
                lambda d: len(d.window_handles) > 1
            )
            conference_window = next(
                w for w in self.driver.window_handles if w != original_window
            )
            logger.info(f'Conference window: {conference_window}')
            logger.info(f'Switching to conference window: {conference_window}')
            self.driver.switch_to.window(conference_window)
            WebDriverWait(self.driver, 10).until(
                lambda d: d.current_window_handle == conference_window
            )
            logger.info('Successfully focused on conference window')
            logger.info("join_meeting successfully")
            self.result_parallel_execute = "PASSED"
            return True
        
        except Exception:
            logger.exception('Verify join meeting error')
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: '+str(sys.exc_info()))

    def join_meeting(self, meeting_id):
        try:
            '''
                * Function name: join_meeting 
                * Description: This function is used to join meeting via web portal 
                * Parameters:  
                    + meeting_id: meeting ID to join meeting
                    + display_name: display name participant after join meeting
            '''

            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            logger = logger_main
            logger.info('Start function join_meeting')
            logger.info(f'Entering meeting ID: {meeting_id}')
            meet_page = MeetNowPage(self.driver)
            meet_page.enter_meeting_id(meeting_id)
            logger.info("Clicking join with browser button...")
            meet_page.click_join_with_browser_button()
            WebDriverWait(self.driver, 20).until(EC.number_of_windows_to_be(2))
            logger.info("Waiting for conference window to open...")
            original_window = self.driver.current_window_handle
            logger.info(f'Original portal window: {original_window}') 
            WebDriverWait(self.driver, 20).until(
                lambda d: len(d.window_handles) > 1
            )
            conference_window = next(
                w for w in self.driver.window_handles if w != original_window
            )
            logger.info(f'Conference window: {conference_window}')
            logger.info(f'Switching to conference window: {conference_window}')
            self.driver.switch_to.window(conference_window)
            WebDriverWait(self.driver, 10).until(
                lambda d: d.current_window_handle == conference_window
            )
            logger.info('Successfully focused on conference window')
            logger.info("join_meeting successfully")
            self.result_parallel_execute = "PASSED"
            return True
        
        except Exception:
            logger.exception('Verify join meeting error')
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: '+str(sys.exc_info()))
        
    def handle_unblock_popup(self):
        try:
            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            logger.info('Handle unblock popup')
            handle_popup = AlertPage(self.driver)
            time.sleep(5)
            handle_popup.handle_close_popup_microphone()
            time.sleep(5)
            handle_popup.handle_close_popup_video()
            logger.info('Handle unblock popup successfully')
        except Exception as e:
            logger.error(f"Error during handle unblock popup: {e}")
    
    def verify_in_meeting(self, my_name):
            ''' 
                * Function name: verify_in_meeting 
                * Description: This function is used to verify new participant to join the meeting
                * Parameters:  
                    + my_name: display name participant after join meeting
            '''

            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            logger.info('Start verify_in_meeting')
            time_out = 5
            start_time = time.time()
            popup_handled = False
            while True:
                elapsed = int(time.time() - start_time)
                logger.info(f"Waiting for participant '{my_name}' ({elapsed}s)")
                if elapsed >= time_out:
                    self.result_parallel_execute = "FAILED"
                    raise RuntimeError("verify_in_meeting failed")
                logger.info(f"Waiting for participant '{my_name}' ({elapsed}s)")
                if not popup_handled:
                    try:
                        self.handle_unblock_popup()
                        popup_handled = True
                        logger.info("Popup handled, will not retry")
                    except Exception:
                        logger.debug("Popup not present yet")

                try:
                    found = RosterListPage.find_participant_in_roster_list(self.driver, my_name)
                except Exception as e:
                    logger.warning(f"Roster not ready, retrying: {e}")
                    time.sleep(1)
                    continue

                if found:
                    logger.info(f"Participant '{my_name}' found in roster list. {my_name} joined meeting successfully")
                    self.result_parallel_execute = "PASSED"
                    return True
        
    def switch_window(self, window_type):
        """Switch to a specific window type: 'conference_window' or 'unified_portal'"""
        try:
            logger.info(f'=== SWITCHING TO {window_type} ===')
            logger.info(f'Total windows available: {len(self.driver.window_handles)}')
            logger.info(f'Window handles: {self.driver.window_handles}')
            
            current_window = self.driver.current_window_handle
            logger.info(f'Current window: {current_window}')
            
            if window_type == 'conference_window':
                for window_handle in self.driver.window_handles:
                    if window_handle != current_window:
                        logger.info(f'Switching to conference window: {window_handle}')
                        self.driver.switch_to.window(window_handle)
                        logger.info(f'Switched to: {self.driver.current_window_handle}')
                        logger.info(f'Conference window URL: {self.driver.current_url}')
                        time.sleep(2)
                        return True
                logger.warning('Could not find conference window!')
                return False
                
            elif window_type == 'unified_portal':
                for window_handle in self.driver.window_handles:
                    if 'portal' in window_handle or window_handle == self.driver.window_handles[0]:
                        logger.info(f'Switching to portal window: {window_handle}')
                        self.driver.switch_to.window(window_handle)
                        logger.info(f'Switched to: {self.driver.current_window_handle}')
                        logger.info(f'Portal window URL: {self.driver.current_url}')
                        time.sleep(2)
                        return True
                logger.warning('Could not find portal window!')
                return False
            else:
                logger.error(f'Unknown window type: {window_type}')
                return False
        except Exception as e:
            logger.error(f'Error switching window: {e}')
            return False
        
    def terminate_meeting(self):
        try:
            '''
                * Function name: terminate_meeting 
                * Description: This function is used to terminate meeting via SWC moderator client 
            '''
            
            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            logger = logger_main
            logger.info('Start function terminate_meeting')
            BuiltIn().should_be_true(ModeratorPage(self.driver).handle_meeting_controls(), 'Handle meeting controls failed')
            time.sleep(5)
            BuiltIn().should_be_true(ModeratorPage(self.driver).handle_terminate_meeting(), 'Handle terminate meeting failed')
            time.sleep(5)
            logger.info('Terminate_meeting successfuly')
            self.close_conference_window()
            self.result_parallel_execute = "PASSED"
            return True
        
        except:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: '+str(sys.exc_info()))
        
    def mute_all_participants(self):
        try:
            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            logging.info("Start function mute all participants")
            BuiltIn().should_be_true(ModeratorPage(self.driver).handle_meeting_controls(), 'Handle meeting controls failed')
            time.sleep(5)
            BuiltIn().should_be_true(ModeratorPage(self.driver).mute_all_participants(), 'Handle mute all participants failed')
            time.sleep(5)
            logger.info('Mute all participantsg successfuly')
            self.result_parallel_execute = "PASSED"
            return True
        except:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: '+str(sys.exc_info()))
        
    def close_conference_window(self):
        logger.info('Closing conference window')
        all_windows = self.driver.window_handles
        if len(all_windows) <= 1:
            logger.warning('No conference window to close')
            return

        current = self.driver.current_window_handle
        self.driver.close()
        logger.info(f'Closed window: {current}')
        remaining = self.driver.window_handles[0]
        self.driver.switch_to.window(remaining)
        logger.info(f'Switched back to original window: {remaining}')
        
    def sign_out(self):
        try:
            '''
                * Function name: sign_out_portal 
                * Description: This function is used to logout web portal 
            '''

            logging.info(f"Client IP: {self.client_ip}, Port: {self.client_port}, Function: {inspect.stack()[0][3]}")
            logger = logger_main
            logger.info('Start function sign_out_portal')
            self.close_conference_window()
            BuiltIn().should_be_true(MeetNowPage(self.driver).click_txt_sign_out(), 'Handle meeting controls failed')
            time.sleep(5)
            logger.info("Successfully signed out - sign out button detected")
            self.result_parallel_execute = "PASSED"
            return True
        
        except:
            self.result_parallel_execute = "FAILED"
            raise RuntimeError('Function exception: '+str(sys.exc_info()))
    
    def quit_browser(self):
        try:
            if hasattr(self, "driver") and self.driver:
                self.driver.quit()
                logger.info("Browser quit successfully")
        except Exception as e:
            logger.warning(f"Quit browser failed or browser already closed: {e}")
        finally:
            self.driver = None