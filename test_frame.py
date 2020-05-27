from selenium import webdriver
from selenium.webdriver import ActionChains


class TestFrame:

    # id = "iframeResult"
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换frame查找元素
        self.driver.switch_to.frame("iframeResult")
        #还可以通过这种方式切换frame
        #self.driver.switch_to_frame("iframeResult")
        """
        切换为默认的frame是
        self.driver.switch_to_default_content()
        切换为父级frame是
        self.driver.switch_to.parent_frame()
        """

        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

