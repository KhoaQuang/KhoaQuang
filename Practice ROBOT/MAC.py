from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

#http://10.102.2.58/hfs/auto_conf_iview126.txt
#auto2006000/RAPtor1234
#auto2006001/RAPtor1234
#ActionChains(self.driver).move_to_element(configbtn).click().perform()
#ActionChains(self.driver).move_to_element(http).send_keys('http').perform()

class MAC():
    def __init__(self):
        print("Create a object winium")
    def get_desired_capabilities(self):
        desired_capabilities_mac = {
            'platformName':'mac',  
            'commandDelay':500, 
            'loopDelay':1000, 
            'implicitTimeout':3000, 
            'mouseMoveSpeed':50, 
            "screenShotOnError":1,
            "--url-base":"wd/hub"
        }
        desired_capabilities_list= {
            "mac": desired_capabilities_mac,
        }
        return desired_capabilities_list.get("mac")
    def launch_app(self):
        print('Start function launch_app')
        desired_capabilities = self.get_desired_capabilities()
        self.driver = webdriver.Remote(command_executor='http://10.102.1.104:4622', desired_capabilities=desired_capabilities)
        self.driver.get("Avaya Workplace")

    def Workplace(self,name,address,meetingid):
        print("Begin button join meeting")
        meeting_join = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier']/AXButton[@AXTitle='Join a meeting']")
        join_meeting = ActionChains(self.driver)
        join_meeting.move_to_element(meeting_join)
        join_meeting.click()
        join_meeting.perform()
        join_meeting.release()
        join_meeting.reset_actions()
        time.sleep(15)
        print("Begin input your name")
        your_name = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXStaticText[@AXValue='Your name']")
        name_your = ActionChains(self.driver)
        name_your.move_to_element(your_name)
        name_your.click()
        name_your.send_keys(name)
        name_your.perform()
        name_your.release()
        name_your.reset_actions()
        print("Input your name successfully!!!")
        time.sleep(2)
        print("Begin input meeting address")
        meeting_address = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXStaticText[@AXValue='Meeting Address']") 
        address_meeting = ActionChains(self.driver)
        address_meeting.move_to_element(meeting_address)
        address_meeting.click()
        address_meeting.send_keys(address)
        address_meeting.perform()
        address_meeting.release()
        address_meeting.reset_actions()
        print("Input meeting address successfully!!!")
        time.sleep(2)
        print("Begin input meeting ID")
        id_meeting = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXStaticText[@AXValue='Meeting ID']")
        meeting_id = ActionChains(self.driver)
        meeting_id.move_to_element(id_meeting)
        meeting_id.click()
        meeting_id.send_keys(meetingid)
        meeting_id.perform()
        meeting_id.release()
        meeting_id.reset_actions()
        time.sleep(8)
        print("Input meeting ID successfully!!!")
        time.sleep(2)
        avaya_click = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='Avaya Workplace' and @AXIdentifier='UCC3MainWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXSplitGroup[0]/AXStaticText[@AXValue='Avaya Workplace']")
        click_avaya = ActionChains(self.driver)
        click_avaya.move_to_element(avaya_click)
        click_avaya.click()
        click_avaya.release()
        click_avaya.reset_actions()
        time.sleep(2)
        ActionChains(self.driver).move_to_element_with_offset(avaya_click,9,0).double_click().perform()

        print("Begin button join")
        join = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3MainWindowIdentifier']/AXSplitGroup[0]/AXScrollArea[0]/AXButton[@AXTitle='Join']")
        join_1 = ActionChains(self.driver)
        join_1.move_to_element(join)
        join_1.click()
        join_1.perform()
        join_1.release()
        join_1.reset_actions()
        print("Join successfully!!!") 
        time.sleep(20)
        expected = ' (Me)'
        result1 = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3ConferenceWindowIdentifier']/AXScrollArea[0]/AXTable[@AXIdentifier='UCC3AutomationConferenceRosterParticipantTableIdentifier']/AXRow[@AXSubrole='AXTableRow']/AXCell[0]/AXStaticText[@AXValue=' (Me)']")
        result = ActionChains(self.driver)
        result.move_to_element(result1)
        result.perform()
        result.release()
        result.reset_actions()
        actual_username = result.get_attribute("Name")
        time.sleep(5)
        if expected in actual_username:
            print("Pass!>>>Username is exactly!!!")
            return True
        else: 
            print("Failed!!!")
            return False
        
    def endcall(self):
        print("Button end")
        time.sleep(5)
        call_end = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXIdentifier='UCC3ConferenceWindowIdentifier']/AXCheckBox[@AXIdentifier='UCC3AutomationConferenceRosterLeaveConferenceButtonIdentifier']")
        end_call = ActionChains(self.driver)
        end_call.move_to_element(call_end)
        end_call.click()
        end_call.perform()
        end_call.release()
        end_call.reset_actions()
        # print(len(end_call))
        # print("2")
        print("Call Ended")
        time.sleep(5)


    def close_workplace(self):
        print("Begin close workplace!!!")
        close_mac = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='Avaya Workplace' and @AXIdentifier='UCC3MainWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXSplitGroup[0]/AXButton[@AXIdentifier='UCC3AutomationMainWindowSettingsButton']")
        mac_close = ActionChains(self.driver)
        mac_close.move_to_element(close_mac)
        mac_close.click()
        mac_close.perform()
        mac_close.release()
        mac_close.reset_actions()
        time.sleep(3)
        close_mac1 = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='Avaya Workplace Settings' and @AXIdentifier='UCC3ConfigurationWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXScrollArea[@AXIdentifier='_NS:194']/AXTable[@AXIdentifier='_NS:54']/AXRow[@AXSubrole='AXTableRow']/AXCell[0]/AXStaticText[@AXValue='Support' and @AXIdentifier='Support preferences']")
        mac1_close = ActionChains(self.driver)
        mac1_close.move_to_element(close_mac1)
        mac1_close.click()
        mac1_close.perform()
        mac1_close.release()
        mac1_close.reset_actions()
        time.sleep(3)
        close_mac2 = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='Avaya Workplace Settings' and @AXIdentifier='UCC3ConfigurationWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXScrollArea[@AXIdentifier='_NS:109']/AXTable[@AXIdentifier='_NS:115']/AXRow[@AXSubrole='AXTableRow']/AXCell[0]/AXButton[@AXTitle='Reset Application' and @AXIdentifier='UCC3AutomationConfigurationShowDetailsIdentifier']")
        mac2_close = ActionChains(self.driver)
        mac2_close.move_to_element(close_mac2)
        mac2_close.click()
        mac2_close.perform()
        mac2_close.release()
        mac2_close.reset_actions()
        time.sleep(3)
        close_mac3 = self.driver.find_element(By.XPATH,"/AXApplication[@AXTitle='Avaya Workplace']/AXWindow[@AXTitle='Avaya Workplace Settings' and @AXIdentifier='UCC3ConfigurationWindowIdentifier' and @AXSubrole='AXStandardWindow']/AXSheet[@AXIdentifier='UCC3AlertWindowIdentifier']/AXLayoutArea[@AXIdentifier='UCC3AutomationAlertViewResetIdentifier']/AXButton[@AXTitle='Reset']")
        mac3_close = ActionChains(self.driver)
        mac3_close.move_to_element(close_mac3)
        mac3_close.click()
        mac3_close.perform()
        mac3_close.release()
        mac3_close.reset_actions()
        print("Workplace finished!!!")





mac1 = MAC()
mac1.launch_app()
mac1.Workplace(name="Khoa",address="https://aawg-mt-virtual.hcm.com/portal/tenants/dc1/",meetingid="322006500")
mac1.endcall()
mac1.close_workplace()