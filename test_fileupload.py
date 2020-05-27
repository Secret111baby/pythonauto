from time import sleep

from test_selenium.base import Base


class TestFileUpload(Base):

    def test_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        #运行报错，不知道怎么解决，应该是图片的路径问题
        self.driver.find_element_by_id("stfile").send_keys("/Users/fab/PycharmProjects/pythonauto/test_selenium/20200509114219.png")
        sleep(2)

