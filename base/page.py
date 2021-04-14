from page.flow_page import FlowProxy
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from page.set_page import SetProxy
from page.slsq_page import SlsqProxy
from page.sjwt_page import SjwtProxy
from page.sjct_page import SjctProxy
from page.tzsh_page import TzshProxy
from page.tzqs_page import TzqsProxy
from page.gcgj_page import GcgjProxy
from page.gjqr_page import GjqrProxy
from page.azht_page import AzhtProxy


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

    @classmethod
    def get_sjwtPage(cls):
        """返回设计委托页面类实例化对象"""
        return SjwtProxy()

    @classmethod
    def get_sjctPage(cls):
        """返回设计出图页面类实例化对象"""
        return SjctProxy()

    @classmethod
    def get_tzshPage(cls):
        """返回图纸审核页面类实例化对象"""
        return TzshProxy()

    @classmethod
    def get_tzqsPage(cls):
        """返回图纸签收页面类实例化对象"""
        return TzqsProxy()

    @classmethod
    def get_gcgjPage(cls):
        """返回工程估价页面类实例化对象"""
        return GcgjProxy()

    @classmethod
    def get_gjqrPage(cls):
        """返回估价确认页面类实例化对象"""
        return GjqrProxy()

    @classmethod
    def get_azhtPage(cls):
        """返回安装合同页面类实例化对象"""
        return AzhtProxy()
