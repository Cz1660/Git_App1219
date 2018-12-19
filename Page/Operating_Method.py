import Page,allure
from Base.Base_Method import Base_Method

class Operating_Method(Base_Method):
    def __init__(self,driver):
        Base_Method.__init__(self,driver)
    @allure.step(title="获取文本列表")
    def gain_text_list(self,elements):
        self.text_list = []
        for i in self.find_elements(elements):
            self.text_list.append(i.text)
        allure.attach("列表","{0}".format(self.text_list))
        return self.text_list
    @allure.step(title="点击回退按钮")
    def click_back_button(self):
        self.click_element(Page.back_button)

