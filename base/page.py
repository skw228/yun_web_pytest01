from page.flow_page import FlowProxy
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from page.set_page import SetProxy
from page.slsq_page import SlsqProxy


class Page:
    """返回所有页面实例化对象"""

    @classmethod
    def get_flowPage(cls):
        """返回流程页面类实例化对象"""
        return FlowProxy()

    @classmethod
    def get_homePage(cls):
        """返回主页面类实例化对象"""
        return HomeProxy()

    @classmethod
    def get_loginPage(cls):
        """返回登录页面类实例化对象"""
        return LoginProxy()

    @classmethod
    def get_setPage(cls):
        """返回设置页面类实例化对象"""
        return SetProxy()

    @classmethod
    def get_slsqPage(cls):
        """返回受理申请页面类实例化对象"""
        return SlsqProxy()
