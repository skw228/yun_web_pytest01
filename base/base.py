# 导包
import time
from selenium.webdriver.common.by import By
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


# 1.切换窗口
def to_swtich():
    handles = DriverUtils.get_driver().window_handles
    DriverUtils.get_driver().switch_to.window(handles[-1])


# 2.显示等待
def wait(element):
    return WebDriverWait(DriverUtils.get_driver(), 10, 1.0).until(lambda x: x.find_element(*element))


# 4.获取弹出框信息
def get_msg():
    time.sleep(2)
    msg = DriverUtils.get_driver().find_element_by_css_selector(".layui-layer-content").text
    print(msg)
    return msg


# 5.获取alert弹出框信息并关闭
def get_alert():
    time.sleep(2)
    alert = DriverUtils.get_driver().switch_to.alert
    msg = alert.text  # 获取弹出框文本信息
    alert.accept()  # 接受
    print(msg)
    return msg


# 6.获取toast
def get_toast(mess):
    toast_xpath = (By.XPATH, f'//*[text()="{mess}"]')
    return wait(toast_xpath)


# 7.frame切换
def to_frame(ele):
    DriverUtils.get_driver().switch_to.frame(ele)

# 8.
