import time,allure
from selenium.webdriver.support.wait import WebDriverWait


class Base_Method:
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    def find_elements(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    def click_element(self,loc):
        self.find_element(loc).click()
    @allure.step(title="输入操作")
    def send_keys_text(self,loc,text):
        self.element = self.find_element(loc)
        self.element.clear()
        allure.attach("输入","{0}".format(text))
        self.element.send_keys(text)
    @allure.step(title="截图操作")
    def gain_screenshot(self):
        self.time = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        allure.attach("图片名字","{0}".format("app_%s.png"%self.time))
        return self.driver.get_screenshot_as_file\
            ("C:/Users/Administrator/PycharmProjects/Git_App1219/Gain_Screenshot/app_%s.png"%self.time)