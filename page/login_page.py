"""
客服云登录页面
"""
from base.base import BasePage, BaseHandle
from page.pageElements import PageElements


# 对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()

    # 找到用户名输入框
    def find_username(self):
        return self.find_elt(PageElements.username)

    # 找到密码输入框
    def find_password(self):
        return self.find_elt(PageElements.password)

    # 找到登录按钮
    def find_login_btn(self):
        return self.find_elt(PageElements.login_btn)


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
