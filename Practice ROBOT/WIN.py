from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Win():
    def __init__(self):
        print("Create a object winium")
    def prepare_webdriver(self,ip):
        print('Webdriver is ready')
        self.driver=webdriver.Remote(
                command_executor='http://'+ip+':9999',
                desired_capabilities={
                    "debugConnectToRuningApp": 'false',
                    #"app": r"C:/windows/system32/calc.exe"
                    "app": r"C:/Program Files (x86)/Avaya/Avaya IX Workplace/Avaya IX Workplace.exe"
                    }
            )
        print('End')
    def launch_app(self,ip):
        print('Start launch_app')
        if ip == None:
            ip="localhost"
            self.prepare_webdriver(ip)
        else:
            self.prepare_webdriver(ip)
        print('End launch_app')
        #time.sleep(15)
    def calculator(self,number1,number2,choose):
        time.sleep(5)
        print("Welcome to my Calculator")
        #time.sleep(5)
        enter_equal = self.driver.find_element(By.NAME,'Equals')
        enter_number = self.driver.find_element(By.NAME,'Display is 0')
        choose = str(choose)
        #choose = input("Enter a math a,s,m,d: ")
        #print("Type:%s" + type(choose))
        if choose == 'a' :
            print("Start a addition")
            addition_math = self.driver.find_element(By.NAME,'Plus')
            text_enter_number1 = enter_number.send_keys(number1)
            print("Input first number: " + number1)
            #time.sleep(5)
            addition = addition_math.click()
            #time.sleep(5)
            text_enter_number2 = enter_number.send_keys(number2)
            print("Input second number: " + number2)
            equal = enter_equal.click()
            time.sleep(3)
            expected_math = str(int(number1)) +" + "+ str(int(number2))
            locator_math = 'Expression is' + str(expected_math)
            result1 = self.driver.find_element(By.ID,"CalculatorExpression")
            actual_math = result1.get_attribute("Name")
            print("Expression is:" + actual_math)
            expected_result = int(number1)+int(number2)
            locator_result = 'Display is ' + str(expected_result)
            result = self.driver.find_element(By.ID,"CalculatorResults")
            actual_result = result.get_attribute("Name")
            print("value_actual_result: "+actual_result)
            if str(expected_result) in actual_result:
                print("Pass!!!!!")
                print("Result is " + actual_result)
                return True
            else: 
                print("Invalid!!!!")
                return False
    
        elif choose == 's':
            print("Start a subtraction")
            time.sleep(5)
            subtraction_math = self.driver.find_element(By.NAME,'Minus')
            text_enter_number1 = enter_number.send_keys(number1)
            print("Input first number: " + number1)
            subtraction = subtraction_math.click()
            time.sleep(5)
            text_enter_number2 = enter_number.send_keys(number2)
            print("Input second number: " + number2)
            equal = enter_equal.click()
            time.sleep(5)
            expected_math = str(int(number1)) +" - "+ str(int(number2))
            locator_math = 'Expression is' + str(expected_math)
            result1 = self.driver.find_element(By.ID,"CalculatorExpression")
            actual_math = result1.get_attribute("Name")
            print(actual_math)
            expected_result = int(number1) - int(number2)
            locator_result = 'Display is ' + str(expected_result)
            result = self.driver.find_element(By.ID,"CalculatorResults")
            actual_result = result.get_attribute("Name")
            print("value_actual_result: "+ actual_result)
            if str(expected_result) in actual_result:
                print("Pass!!!!!")
                print("Result is " + actual_result)
                return True
            else: 
                print("Invalid!!!!")
                return False
        
        elif choose == 'm':
            print("start a multiplication")
            time.sleep(5)
            multiply_math = self.driver.find_element(By.NAME,'Multiply by')
            text_enter_number1 = enter_number.send_keys(number1)
            print("Input first number: " + number1)
            multiply = multiply_math.click()
            text_enter_number2 = enter_number.send_keys(number2)
            print("Input second number: " + number2)
            equal = enter_equal.click()
            time.sleep(5)
            expected_math = str(int(number1)) +" * "+ str(int(number2))
            locator_math = 'Expression is' + str(expected_math)
            result1 = self.driver.find_element(By.ID,"CalculatorExpression")
            actual_math = result1.get_attribute("Name")
            print(actual_math)
            expected_result = int(number1)*int(number2)
            locator_result = 'Display is ' + str(expected_result)
            result = self.driver.find_element(By.ID,"CalculatorResults")
            actual_result = result.get_attribute("Name")
            print("value_actual_result: "+actual_result)
            if str(expected_result) in actual_result:
                print("Pass!!!!!")
                print("Result is " + actual_result)
                return True
            else: 
                print("Invalid!!!!")
                return False
        
        elif choose == 'd':
            print("Start a division")
            time.sleep(5)
            divide_math = self.driver.find_element(By.NAME,'Divide by')
            text_enter_number1 = enter_number.send_keys(number1)
            print("Input first number: " + number1)
            divide = divide_math.click()
            text_enter_number2 = enter_number.send_keys(number2)
            print("Input second number: " + number2)
            equal = enter_equal.click()   
            time.sleep(5)
            expected_math = str(int(number1)) +" / "+ str(int(number2))
            locator_math = 'Expression is' + str(expected_math)
            result1 = self.driver.find_element(By.ID,"CalculatorExpression")
            actual_math = result1.get_attribute("Name")
            print(actual_math)
            expected_result = int(number1) / int(number2)
            #locator_result = 'Display is ' + str(expected_result)
            result = self.driver.find_element(By.ID,"CalculatorResults")
            actual_result = result.get_attribute("Name")
            print("value_actual_result: "+ actual_result)
            if str(expected_result) in actual_result:
                print("Pass!!!!!")
                print("Result is " + actual_result)
                return True
            else: 
                print("Invalid!!!!")
                return False  
        else:
            print("Invalid a math!!!!!") 
        time.sleep(5)
        

    def Workplace(self,name,address,ID):
        #window = self.driver.find_element(By.NAME,'Avaya Workplace')
        #self.driver.switch_to.frame(window)
        join_meeting = self.driver.find_element(By.NAME,'Join a meeting')
        time.sleep(5)
        join_meeting.click()
        time.sleep(5)
        your_name = self.driver.find_element(By.NAME,'Your name')
        your_name.send_keys(name)
        meeting_address = self.driver.find_element(By.NAME,'Meeting Address')
        meeting_address.send_keys(address)
        meeting_ID = self.driver.find_element(By.NAME,'Meeting ID')
        meeting_ID.send_keys(ID)
        join_button = self.driver.find_element(By.NAME,'Join')
        join_button.click()
        time.sleep(5)
        maximize_window = self.driver.find_element(By.NAME,'Maximize Window')
        maximize_window.click()
        expected = 'Khoa (me)'
        result1 = self.driver.find_element(By.ID,"ParticipantName")
        actual_username = result1.get_attribute("Name")
        time.sleep(10)
        if expected in actual_username:
            print("Pass!>>>Username is exactly!!!")
            return True
        else: 
            print("Failed!!!")
            return False
        time.sleep(5)
    
    def endcall(self,id):
        print("Button end")
        father = self.driver.find_element(By.NAME,id)
        end_call = father.find_element(By.NAME,'End Call')
        # print(len(end_call))
        # print("2")
        end_call.click()
        print("Call Ended")


    def close_workplace(self):
        print("Begin close workplace!!!")
        win_close = self.driver.find_element(By.NAME,'Options and Settings')
        win_close.click()
        time.sleep(3)
        win1_close = self.driver.find_element(By.NAME,'Support')
        win1_close.click()
        time.sleep(3)
        win2_close = self.driver.find_element(By.NAME,'Reset Application')
        win2_close.click()
        time.sleep(3)
        win3_close = self.driver.find_element(By.NAME,'Clear')
        win3_close.click()
        print("Workplace finished!!!")
win1 = Win()
#win1.launch_app(ip="localhost")
win1.launch_app(ip="10.102.1.30")
# win1.calculator(number1="6",number2="3",choose="d")
win1.Workplace(name="Khoa",address="https://aawg-mt-virtual.hcm.com/portal/tenants/dc1/",ID="322006500")
#win1.kkkk(url="http://10.102.2.58/hfs/auto_conf_iview126.txt",username="auto2006000",password="RAPtor1234")
win1.endcall("322006500")
win1.close_workplace()