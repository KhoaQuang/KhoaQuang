from Khoa import Web

class TestPage(Web):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        # self.launch_browser("https://www.example.com/")
TestPage(Web).launch_browser("https://www.example.com/")
    
    