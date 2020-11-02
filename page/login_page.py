"""
客服云登录页面
"""
import time

from selenium.webdriver.common.by import By

from base.base import BasePage, BaseHandle


# 对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名
        self.username = (By.XPATH,
                         '//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/div/div/div[1]/input')
        # 密码
        self.password = (By.XPATH,
                         '//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/div/div/input')
        # 登录按钮
        self.login_btn = (By.CLASS_NAME, 'el-button')

    # 找到用户名输入框
    def find_username(self):
        return self.find_elt(self.username)

    # 找到密码输入框
    def find_password(self):
        return self.find_elt(self.password)

    # 找到登录按钮
    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层

class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 用户名输入
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 密码输入
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)

    # 点击登录
    def click_btn(self):
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录
    def test_login(self, username, password):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.click_btn()
