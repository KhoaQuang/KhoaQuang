import sys
import os
import time
import logging
import datetime
import unittest
import inspect
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui

try:
    from robotbackgroundlogger import BackgroundLogger
except ImportError:
    class BackgroundLogger:
        def info(self, msg): logging.info(msg)
        def debug(self, msg): logging.debug(msg)
        def error(self, msg): logging.error(msg)

# Setup path
base_path = os.environ.get('PHOENIX_BASE_PATH', '')
if base_path:
    sys.path.append(os.path.join(base_path, 'MAIN/GUI/'))
    sys.path.append(os.path.join(base_path, 'MAIN/CLI/logger/1.0.0.478_0.crx'))

# Configure logging
def configure_log(level, name):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger

# Initialize loggers
logger_main = configure_log(logging.DEBUG, __name__)
logger = configure_log(logging.DEBUG, __name__)
logger_bg = BackgroundLogger()

def log_info(ip, port, func_name):
    """Log function entry with context information"""
    logger.info(f'Function: {func_name} | IP: {ip} | Port: {port}')


class Clients(unittest.TestCase):
    """Selenium WebDriver wrapper for Avaya Equinox testing"""
    
    def __init__(self, platform=None):
        super().__init__()
        self.driver = None
        self.point = None  # For threading
        
        if platform is None:
            platform = {}
        
        self.client_ip = platform.get("host") if isinstance(platform.get("host"), str) else None
        self.client_port = platform.get("port")
        self.client = platform.get("platform")
        self.udid = platform.get("udid")
        self.xcodeorgid = platform.get("xcodeorgid")
        self.profile = None
        self.screenshot_dir = platform.get('screenshot_dir')
        self.stop_point = 0
        self.main_window = "Avaya Workplace"
        self.subimage = platform.get('subimage')
        self.result_parallel_execute = None

    def get_desired_capabilities(self):
        """Get desired capabilities for different platforms"""
        desired_capabilities_list = {
            "win": {
                "debugConnectToRunningApp": False,
                "app": r"C:\Program Files (x86)\Avaya\Avaya IX Workplace\Avaya IX Workplace.exe"
            },
            "mac": {
                'platformName': 'mac',
                'deviceName': 'ThoPham',
                'browserName': 'Chrome',
                'commandDelay': 500,
                'loopDelay': 1000,
                'implicitTimeout': 3000,
                'mouseMoveSpeed': 50,
                "screenShotOnError": 1,
                "--url-base": "wd/hub"
            },
            "aea": {
                "udid": self.udid,
                "platformVersion": "9",
                "deviceName": "Samsung devices",
                "platformName": "Android",
                "noReset": False,
                "automationName": "UiAutomator2",
                "appPackage": "com.avaya.android.flare",
                "appActivity": "com.avaya.android.flare.MainActivity",
                "newCommandTimeout": "200000",
                "autoGrantPermissions": True,
                "systemPort": 8210,
                "--url-base": "wd/hub"
            },
            "aei": {
                "platformName": "iOS",
                "platformVersion": "10.1.1",
                "deviceName": "iPad",
                "xcodeOrgId": self.xcodeorgid,
                "xcodeSigningId": "iPhone Developer",
                "automationName": "XCUITest",
                "bundleId": "com.avaya.internal.Equinox",
                "udid": self.udid,
                "newCommandTimeout": "10000"
            }
        }
        return desired_capabilities_list.get(self.client, {})  

    def get_command_url(self):
        """Get command executor URL based on client type"""
        client_ip = self.client_ip or "127.0.0.1"
        client_port = self.client_port or "4444"
        
        command_urls = {
            "win": f'http://{client_ip}:{client_port}',
            "mac": f'http://{client_ip}:{client_port}',
            "aea": f'http://{client_ip}:{client_port}/wd/hub',
            "aei": f'http://{client_ip}:{client_port}/wd/hub'
        }
        return command_urls.get(self.client)
        
    def prepare_webdriver(self):
        """Initialize Chrome webdriver"""
        try:
            self.driver = webdriver.Chrome()
            logger.info('Chrome webdriver initialized')
            self.driver.maximize_window()
            logger.info('Browser window maximized')
            return True
        except Exception as e:
            logger.error(f'Failed to prepare webdriver: {e}')
            raise
    def launch_browser(self, url):
        """Launch browser and navigate to URL"""
        try:
            logger.info(f'Launching browser with URL: {url}')
            self.prepare_webdriver()
            self.driver.get(url)
            time.sleep(5)
            logger.info('Browser launched successfully')
            return True
        except Exception as e:
            logger.error(f'Failed to launch browser: {e}')
            raise
    def title_mywebsite(self):
        # title_web = "My Store"
        # expected_title = "Example Domain"
        expected_title = "What is a Java Backend Developer?"
        # self.driver.get(self.url)
        title_current = self.driver.title
        # if title_current == title_web: 
        #     time.sleep(3)
        #     print("Welcome to My Website: " + title_current)
        #     return True
        # else:
        #     assert('Goto %s failed,please check network'% self.url)
        #     print("Invalid")
        #     return False
        if title_current == expected_title:
            time.sleep(5)
            print("Titles match!")
            return True
        else:
            print("Don't match")
            return f"Expected title: {expected_title}, Actual title: {title_current}"
        
    def signin(self, username, password):
        """Sign in with username and password"""
        try:
            logger.info('Starting sign-in process')
            username_field = self.driver.find_element(By.CSS_SELECTOR, "input[id='loginForm:username']")
            username_field.clear()
            username_field.send_keys(username)
            logger.info('Username entered')
            time.sleep(2)
            
            password_field = self.driver.find_element(By.CSS_SELECTOR, "input[id='loginForm:password']")
            password_field.clear()
            password_field.send_keys(password)
            logger.info('Password entered')
            time.sleep(2)
            
            submit_btn = self.driver.find_element(By.CSS_SELECTOR, "span[id='loginForm:submitText']")
            submit_btn.click()
            logger.info('Sign-in submitted')
            time.sleep(5)
            return True
        except Exception as e:
            logger.error(f'Sign-in failed: {e}')
            raise

    def signout(self):
        """Sign out from application"""
        try:
            logger.info('Signing out')
            logout_btn = self.driver.find_element(By.ID, "logoutForm:log_out")
            logout_btn.click()
            logger.info('Sign-out completed')
            time.sleep(3)
            return True
        except Exception as e:
            logger.error(f'Sign-out failed: {e}')
            raise
        
    def get_download(self):
        """Click downloads element"""
        try:
            logger.info('Clicking downloads')
            downloads_element = self.driver.find_element(By.CSS_SELECTOR, "li[id='downloads']")
            downloads_element.click()
            logger.info('Downloads element clicked')
            time.sleep(2)
            return True
        except Exception as e:
            logger.error(f'Failed to click downloads: {e}')
            raise

    def perform_action(self):
        """Perform generic action"""
        logger.info('Performing action')

    def close_browser(self):
        """Close browser and cleanup"""
        try:
            logger.info('Closing browser')
            if self.driver:
                time.sleep(2)
                self.driver.quit()
                logger.info('Browser closed')
            return True
        except Exception as e:
            logger.error(f'Error closing browser: {e}')
            raise


    def launch_app(self):
        '''
            # Function name: launch_app
            # Description: This function is used to launch avaya equinox app
            # Parameters:  None
            # Author: Haonva
            # Date: 19 Jun, 2019
            # Ex: launch_app
            # Modify by: Hao Nguyen , update remote driver - handle abnormal case - add parallel execution
            # Date : Jan 8 2020
        '''
        try:
            log_info(self.client_ip, self.client_port, inspect.stack()[0][3])
            if self.point != None and self.point.is_alive():
                logger = logger_bg
                logger.info('Status is sub thread so log background will be write after back to main thread')
            else:
                logger = logger_main
            logger.info('Start function launch_app')
            desired_capabilities = self.get_desired_capabilities()
            logger.info('Desired_capabilities: %s'%(desired_capabilities))
            logger.info('Client_port: %s' %self.client_port)
            logger.info('Client: %s' %self.client)
            if self.client in ["mac", "aei", "aea"]:
                self.driver = webdriver.Remote(command_executor=self.get_command_url(), desired_capabilities=desired_capabilities)
            elif self.client in ["win"]:
                self.driver = webdriver.Remote(command_executor=self.get_command_url(), desired_capabilities=desired_capabilities)
            else:
                self.driver = webdriver.Remote(command_executor=self.get_command_url(), desired_capabilities=desired_capabilities)
                if Utility and InitPage and hasattr(Utility, 'wait_to_element_is_displayed'):
                    try:
                        if Utility.wait_to_element_is_displayed(self.driver, *InitPage().AUTO_CONFIG_INIT_SCREEN.get(self.client), 15):
                            Utility.click_element(self.driver, 1, *InitPage().AUTO_CONFIG_INIT_SCREEN.get(self.client))
                    except Exception as e:
                        logger.warning(f'Error in initial config: {e}')
            logger.info('Create a new driver session')
            if self.client in ["win", "mac"]:
                if self.client == "mac":
                    self.driver.get(self.main_window)
                logger.info('Verify launch_app desktop')
                logger.info(('Waiting to open equinox client on host: %s.') %(self.client_ip))
                current_window = self.driver.current_window_handle
                logger.info('current_window_handle: %s' %current_window)
                window_handles = self.driver.window_handles
                logger.info('window_handles: %s' %window_handles)
                if current_window != None and self.check_is_existed_ix_app():
                    logger.info(('Open window : %s') % (current_window))
                    self.result_parallel_execute = "PASSED"
                    return True
                else:
                    self.result_parallel_execute = "FAILED"
                    self.fail("AVAYA IX WORKPLACE is opened unsuccessfully")
            else:
                logger.info('Verify launch_app mobile')
                if self.client == "aei" and AlertPage and Utility:
                    try:
                        if Utility.wait_for_exists_not_except(self.driver, 5, *(AlertPage().ACCEPT_BTN.get(self.client))):
                            Utility.click_element(self.driver, 3, *(AlertPage().ACCEPT_BTN.get(self.client)))
                            logger.info('clicked ACCEPT button')
                    except Exception as e:
                        logger.warning(f'Error handling iOS alert: {e}')
                self.result_parallel_execute = "PASSED"
                return True
        except Exception as e:
            self.result_parallel_execute = "FAILED"
            logger.error(f'launch_app failed: {e}')
            raise RuntimeError(f'Function exception: {str(e)}')