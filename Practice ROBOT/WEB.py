from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Web():
    url=""
    def __init__(self, url):
        print("Create a object website")
        url=url
    def prepare_webdriver(self,ip):
        print('Webdriver is ready')
        profile_temp = webdriver.ChromeOptions()
        profile_temp.accept_untrusted_cert = True
        profile_temp.add_argument("--lang=en")
        profile_temp.add_argument("--disable-application-cache")
        profile_temp.add_argument("start-maximized")
        self.cap = profile_temp.to_capabilities()
        self.cap['goog:loggingPrefs'] = { 'browser':'ALL' }
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=self.cap)    
        print('Webdriver was created')
        return True
    def launch_browser(self,ip=None):
        print('Start launch_browser')
        self.prepare_webdriver(ip)
        self.driver.get(self.url)
        print('End launch_browser')
        return True
    def title_mywebsite(self):
        title_web = "My Store"
        title_current = self.driver.title
        if title_current == title_web: 
            print("Welcome to My Website: " + title_current)
            return True
        else:
            self.fail('Goto %s failed,please check network'% self.url)
            print("Invalid")
            return False
    def sign_up(self,email,gender,fname,lname,passw,day,month,year,company,address1,address2,city,state,zip,country,mobile):
        print('Start sign_up')
        sign_up_button = self.driver.find_element(By.CSS_SELECTOR,"a[class='login']") 
        sign_up_button.click()
        time.sleep(3)
        print('Email had written')
        email_textbox = self.driver.find_element(By.CSS_SELECTOR,"input[id='email_create']")
        email_textbox.send_keys(email)
        print(email + 'created')
        create_subcribe_button = self.driver.find_element(By.CSS_SELECTOR,"button[id='SubmitCreate']")
        create_subcribe_button.click()
        print("Subcribe was created")
        time.sleep(10)
        input_mr = self.driver.find_element(By.CSS_SELECTOR,"input[id='id_gender1']")
        input_mrs = self.driver.find_element(By.CSS_SELECTOR,"input[id='id_gender2']")
        if gender == 'mr':
            input_mr.click()
            print("Mr was writted")
        elif gender == 'mrs':
            input_mrs.click()
            print("Mrs was writted")
        else:
            print("Invalid option!!")
        print('First name had written')
        input_fname = self.driver.find_element(By.CSS_SELECTOR,"input[id='customer_firstname']")
        input_fname.send_keys(fname)
        print(fname + 'created')
        print('Last name had written')
        input_lname = self.driver.find_element(By.CSS_SELECTOR,"input[id='customer_lastname']")
        input_lname.send_keys(lname)
        print(lname + 'created')
        print('Password had written')
        input_pass = self.driver.find_element(By.CSS_SELECTOR,"input[name='passwd']")
        input_pass.send_keys(passw)
        print(passw + 'created')
        print('Day had choose')
        day_select = self.driver.find_element(By.CSS_SELECTOR,"select[name='days']")
        select = Select(day_select)
        select.select_by_value(day)
        print('Day had created')
        print('Month had choose')
        month_select = self.driver.find_element(By.CSS_SELECTOR,"select[name='months']")
        select = Select(month_select)
        select.select_by_value(month)
        print('Month had created')
        print('Year had choose')
        month_select = self.driver.find_element(By.CSS_SELECTOR,"select[name='years']")
        select = Select(month_select)
        select.select_by_value(year)
        print('Year had created')
        print('Company had written')
        company_input = self.driver.find_element(By.CSS_SELECTOR,"input[id='company']")
        company_input.send_keys(company)
        print(company + 'created')
        print('Address1 had written')
        address1_input = self.driver.find_element(By.CSS_SELECTOR,"input[name='address1']")
        address1_input.send_keys(address1)
        print(address1 + 'created')
        print('Address2 had written')
        address2_input = self.driver.find_element(By.CSS_SELECTOR,"input[name='address2']")
        address2_input.send_keys(address2)
        print(address2 + 'created')
        print('City had written')
        city_input = self.driver.find_element(By.CSS_SELECTOR,"input[name='city']")
        city_input.send_keys(city)
        print(city + 'created')
        print('State had written')
        state_select = self.driver.find_element(By.CSS_SELECTOR,"select[id='id_state']")
        select = Select(state_select)
        select.select_by_value(state)
        print('State had created')
        print('Zip had written')
        zip_input = self.driver.find_element(By.CSS_SELECTOR,"input[id='postcode']")
        zip_input.send_keys(zip)
        print(zip + 'created')
        print('Country had written')
        country_select = self.driver.find_element(By.CSS_SELECTOR,"select[id='id_country']")
        select = Select(country_select)
        select.select_by_value(country)
        print('Country had created')
        print('Mobile phone had written')
        mobile_input = self.driver.find_element(By.CSS_SELECTOR,"input[name='phone_mobile']")
        mobile_input.send_keys(zip)
        print(mobile + 'created')
        time.sleep(5)
        print("Register was button")
        register_button = self.driver.find_element(By.CSS_SELECTOR,"button[name='submitAccount']")
        register_button.click()
        print("Register was created")
        print('End sign_up')
        Message = "Welcome to your account. Here you can manage all of your personal information and orders."
        web_element = self.driver.find_element(By.CSS_SELECTOR,"p[class='info-account']")
        text_web_element = web_element.text
        if text_web_element == Message:
            print("Pass!!!!")
            pass
        else: 
            print("Invalid!!!!")
    def sign_out(self):
        time.sleep(5)
        sign_out_button = self.driver.find_element(By.CSS_SELECTOR,"a[class='logout']")
        sign_out_button.click()
        print("Logout successfully!!!")
        time.sleep(5)
    def sign_in(self,email,passw):
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR,"a[class='login']")
        sign_in_button.click()
        print("Login successfully!!!")
        print('Email had written')
        email_address_input = self.driver.find_element(By.CSS_SELECTOR,"input[id='email']")
        email_address_input.send_keys(email)
        print(email + 'created') 
        print('Email had written')
        pass_word_input = self.driver.find_element(By.CSS_SELECTOR,"input[id='passwd']")
        if passw == '123456khoa':
            pass_word_input.send_keys(passw)
            print("Passw was writted")
        elif passw == 'khoa123456':
            pass_word_input.send_keys(passw)
            print("Passwd was writted")
        else:
            print("Invalid option!!")
        sign_intt_button = self.driver.find_element(By.CSS_SELECTOR,"button[id='SubmitLogin']")
        sign_intt_button.click()
        print("Login successfully!!!")
        time.sleep(5)
        username_check  = "Quang Dang"
        account_username_button = self.driver.find_element(By.CSS_SELECTOR,"a[class='account']")
        text_account_username_button = account_username_button.text   
        if text_account_username_button == username_check:
            print("Acount exactly: " + text_account_username_button)
            pass
        else:
            print("Account don't exactly")
            return False
        print("My personal information had been pushed!!!")
        personal_infor_button = self.driver.find_element(By.CSS_SELECTOR,"a[title='Information']")
        personal_infor_button.click()
        print("See my personal information successfully!!!")
        time.sleep(5)
        
    def change_information(self,fname,lname,day,month,year,passw,passwd):
        print('First name had written')
        input_fname = self.driver.find_element(By.CSS_SELECTOR,"input[id='firstname']")
        input_fname.clear()
        input_fname.send_keys(fname)
        print(fname + 'changed')
        print('Last name had written')
        input_lname = self.driver.find_element(By.CSS_SELECTOR,"input[id='lastname']")
        input_lname.clear()
        input_lname.send_keys(lname)
        print(lname + 'changed')
        print('Day had choose')
        day_select = self.driver.find_element(By.CSS_SELECTOR,"select[name='days']")
        select = Select(day_select)
        select.select_by_value(day)
        print('Day had changed')
        print('Month had choose')
        month_select = self.driver.find_element(By.CSS_SELECTOR,"select[name='months']")
        select = Select(month_select)
        select.select_by_value(month)
        print('Month had created')
        print('Year had choose')
        month_select = self.driver.find_element(By.CSS_SELECTOR,"select[name='years']")
        select = Select(month_select)
        select.select_by_value(year)
        print('Year had created')
        current_password_input = self.driver.find_element(By.CSS_SELECTOR,"input[name='old_passwd']")
        current_password_input.send_keys(passw)
        new_password_input = self.driver.find_element(By.CSS_SELECTOR,"input[name='passwd']")
        new_password_input.send_keys(passwd)
        confirmation_password_input = self.driver.find_element(By.CSS_SELECTOR,"input[name='confirmation']")
        confirmation_password_input.send_keys(passwd)
        save_inf_button = self.driver.find_element(By.CSS_SELECTOR,"button[name='submitIdentity']")
        save_inf_button.click()
        print("Save successfully!!!")
        time.sleep(5)
        Message = "Your personal information has been successfully updated."
        your_infor_element = self.driver.find_element(By.CSS_SELECTOR,"p[class='alert alert-success']")
        text_your_infor_element = your_infor_element.text
        if text_your_infor_element == Message:
            print("Pass!!!!>>Check your personal information has been successfully updated")
            return True
        else: 
            print("Invalid!!!!")
            return False
        time.sleep(5)
    
    def purchase_items(self,item1,item2):
        print("Search Begun")
        search_item1_input = self.driver.find_element(By.CSS_SELECTOR,"input[id='search_query_top']")
        search_item1_input.send_keys(item1)
        print("Search successfully!!!")
        search_item1_button = self.driver.find_element(By.CSS_SELECTOR,"button[name='submit_search']")
        search_item1_button.click()
        time.sleep(7)
        quick_view1_a = self.driver.find_element(By.CSS_SELECTOR,"img[title='Blouse']")
        quick_view1_a.click()
        time.sleep(15)
        #iframe = self.driver.find_element(By.CSS_SELECTOR,"iframe[id*='fancybox-frame']")
        #self.driver.switch_to.frame(iframe)
        add_to_cart_a = self.driver.find_element(By.CSS_SELECTOR,"button[name='Submit']")
        add_to_cart_a.click()
        self.driver.switch_to.default_content()
        time.sleep(7)
        continute_shopping1_span = self.driver.find_element(By.CSS_SELECTOR,"span[title='Continue shopping']")
        continute_shopping1_span.click()
        time.sleep(5)
        print("Search Begun")
        search_item1_input = self.driver.find_element(By.CSS_SELECTOR,"input[id='search_query_top']")
        search_item1_input.clear()
        search_item1_input.send_keys(item2)
        print("Search successfully!!!")
        search_item2_button = self.driver.find_element(By.CSS_SELECTOR,"button[name='submit_search']")
        search_item2_button.click()
        time.sleep(7)
        quick_view2_a = self.driver.find_element(By.CSS_SELECTOR,"img[title='Faded Short Sleeve T-shirts']")
        quick_view2_a.click()
        time.sleep(15)
        #iframe1 = self.driver.find_element(By.CSS_SELECTOR,"iframe[id*='fancybox-frame']")
        #self.driver.switch_to.frame(iframe1)
        add_to_cart1_a = self.driver.find_element(By.CSS_SELECTOR,"button[name='Submit']")
        add_to_cart1_a.click()
        self.driver.switch_to.default_content()
        time.sleep(7)
        continute_shopping2_span = self.driver.find_element(By.CSS_SELECTOR,"span[title='Continue shopping']")
        continute_shopping2_span.click()
        time.sleep(5)
        view_cart_a = self.driver.find_element(By.CSS_SELECTOR,"a[title='View my shopping cart']")
        view_cart_a.click()
        time.sleep(5)
        delete_item1 = self.driver.find_element(By.CSS_SELECTOR,"a[id='2_7_0_602866']")
        delete_item1.click()
