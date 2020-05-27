import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestActionChain:
    def setup(self):
        self.driver = webdriver.Chrome()
        #加上隐式等待
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_actionchains(self):

        self.driver.get("http://sahitest.com/demo/clicks.htm")
        dbl_click = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        click = self.driver.find_element_by_xpath("//input[@value='click me']")
        right_click = self.driver.find_element_by_xpath("//input[@value='right click me']")
        actions = ActionChains(self.driver)
        actions.click(click)
        actions.context_click(right_click)
        actions.double_click(dbl_click)
        actions.perform()

    if __name__ == '__main__':
        pytest.main()

