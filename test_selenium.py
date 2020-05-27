import pytest
from selenium import webdriver
from time import sleep


class TestSelenium:

    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_one(self):
        self.driver.get("https://www.baidu.com/")
        sleep(2)

    if __name__ == '__main__':
        pytest.main()