from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys



# 0. All users sign in 
# 1. User A click Start my meeting to start conference
# 2. all users join meeting
# 3. All users block/unblock video
# 4. User A share full screen
# 5. User B leave and re-join meeting 
# 6. All paticipants chat public and privite
# 7. Moderator teminate meeting

class WORKPLACE():
    def __init__(self):
        print("Create a object")
    def get_desired_capabilities(self,client):
        desired_capabilities_win = {
            "debugConnectToRuningApp": 'false',
            "app": r"C:/Program Files (x86)/Avaya/Avaya IX Workplace/Avaya IX Workplace.exe"
        }
        desired_capabilities_mac = {
            'platformName':'mac',  
            'commandDelay':500, 
            'loopDelay':1000, 
            'implicitTimeout':3000, 
            'mouseMoveSpeed':50, 
            "screenShotOnError":1,
            "--url-base":"wd/hub"
        }
        desired_capabilities_aea = {
			"udid": "215d1b04630d7ece",
            "platformVersion": "9",
			"deviceName":"Samsung devices",
			"platformName":"Android",
            "noReset":False,
            "automationName":"UiAutomator2",
			"appPackage": "com.avaya.android.flare",
			"appActivity":"com.avaya.android.flare.MainActivity",
            "newCommandTimeout":"200000",
			"autoGrantPermissions":True,
            "systemPort":8220,
            "--url-base":"wd/hub"
	    }
        # desired_capabilities_aei = {
        #     #"browserName": "Chrome",
		# 	"platformName": "iOS",
        #     "platformVersion": "12.2",
        #     "deviceName": "iPad",
        #     "xcodeOrgId": "65HX78R444",
        #     "notReset": True,
        #     "xcodeSigningId": "iPhone Developer",
        #     "automationName": "XCUITest",
        #     "bundleId": "com.avaya.internal.Equinox",
        #     "udid": "e344155913ca64b64e0f3963c1f89817b1eae496",
        #     "newCommandTimeout": "240"
	    # }
        desired_capabilities_list = {
            "win": desired_capabilities_win,
            "mac": desired_capabilities_mac,
            "aea": desired_capabilities_aea,
            # "aei": desired_capabilities_aei,
        }
        return desired_capabilities_list.get(client)
    def launch_app(self,ip,client):
        if client == 'win':
            print('Start launch_app'+ client)
            print('Webdriver is ready')
            desired_capabilities = self.get_desired_capabilities(client)
            self.driver = webdriver.Remote(command_executor='http://'+ ip +':9999',desired_capabilities=desired_capabilities )
            print("End Launch app for "+ client)
            time.sleep(3)
        elif client == 'mac':
            print('Start function launch_app'+ client)
            desired_capabilities = self.get_desired_capabilities(client)
            self.driver = webdriver.Remote(command_executor='http://'+ip+':4622',desired_capabilities=desired_capabilities)
            self.driver.get("Avaya Workplace")
            print("End Launch app for "+ client)
        elif client in 'aea aei':
            print("Start Launch App for "+ client)
            desired_capabilities = self.get_desired_capabilities(client)
            self.driver = webdriver.Remote(command_executor='http://'+ip+':4723/wd/hub', desired_capabilities=desired_capabilities)
            print("End Launch app for "+ client)
        else:
            print("Invalid!!!!!")
            return False

    def sign_in(self,client,url,username,password,webaddress,nameuser,passwd): 
        if client == 'win':
            print("Pull configure my meeting cho WIN")
            configure_account = self.driver.find_element(By.NAME,"Configure my account")
            configure_account.click()
            print("options and my setting")
            options_setting = self.driver.find_element(By.NAME,"Options and Settings")
            options_setting.click()
            print("Click web address")
            web_address = self.driver.find_element(By.NAME,"Use web address")
            web_address.click()
            print("Input URL")
            url_address = self.driver.find_element(By.NAME,"URL")
            url_address.send_keys(url)
            print("Button Next")
            next_button = self.driver.find_element(By.NAME,"NEXT")
            next_button.click()
            time.sleep(5)
            print("Begin Input Username")
            user_name = self.driver.find_element(By.NAME,'Username')
            user_name.send_keys(username)
            print("Begin Input PASS")
            word_pass = self.driver.find_element(By.ID,"PasswordBox")
            time.sleep(2)
            word_pass.send_keys(password)
            time.sleep(5)
            print("Click Next")
            nexttt_button = self.driver.find_element(By.NAME,"NEXT")
            nexttt_button.click()
            time.sleep(8)
        elif client == 'mac':
            print("Pull configure my meeting MAC")
            configure = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXButton[@AXTitle='Configure my account']")
            meeting_configure = ActionChains(self.driver)
            meeting_configure.move_to_element(configure)
            meeting_configure.click()
            meeting_configure.perform()
            meeting_configure.release()
            meeting_configure.reset_actions()
            print("Choose setting")
            choose_setting = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXButton[@AXIdentifier='UCC3AutomationLoginSettingsButtonIdentifier']")
            setting_choose = ActionChains(self.driver)
            setting_choose.move_to_element(choose_setting)
            setting_choose.click()
            setting_choose.perform()
            setting_choose.release()
            setting_choose.reset_actions()
            print("Button user web address")
            user_web_address = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXSubrole='AXUnknown']/AXButton[@AXTitle='Use a web address' and @AXIdentifier='UCC3AutomationLoginAutomaticConfigurationButtonIdentifier']") 
            web_address_user = ActionChains(self.driver)
            web_address_user.move_to_element(user_web_address)
            web_address_user.click()
            web_address_user.perform()
            web_address_user.release()
            web_address_user.reset_actions()
            print("Input web address")
            web_address = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXStaticText[@AXValue='WEB ADDRESS' and @AXIdentifier='UCC3AutomationLoginLabelIdentifier']")
            address_web = ActionChains(self.driver)
            address_web.move_to_element(web_address)
            address_web.click()
            address_web.send_keys(webaddress)
            address_web.perform()
            address_web.release()
            address_web.reset_actions()
            print("Button next")
            nextt_button = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXButton[@AXTitle='NEXT' and @AXIdentifier='UCC3AutomationLoginNextButtonIdentifier']")            
            button_nextt = ActionChains(self.driver)
            button_nextt.move_to_element(nextt_button)
            button_nextt.click()
            button_nextt.perform()
            button_nextt.release()
            button_nextt.reset_actions()
            time.sleep(3)
            print("Input user name")
            user_name = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXStaticText[@AXValue='USERNAME' and @AXIdentifier='UCC3AutomationLoginLabelIdentifier']")
            name_user = ActionChains(self.driver)
            name_user.move_to_element(user_name)
            name_user.click()
            name_user.send_keys(nameuser)
            name_user.perform()
            name_user.release()
            name_user.reset_actions()
            print("Input password")
            pass_word = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXStaticText[@AXValue='PASSWORD' and @AXIdentifier='UCC3AutomationLoginLabelIdentifier']")
            word_pass = ActionChains(self.driver)
            word_pass.move_to_element(pass_word)
            word_pass.click()
            word_pass.send_keys(passwd)
            word_pass.perform()
            word_pass.release()
            word_pass.reset_actions()
            time.sleep(5)
            print("Button next")
            next_button = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXButton[@AXTitle='NEXT' and @AXIdentifier='UCC3AutomationLoginNextButtonIdentifier']")
            button_next = ActionChains(self.driver)
            button_next.move_to_element(next_button)
            button_next.click()
            button_next.perform()
            button_next.release()
            button_next.reset_actions()
            time.sleep(15)
            print("Button skip")
            skip_button = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='Window' and @AXIdentifier='_NS:6' and @AXSubrole='AXStandardWindow']/AXButton[@AXTitle='SKIP TUTORIAL' and @AXIdentifier='UCC3AutomationTutorialSkipButtonIdentifier']")
            button_skip = ActionChains(self.driver)
            button_skip.move_to_element(skip_button)
            button_skip.click()
            button_skip.perform()
            button_skip.release()
            button_skip.reset_actions()
            time.sleep(8)
        elif client == 'aea':
            # print("Pull Configure my account cho android")
            # configure_account = self.driver.find_element(By.ID,"com.avaya.android.flare:id/configure_account")
            # configure_account.click()
            print("options and my setting")
            options_mysetting = self.driver.find_element(By.ID,"com.avaya.android.flare:id/settings_icon")
            options_mysetting.click()
            print("Click use web address")
            web_address = self.driver.find_element(By.ID,"com.avaya.android.flare:id/popoverButton1")
            web_address.click()
            print("Input URL")
            url_address = self.driver.find_element(By.ID,"com.avaya.android.flare:id/auto_config_address")
            url_address.send_keys(url)
            time.sleep(10)
            print("Button Next")
            next_button = self.driver.find_element(By.ID,"com.avaya.android.flare:id/connect_button")
            next_button.click()
            time.sleep(10)
            print("Begin Input Username")
            user_name = self.driver.find_element(By.ID,"com.avaya.android.flare:id/service_username")
            user_name.send_keys(username)
            print("Begin Input PASS")
            word_pass = self.driver.find_element(By.ID,"com.avaya.android.flare:id/service_password")
            word_pass.send_keys(password)
            print("Button sign in")
            sign_in = self.driver.find_element(By.ID,"com.avaya.android.flare:id/connect_button")
            sign_in.click()
            time.sleep(8)
            # print("Start meeting")
            # start_meeting = self.driver.find_element(By.ID,"com.avaya.android.flare:id/my_meeting_id")
            # start_meeting.click()
            # time.sleep(3)
            # print("Join")
            # join_button = self.driver.find_element(By.ID,"com.avaya.android.flare:id/join_meeting")
            # join_button.click()
            # time.sleep(8)

    def start_my_meeting(self): 
        print("Choose room 322006000")
        choose_room = self.driver.find_element(By.NAME,"322006000")
        choose_room.click()
        print("Begin join")
        join_button = self.driver.find_element(By.NAME,"Join")
        join_button.click()
        time.sleep(5)
    def join_meeting(self,client,name,meetingid):  
        if client == 'mac':
            print("Click avaya workplace")
            avaya_click = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='Avaya Workplace' and @AXIdentifier='UCC3MainWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXSplitGroup[0]/AXStaticText[@AXValue='Avaya Workplace']")
            click_avaya = ActionChains(self.driver)
            click_avaya.move_to_element(avaya_click)
            click_avaya.click()
            click_avaya.release()
            click_avaya.reset_actions()
            ActionChains(self.driver).move_to_element_with_offset(avaya_click,9,0).double_click().perform()
            time.sleep(5)
            print("Choose join workplace meeting")
            join_meeting_wplace = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='Avaya Workplace' and @AXIdentifier='UCC3MainWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXSplitGroup[0]/AXScrollArea[0]/AXTable[0]/AXRow[@AXSubrole='AXTableRow']/AXCell[0]/AXLayoutArea[@AXIdentifier='_NS:9']/AXButton[0]")
            join_wplace = ActionChains(self.driver)
            join_wplace.move_to_element(join_meeting_wplace)
            join_wplace.click()
            join_wplace.perform()
            join_wplace.release()
            join_wplace.reset_actions()
            print("Join meeting workplace successfully!!!")
            print("Begin input meeting ID")
            id_meeting = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXStaticText[@AXValue='Meeting ID']")
            meeting_id = ActionChains(self.driver)
            meeting_id.move_to_element(id_meeting)
            meeting_id.click()
            meeting_id.send_keys(meetingid)
            meeting_id.perform()
            meeting_id.release()
            meeting_id.reset_actions()
            print("Input meeting ID successfully!!!")
            time.sleep(8)
            print("Begin button join")
            join = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXButton[@AXTitle='Join']")
            join_1 = ActionChains(self.driver)
            join_1.move_to_element(join)
            join_1.click()
            join_1.perform()
            join_1.release()
            join_1.reset_actions()
            print("Join successfully!!!")      
            time.sleep(15)   
        elif client == 'aea':
            print("Choose join workplace meeting")
            join_meeting_wplace = self.driver.find_element(By.ID,"com.avaya.android.flare:id/join_other_meeting_layout")
            join_meeting_wplace.click()
            time.sleep(10)
            print("Input your name")
            your_name = self.driver.find_element(By.ID,"com.avaya.android.flare:id/name")
            your_name.click()
            your_name.clear()
            your_name.send_keys(name)
            print("Input meeting id")
            id_meeting = self.driver.find_element(By.ID,"com.avaya.android.flare:id/meeting_id")
            id_meeting.click()
            id_meeting.clear()
            id_meeting.send_keys(meetingid)
            time.sleep(10)
            print("Begin button join")
            join_meeting_wplace = self.driver.find_element(By.ID,"com.avaya.android.flare:id/join_meeting")
            join_meeting_wplace.click()
        else:
            print("Invalid!!!!!")
            return False
    def users_block_unblock_video(self,client):
        if client == 'win':
            print("Block camera for win")
            block_camera = self.driver.find_element(By.NAME,"Block camera")
            block_camera.click()
            print("UnBlock camera for win")
            unblock_camera = self.driver.find_element(By.NAME,"Unblock camera")
            unblock_camera.click()
        # print("Click user for mac")
        # click_user_mac = self.driver.find_element(By.ID,"ConferenceItem(Moderator_auto2006001 Scopia)")
        # click_user_mac.click()
            time.sleep(5)
        # print("Click button...")
        # options_more = self.driver.find_element(By.NAME,"More options...")
        # options_more.click()
        # print("Block video for mac")
        # video_block = self.driver.find_element(By.NAME,"Block video")
        # video_block.click()
        # print("UnBlock video for mac")
        # video_unblock = self.driver.find_element(By.NAME,"Block video")
        # video_unblock.click()
        # time.sleep(5)
        # print("Click user for android")
        # click_user_aea = self.driver.find_element(By.NAME,"auto2006002 Scopia")
        # click_user_aea.click()
        # time.sleep(3)
        # print("Click button...")
        # options_more = self.driver.find_element(By.NAME,"More options...")
        # options_more.click()
        # print("Block video for android")
        # video_block = self.driver.find_element(By.NAME,"Block video")
        # video_block.click()
        # print("UnBlock video for android")
        # video_unblock = self.driver.find_element(By.NAME,"Block video")
        # video_unblock.click()
        elif client == 'mac':
            print("Block video for mac")
            block_camera = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='10:15  322006000' and @AXIdentifier='UCC3ConferenceWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXCheckBox[@AXIdentifier='UCC3AutomationConferenceRosterDisableVideoButtonIdentifier' and @AXSubrole='AXToggle']")
            video_block = ActionChains(self.driver)
            video_block.move_to_element(block_camera)
            video_block.click()
            video_block.perform()
            video_block.release()
            video_block.reset_actions()
            print("UnBlock video for mac")
            unblock_video = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='13:55  322006000' and @AXIdentifier='UCC3ConferenceWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXCheckBox[@AXIdentifier='UCC3AutomationConferenceRosterDisableVideoButtonIdentifier' and @AXSubrole='AXToggle']")
            video_ublock = ActionChains(self.driver)
            video_ublock.move_to_element(unblock_video)
            video_ublock.click()
            video_ublock.perform()
            video_ublock.release()
            video_ublock.reset_actions()
        elif client == 'aea':
            time.sleep(5)
            selec_video = self.driver.find_element(By.ID,"com.avaya.android.flare:id/midcall_video")
            selec_video.click()
            print("Unblock video for android")
            time.sleep(15)
            video_block = self.driver.find_element(By.XPATH,"//android.widget.ImageButton[@content-desc='Unblock Video']")
            video_block.click()
            print("Block video for android")
            time.sleep(20)
            video_unblock = self.driver.find_element(By.XPATH,"//android.widget.ImageButton[@content-desc='Block Video']")
            time.sleep(5)
            video_unblock.click()
            print("Block successfully")
            # click_main = self.driver.find_element(By.ID,"com.avaya.android.flare:id/advanced_controls_container")
            # click_main.click()
    def win_share_screen(self):
        print("Begin share screen")
        share_screen= self.driver.find_element(By.NAME,"Start Sharing")
        share_screen.click()
        display = self.driver.find_element(By.NAME,"Display 1 (Primary)")
        display.click()
        time.sleep(5)
    def mac_leave_rejoin(self):
        print("Button end")
        time.sleep(5)
        call_end = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3ConferenceWindowIdentifier']/AXCheckBox[@AXIdentifier='UCC3AutomationConferenceRosterLeaveConferenceButtonIdentifier']")
        end_call = ActionChains(self.driver)
        end_call.move_to_element(call_end)
        end_call.click()
        end_call.perform()
        end_call.release()
        end_call.reset_actions()
        print("Call Ended")
        time.sleep(8)
        print("Begin button join")
        join = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXButton[@AXTitle='Join']")
        join_1 = ActionChains(self.driver)
        join_1.move_to_element(join)
        join_1.click()
        join_1.perform()
        join_1.release()
        join_1.reset_actions()
        print("Join successfully!!!") 
        time.sleep(5)    
    def all_participants_chat(self,chat,client):
        if client == 'win':
            print("Input chat from win")
            chat_win = self.driver.find_element(By.ID,"MessageTextBox")
            chat_win.send_keys(chat)
            chat_win.submit()
            print("Send successfully")
            time.sleep(3)
        elif client == 'mac':
            print("Input chat from mac")
            chat_mac = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='41:00  322006000' and @AXIdentifier='UCC3ConferenceWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXScrollArea[1]/AXTextArea[@AXIdentifier='UCC3AutomationConferenceRosterChatInputTextViewIdentifier']")
            mac_chat = ActionChains(self.driver)
            mac_chat.move_to_element(chat_mac)
            mac_chat.click()
            mac_chat.send_keys(chat)
            # mac_chat.send_keys(Keys.ENTER)
            mac_chat.perform()
            mac_chat.release()
            mac_chat.reset_actions()
            chat_mac1 = ActionChains(self.driver)
            chat_mac1.move_to_element(chat_mac)
            chat_mac1.submit()
            chat_mac1.perform()
            chat_mac1.release()
            chat_mac1.reset_actions()
            print("Send successfully")
            time.sleep(3)
        elif client == 'aea':
            print("Input chat from android")
            chat_aea = self.driver.find_element(By.ID,"com.avaya.android.flare:id/activecall_conf_chat_button")
            chat_aea.click()
            input_chat = self.driver.find_element(By.ID,"com.avaya.android.flare:id/message_input_area")
            input_chat.click()
            input_chat.send_keys(chat)
            time.sleep(3)
            print("Send successfully")
            send_chat = self.driver.find_element(By.ID,"com.avaya.android.flare:id/messaging_message_send_button")
            send_chat.click()
            time.sleep(3)
            hide = self.driver.find_element(By.ID,"com.avaya.android.flare:id/hide")
            hide.click()
            time.sleep(3)
            
    def terminate_meeting(self,client):
        # if client == 'win':
        # conference = self.driver.find_element(By.NAME,"Sharing frame window edge")
        # conference.click()
        time.sleep(5)
        print("Click icon user")
        time.sleep(8)
        conference_menu = self.driver.find_element(By.NAME,"Conference Menu")
        conference_menu.click()
        print("Choose meeting control")
        time.sleep(15) 
        control_meeting = self.driver.find_element(By.NAME,"Meeting Controls")
        control_meeting.click()
        print("End Meeting")
        time.sleep(5)
        end_meeting = self.driver.find_element(By.NAME,"End Meeting")
        end_meeting.click()
        time.sleep(5)
        print("Button End")
        END = self.driver.find_element(By.NAME,"End")
        END.click()
        time.sleep(5)
        # elif client == 'mac':
        #     print("Begin button join meeting")
        #     meeting_join = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier']/AXButton[@AXTitle='Join a meeting']")
        #     join_meeting = ActionChains(self.driver)
        #     join_meeting.move_to_element(meeting_join)
        #     join_meeting.click()
        #     join_meeting.perform()
        #     join_meeting.release()
        #     join_meeting.reset_actions()
        #     time.sleep(15)
        #     print("Begin input your name")
        #     your_name = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXStaticText[@AXValue='Your name']")
        #     name_your = ActionChains(self.driver)
        #     name_your.move_to_element(your_name)
        #     name_your.click()
        #     name_your.send_keys(name)
        #     name_your.perform()
        #     name_your.release()
        #     name_your.reset_actions()
        #     print("Input your name successfully!!!")
        #     time.sleep(2)
        #     print("Begin input meeting address")
        #     meeting_address = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXStaticText[@AXValue='Meeting Address']") 
        #     address_meeting = ActionChains(self.driver)
        #     address_meeting.move_to_element(meeting_address)
        #     address_meeting.click()
        #     address_meeting.send_keys(address)
        #     address_meeting.perform()
        #     address_meeting.release()
        #     address_meeting.reset_actions()
        #     print("Input meeting address successfully!!!")
        #     time.sleep(2)
        #     print("Begin input meeting ID")
        #     id_meeting = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXStaticText[@AXValue='Meeting ID']")
        #     meeting_id = ActionChains(self.driver)
        #     meeting_id.move_to_element(id_meeting)
        #     meeting_id.click()
        #     meeting_id.send_keys(meetingid)
        #     meeting_id.perform()
        #     meeting_id.release()
        #     meeting_id.reset_actions()
        #     time.sleep(8)
        #     print("Input meeting ID successfully!!!")
        #     time.sleep(2)
        #     avaya_click = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='Avaya Workplace' and @AXIdentifier='UCC3MainWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXSplitGroup[0]/AXStaticText[@AXValue='Avaya Workplace']")
        #     click_avaya = ActionChains(self.driver)
        #     click_avaya.move_to_element(avaya_click)
        #     click_avaya.click()
        #     click_avaya.release()
        #     click_avaya.reset_actions()
        #     time.sleep(2)
        #     ActionChains(self.driver).move_to_element_with_offset(avaya_click,9,0).double_click().perform()
        #     print("Begin button join")
        #     join = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXButton[@AXTitle='Join']")
        #     join_1 = ActionChains(self.driver)
        #     join_1.move_to_element(join)
        #     join_1.click()
        #     join_1.perform()
        #     join_1.release()
        #     join_1.reset_actions()
        #     print("Join successfully!!!") 
        # elif client == 'aea':
        #     print("Choose ---")
        #     choose_select = self.driver.find_element(By.ID,"com.avaya.android.flare:id/show_advanced_controls")
        #     choose_select.click()
        #     print("Select")
        #     cham_gach = self.driver.find_element(By.ID,"com.avaya.android.flare:id/activecall_advctrl_confctrl")
        #     cham_gach.click()
        #     time.sleep(8)
        #     print("End meeting")
        #     end_meeting = self.driver.find_element(By.XPATH,"//android.widget.LinearLayout[@content-desc='END MEETING']/android.widget.LinearLayout")
        #     end_meeting.click()
        #     time.sleep(5)
        #     print("Click OK") 
        #     time.sleep(5)
        #     ok_1 = self.driver.find_element(By.ID,"com.avaya.android.flare:id/dialog_ok_button")
        #     ok_1.click()
        #     time.sleep(8)
        #     print("Continue click OK")
        #     ok_2 = self.driver.find_element(By.ID,"com.avaya.android.flare:id/confirmation_dialog_button")
        #     ok_2.click()
        #     time.sleep(5) 
    def verify_signin(self,client):
        if client == 'win':
            print("Select user")
            select_user = self.driver.find_element(By.NAME,"Open User Dashboard")
            select_user.click()
            time.sleep(5)
            expected = 'auto2006000 '
            verify_name = self.driver.find_element(By.NAME,"auto2006000 ")
            print("Get name")
            actual_username = verify_name.get_attribute("Name")
            time.sleep(10)
            print("User Name: "+actual_username)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!Win sign in successfully")
                return True
            else: 
                print("Failed!!!")
                return False
            time.sleep(5)
        # elif client == 'mac':
        #     select_user = self.driver.find_element(By.XPATH,"")
        #     select_user.click()
        #     expected = 'auto2006001'
        #     verify_name = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3ConferenceWindowIdentifier']/AXScrollArea[0]/AXTable[@AXIdentifier='UCC3AutomationConferenceRosterParticipantTableIdentifier']/AXRow[@AXSubrole='AXTableRow']/AXCell[0]/AXStaticText[@AXValue='auto2006001']")
        #     actual_username = verify_name.get_attribute("AXValue")
        #     time.sleep(5)
        #     if expected in actual_username:
        #         print("Pass!>>>Username is exactly!!!Sign in successfully")
        #         print(actual_username)
        #         return True
        #     else: 
        #         print("Failed!!!")
        #         return False
        elif client == 'aea':
            print("Select user aea")
            select_user = self.driver.find_element(By.ID,"com.avaya.android.flare:id/profile_avatar")
            select_user.click()
            time.sleep(7)
            print("Open user area")
            expected = 'auto2006002'
            verify_name = self.driver.find_element(By.ID,"com.avaya.android.flare:id/tvName")
            print("GEt user Name")
            actual_username = verify_name.get_attribute("text")
            print("User Name: "+actual_username)
            time.sleep(10)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!Android Sign in successfully")
                
            else: 
                print("Failed!!!")
                return False
            time.sleep(5)
            #back_user = self.driver.find_element(By.XPATH,"//android.widget.ImageButton[@content-desc='Di chuyển lên']")
            print("Back to home")
            back_user = self.driver.find_element(By.XPATH,"//android.view.ViewGroup[@resource-id='com.avaya.android.flare:id/toolbar_local_user']/android.widget.ImageButton")
            
            back_user.click()
            time.sleep(3)
            print("clicked back")
    def verify_startmeeting(self):
        expected = "322006000"
        verify_name = self.driver.find_element(By.NAME,"322006000")
        print("Get name")
        actual_username = verify_name.get_attribute("Name")
        print("User name: "+actual_username)
        time.sleep(10)
        if expected in actual_username:
            print("Pass!>>>Username is exactly!!!Win Start meeting successfully")
            return True
        else: 
            print("Failed!!!")
            return False
        time.sleep(5)
    def verify_joinmeeting(self,client):
        if client == 'mac':
            expected = 'auto2006001 Scopia (Me)'
            verify_name = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3ConferenceWindowIdentifier']/AXScrollArea[0]/AXTable[@AXIdentifier='UCC3AutomationConferenceRosterParticipantTableIdentifier']/AXRow[@AXSubrole='AXTableRow']/AXCell[0]/AXStaticText[@AXValue='auto2006001 Scopia (Me)']")            
            print("Get user name mac")
            actual_username = verify_name.get_attribute("AXValue")
            print("User name: "+actual_username)
            time.sleep(5)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!Mac join meeting successfully")
                print(actual_username)
                return True
            else: 
                print("Failed!!!")
                return False
        elif client == 'aea':
            print("Button Participants")
            time.sleep(10)
            Participants = self.driver.find_element(By.ID,"com.avaya.android.flare:id/activecall_conf_roster_button")
            Participants.click()
            time.sleep(10)
            expected = 'auto2006002 Scopia'
            select_user = self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow/android.widget.TextView")
            select_user.click()
            verify_name = self.driver.find_element(By.ID,"com.avaya.android.flare:id/dialog_title")
            print("Get user name aea")
            actual_username = verify_name.get_attribute("text")
            print("User name: "+ actual_username)
            time.sleep(10)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!Andoird join meeting successfully")
            else: 
                print("Failed!!!")
                return False
            main_aea = self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
            main_aea.click()
            time.sleep(10)
            print("Hide")
            hide = self.driver.find_element(By.ID,"com.avaya.android.flare:id/hide")
            print("Back to home")
            hide.click()
            time.sleep(3)
    def verify_video(self,client):
        if client == 'win':
            print("Block camera for win")
            expected = 'Block camera'
            verify_name = self.driver.find_element(By.NAME,"Block camera")        
            actual_username = verify_name.get_attribute("Name")
            print("User name: "+actual_username)
            time.sleep(10)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!Block camera for win successfully")
            else: 
                print("Failed!!!")
                return False
            time.sleep(5)
            print("UnBlock camera for win")
            expected = 'Unblock camera'
            verify_name = self.driver.find_element(By.NAME,"Unblock camera")
            actual_username = verify_name.get_attribute("Name")
            print("User name: "+actual_username)
            time.sleep(10)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!Block camera for win successfully")
            else: 
                print("Failed!!!")
                return False
        # elif client == 'mac':
        #     print("Block video for mac")
        #     video_block = self.driver.find_element(By.NAME,"Block video")
        #     video_block.click()
        #     print("UnBlock video for mac")
        #     video_unblock = self.driver.find_element(By.NAME,"Block video")
        #     video_unblock.click()
        elif client == 'aea':
            time.sleep(8)
            print("UnBlock video for android")
            verify_name = self.driver.find_element(By.XPATH,"//android.widget.ImageButton[@content-desc='Unblock Video']")            
            verify_name.click()
            time.sleep(8)
            expected = "Block Video"
            actual_username = verify_name.get_attribute("content-desc")
            print("User name: "+actual_username)
            time.sleep(10)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!Block camera for android successfully")
            else: 
                print("Failed!!!")
                return False
            print("Block video for android")
            time.sleep(5)
            expected = "Unblock Video"
            verify_name = self.driver.find_element(By.XPATH,"//android.widget.ImageButton[@content-desc='Block Video']")            
            verify_name.click()
            time.sleep(8)
            actual_username = verify_name.get_attribute("content-desc")
            print("User name: "+actual_username)
            time.sleep(10)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!UnBlock camera for android successfully")
            else: 
                print("Failed!!!")
                return False
            time.sleep(5)
            click_main = self.driver.find_element(By.XPATH,"//android.widget.ImageButton[@content-desc='self view']")
            click_main.click()
    def verify_rejoin(self):
        time.sleep(5)
        expected = 'auto2006001 Scopia (Me)'
        verify_name = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3ConferenceWindowIdentifier']/AXScrollArea[0]/AXTable[@AXIdentifier='UCC3AutomationConferenceRosterParticipantTableIdentifier']/AXRow[@AXSubrole='AXTableRow']/AXCell[0]/AXStaticText[@AXValue='auto2006001 Scopia (Me)']")
        print("Get User name: ")
        actual_username = verify_name.get_attribute("AXValue")
        print("User name: "+actual_username)
        time.sleep(5)
        if expected in actual_username:
            print("Pass!>>>Username is exactly!!!Rejoin successfully")
            
            return True
        else: 
            print("Failed!!!")
            return False
    def verify_participant_chat(self,client):
        if client == 'win':
            time.sleep(8)
            messages =  self.driver.find_elements(By.XPATH,"//*[contains(@Name,'Avaya.UCC.ViewModels.Conference.Chat.ChatMessageViewModel')]/child::*/following-sibling::*[2]")
            print("Number messages in message box: "+len(messages))
            latest_message = messages[len(messages)-1]
            actual_message = latest_message.text

            
            choose_win = self.driver.find_element(By.NAME,"Avaya.UCC.ViewModels.Conference.Chat.ChatMessageViewModel")
            choose_win.click()
            expected = "Hello"
            verify_name = self.driver.find_element(By.NAME,"Hello")
            print("Get User name: ")
            time.sleep(5)
            actual_username = verify_name.get_attribute("Name")
            print("User name: "+actual_username)
            time.sleep(10)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!Chat meeting successfully")
                return True
            else: 
                print("Failed!!!")
                return False
        # elif client == 'mac':
            
        elif client == 'aea':
            expected = "Welcome"
            verify_name = self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView")
            time.sleep(8)
            print("Get User name: ")
            actual_username = verify_name.get_attribute("Name")
            print("User name: "+actual_username)
            time.sleep(10)
            if expected in actual_username:
                print("Pass!>>>Username is exactly!!!Chat meeting successfully")
                return True
            else: 
                print("Failed!!!")
                return 
    # def verify_end(self):
        

