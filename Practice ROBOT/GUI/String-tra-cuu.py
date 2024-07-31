from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import openpyxl


class DiemThiWebScraper():
    def __init__(self):
        print("Create a object website")
        self.driver = webdriver.Chrome()
        self.url="https://thanhnien.vn/giao-duc/tra-cuu-diem-thi.htm"
        self.results = []
    def prepare_webdriver(self):
        print('Webdriver is ready')
        self.driver.maximize_window()
        print('Webdriver was created')
        return True
    def search_diem_thi(self, input_string):
        self.prepare_webdriver()
        self.driver.get(self.url)
        editbox = self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Nhập số báo danh']")
        editbox.clear()
        print('Start search diem thi')        
        editbox.send_keys(input_string)
        editbox.send_keys(Keys.RETURN)
        time.sleep(6)
        self.driver.find_element(By.CSS_SELECTOR,"a[class='click-on btn-search']").click()
        print('End search diem thi')
    
    def user_found(self):
        for input_string in range(19000310, 19000315):
            self.search_diem_thi(str(input_string))
            try:
                result1 = self.driver.find_element(By.CSS_SELECTOR, "span[class='value dm1']").text
                result2 = self.driver.find_element(By.CSS_SELECTOR, "span[class='value dm2']").text
                self.results.append((input_string, result1, result2))
                print("Waiting...!Tìm thấy kết quả điểm thi")
            except:
                self.results.append((input_string, 'Không tìm thấy kết quả', 'Không tìm thấy kết quả'))
                print("Không có kết quả phù hợp!")
                time.sleep(5)

    # def save_to_excel(self, file_name):
    #     workbook = openpyxl.Workbook()
    #     sheet = workbook.active
    #     sheet.append(["Student ID", "Result Toán", "Result Văn"])
    #     for input_string, result1, result2 in self.results:
    #         sheet.append((input_string, result1, result2))
    #     workbook.save(file_name)
    #     print("Search tất cả người tham gia hoàn tất")
    def save_to_excel(self, file_name):
        df = pd.DataFrame(self.results, columns=['Student ID', 'Result Toán', 'Result Văn'])
        df.to_excel(file_name, index=False)    

    def close_browser(self):
        self.driver.quit()
        print("Close browser")

if __name__ == "__main__":
    tra_cuu = DiemThiWebScraper()
    tra_cuu.user_found()
    tra_cuu.save_to_excel("results2.xlsx")
    tra_cuu.close_browser()