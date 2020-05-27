from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options

class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_id("kw")
        search = self.driver.find_element_by_id("su")
        #对搜索框的元素进行输入“杨幂”
        el.send_keys("杨幂")
        action = TouchActions(self.driver)
        #点击百度一下
        action.tap(search)
        action.perform()
        #页面进行滑动，起始元素，偏离点
        action.scroll_from_element(search, 0, 10000).perform()