win = WORKPLACE()
mac = WORKPLACE()
android = WORKPLACE()
win.launch_app(client='win',ip='10.102.1.24')
# mac.launch_app(client='mac',ip='10.102.1.104')
# android.launch_app(client='aea',ip='10.102.1.30')
win.sign_in(client='win',url="http://10.102.2.58/hfs/auto_conf_iview126.txt",username="auto2006000",password="RAPtor1234",webaddress=None,nameuser=None,passwd=None)
# win.verify_signin(client='win')
# mac.sign_in(client='mac',webaddress="http://10.102.2.58/hfs/auto_conf_iview126.txt",nameuser="auto2006001",passwd="RAPtor1234",url=None,username=None,password=None)
# mac.verify_signin(client='mac')
# android.sign_in(client='aea',url="http://10.102.2.58/hfs/auto_conf_iview126.txt",username="auto2006002",password="RAPtor1234",webaddress=None,nameuser=None,passwd=None)
# android.verify_signin(client='aea')
win.start_my_meeting()
# win.verify_startmeeting()
# mac.join_meeting(client='mac',meetingid="322006000",name=None)
# mac.verify_joinmeeting(client='mac')
# android.join_meeting(client='aea',name="Khoa",meetingid="322006000")
# android.verify_joinmeeting(client='aea')
# win.users_block_unblock_video(client='win')
# win.verify_video(client='win')
# mac.users_block_unblock_video(client='mac')
# android.users_block_unblock_video(client='aea')
# android.verify_video(client='aea')
# win.win_share_screen()
# mac.mac_leave_rejoin()
# mac.verify_rejoin()
win.all_participants_chat(client='win',chat='Hello')
win.verify_participant_chat(client='win')
# mac.all_participants_chat(client='mac',chat='Hi')
# # # mac.verify_participant_chat(client='mac')
# android.all_participants_chat(client='aea',chat='Welcome')
# android.verify_participant_chat(client='aea')
# win.terminate_meeting(client='win')
# win.
# mac.terminate_meeting(client='mac')
# android.terminate_meeting(client='aea')

            
    











