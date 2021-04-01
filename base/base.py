# 导包
from selenium.webdriver.support.wait import WebDriverWait
from utils import DriverUtils

"""
1. 对象库层-基类
"""


class BasePage:
    def __init__(self):
        self.driver = DriverUtils.get_driver()

    # 元素定位公用方法
    def find_elt(self, location, timeout=5, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*location))


"""
2. 操作层-基类
"""


class BaseHandle:
    # 模拟输入公用方法
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

    def click_btn1(self, element):
        element.click()

