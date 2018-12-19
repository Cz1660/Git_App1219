from Base.Get_Driver import Get_Driver
from Return_Page.Return_Page import Return_Page
from Yaml.Read_Yaml import Read_Yaml
import pytest,allure,time,Page

def gain_yaml():
    yaml_list = []
    yaml_data = Read_Yaml("Input_Yaml.yaml").read_yaml()
    for i in yaml_data.keys():
        yaml_list.append((i,yaml_data.get(i).get("input_text"),
                          yaml_data.get(i).get("assert_text_001"),yaml_data.get(i).get("assert_text_002")))
    return yaml_list
class Test_Login:
    def setup_class(self):
        self.Dv = Return_Page(Get_Driver().get_driver("com.android.settings",".HWSettings"))
    def teardown_class(self):
        self.Dv.driver.quit()
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('test_number,input_text,assert_text_001,assert_text_002',gain_yaml())
    def test_setting(self,test_number,input_text,assert_text_001,assert_text_002):
        @allure.step(title=test_number)
        def test_setting_001():
            self.Dv.return_page().send_keys_text(Page.search_setting,input_text)
            time.sleep(1)
            @allure.step(title="断言并获取文本的列表")
            def assert_text(elements):
                try:
                    if assert_text_002:
                        assert assert_text_001 in self.Dv.return_page().gain_text_list(elements)
                        assert assert_text_002 in self.Dv.return_page().gain_text_list(elements)
                    else:
                        assert assert_text_001 in self.Dv.return_page().gain_text_list(elements)
                except Exception as E:
                    print(E)
                finally:
                    self.Dv.return_page().gain_screenshot()
                    time.sleep(1)
                    self.Dv.return_page().click_back_button()
            assert_text(Page.search_title)
        test_setting_001()