#        delete_item2 = self.driver.find_element(By.CSS_SELECTOR,"a[id='6_31_0_602866']")
#        delete_item2.click()
        time.sleep(5)
        proceed_checkout_a = self.driver.find_element(By.CSS_SELECTOR,"a[class='button btn btn-default standard-checkout button-medium']")
        proceed_checkout_a.click()
        time.sleep(10)
        fullname_li = self.driver.find_element(By.CSS_SELECTOR,"li[class='address_firstname address_lastname']")
        infor_fullname_li = fullname_li.text
        if infor_fullname_li == "Quang Khoa":
            print("Full name: " + infor_fullname_li)
        else: 
            print("Incorrect name")
            return False
        company_li = self.driver.find_element(By.CSS_SELECTOR,"li[class='address_company']")
        infor_company_li = company_li.text
        if infor_company_li == "Khoa TMA":
            print("Company name: " + infor_company_li)
        else: 
            print("Incorrect name")
            return False
        address_li = self.driver.find_element(By.CSS_SELECTOR,"li[class='address_address1 address_address2']")
        infor_address_li = address_li.text
        if infor_address_li == "Khoa,hai ba trung A21,Tang 4":
            print("Address name is : " + infor_address_li)
        else: 
            print("Incorrect name")
            return False
        city_li = self.driver.find_element(By.CSS_SELECTOR,"li[class='address_city address_state_name address_postcode']")
        infor_city_li = city_li.text
        if infor_city_li == "HCM, Massachusetts 00000":
            print("City name is : " + infor_city_li)
        else: 
            print("Incorrect name")
            return False
        country_li = self.driver.find_element(By.CSS_SELECTOR,"li[class='address_country_name']")
        infor_country_li = country_li.text
        if infor_country_li == "United States":
            print("Country name is : " + infor_country_li)
        else: 
            print("Incorrect!!!")
            return False
        phone_li = self.driver.find_element(By.CSS_SELECTOR,"li[class='address_phone_mobile']")
        infor_phone_li = phone_li.text
        if infor_phone_li == "00000":
            print("Phone mobile name is : " + infor_phone_li)
        else: 
            print("Incorrect phone")
            return False
        proceed_to_checkout_button = self.driver.find_element(By.CSS_SELECTOR,"button[name='processAddress']")
        proceed_to_checkout_button.click()
        time.sleep(7)
        checkbox_agree = self.driver.find_element(By.CSS_SELECTOR,"input[id='cgv']")
        checkbox_agree.click()
        proceed_to_checkoutt_button = self.driver.find_element(By.CSS_SELECTOR,"button[name='processCarrier']")
        proceed_to_checkoutt_button.click()
        time.sleep(10)
        pay_mycheck = self.driver.find_element(By.CSS_SELECTOR,"a[class='cheque']")
        pay_mycheck.click()
        time.sleep(8)
        confir_myorder = self.driver.find_element(By.CSS_SELECTOR,"button[class='button btn btn-default button-medium']")
        confir_myorder.click()
        time.sleep(5)
        Message = "Your order on My Store is complete."
        your_infor_element = self.driver.find_element(By.CSS_SELECTOR,"p[class='alert alert-success']")
        text_your_infor_element = your_infor_element.text
        price_payment_infor = self.driver.find_element(By.CSS_SELECTOR,"span[class='price']")
        text_price_payment_infor = price_payment_infor.text
        if text_your_infor_element == Message:
            print("Your order on My Store is complete. Your price is:  " + text_price_payment_infor )
            return True
        else: 
            print("Invalid!!!!")
            return False
        time.sleep(5)
    def close_web(self):
        web_close = self.driver.close()
        print("My program is closed!!!")
        
        
        

web1 = Web("https://www.python.org/downloads/release/python-3119/")
# web1.launch_browser(url = "http://automationpractice.com/index.php")
web1.launch_browser()
web1.title_mywebsite()
#web1.sign_up(email="khoa1233666666@gmail.com",gender="mr",fname="Quang",lname="Khoa",passw="khoa123456",day="12",month="12",year="1999",company="Khoa TMA",address1="Khoa,hai ba trung",address2="A21,Tang 4",city="HCM",state="21",zip="00000",country="21",mobile="09999000")
#web1.sign_out()
#web1.sign_in(email="khoa1233666666@gmail.com",passw="123456khoa")
#web1.change_information(fname="Quang",lname="Dang",day="10",month="1",year="2000",passwd="khoa123456",passw="123456khoa")
#web1.sign_out()
web1.sign_in(email="khoa1233666666@gmail.com",passw="khoa123456")
web1.purchase_items(item1="Blouse",item2="Faded Short Sleeve T-shirts")
web1.close_web()
