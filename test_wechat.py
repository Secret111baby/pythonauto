from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWeChat:
    def test_wechat_login(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#apps")
