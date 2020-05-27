from time import sleep

from selenium.webdriver import ActionChains

from test_selenium.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        #切换到页面的alert弹窗并点击确认
        self.driver.switch_to_alert().accept()
        sleep(1)
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(1)