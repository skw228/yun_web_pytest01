"""
主页面
"""
import time
from base.base import BasePage, BaseHandle
from page.pageElements import PageElements


# 对象库层


class HomePage(BasePage):
    def __init__(self):
        super().__init__()

    # 找到工程项目按钮
    def find_gcxm(self):
        return self.find_elt(PageElements.gcxm)

    # 找到立项按钮
    def find_lx(self):
        return self.find_elt(PageElements.lx)

    # 找到受理申请按钮
    def find_slsq(self):
        return self.find_elt(PageElements.slsq)

    # 找到设计按钮
    def find_sj(self):
        return self.find_elt(PageElements.sj)

    # 找到设计委托按钮
    def find_sjwt(self):
        return self.find_elt(PageElements.sjwt)

    # 找到设计出图按钮
    def find_sjct(self):
        return self.find_elt(PageElements.sjct)

    # 找到图纸审核按钮
    def find_tzsh(self):
        return self.find_elt(PageElements.tzsh)

    # 找到图纸签收按钮
    def find_tzqs(self):
        return self.find_elt(PageElements.tzqs)

    # 找到预算按钮
    def find_ys(self):
        return self.find_elt(PageElements.ys)

    # 找到工程估价
    def find_gcgj(self):
        return self.find_elt(PageElements.gcgj)

    # 找到估价确认
    def find_gjqr(self):
        return self.find_elt(PageElements.gjqr)

    # 找到合同
    def find_ht(self):
        return self.find_elt(PageElements.ht)

    # 找到安装合同
    def find_azht(self):
        return self.find_elt(PageElements.azht)
# 操作层

class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    # 点击工程项目
    def click_gcxm(self):
        self.home_page.find_gcxm().click()

    # 点击立项
    def click_lx(self):
        self.home_page.find_lx().click()

    # 点击受理申请
    def click_slsq(self):
        self.home_page.find_slsq().click()

    # 点击设计
    def click_sj(self):
        self.home_page.find_sj().click()

    # 点击设计委托
    def click_sjwt(self):
        self.home_page.find_sjwt().click()

    # 点击设计出图
    def click_sjct(self):
        self.home_page.find_sjct().click()

    # 点击图纸审核
    def click_tzsh(self):
        self.home_page.find_tzsh().click()

    # 点击图纸签收
    def click_tzqs(self):
        self.home_page.find_tzqs().click()

    # 点击预算
    def click_ys(self):
        self.home_page.find_ys().click()

    # 点击工程估价
    def click_gcgj(self):
        self.home_page.find_gcgj().click()

    # 点击估价确认
    def click_gjqr(self):
        self.home_page.find_gjqr().click()

    # 点击合同
    def click_ht(self):
        self.home_page.find_ht().click()

    # 点击安装合同
    def click_azht(self):
        self.home_page.find_azht().click()


# 业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()
        self.home_page = HomePage()

    # 进入受理申请
    def test_int_slsq(self):
        self.home_handle.click_gcxm()
        # self.home_handle.click_lx()
        self.home_handle.click_slsq()

    # 进入设计委托
    def test_int_sjwt(self):
        self.home_handle.click_sj()
        self.home_handle.click_sjwt()

    # 进入设计出图
    def test_int_sjct(self):
        if self.home_page.find_sjct():
            self.home_handle.click_sjct()
        else:
            self.home_handle.click_sjct()
            self.home_handle.click_sjct()

    # 进入图纸审核
    def test_int_tzsh(self):
        time.sleep(2)
        self.home_handle.click_tzsh()

    # 进入图纸签收
    def test_int_tzqs(self):
        self.home_handle.click_tzqs()

    # 进入工程估价
    def test_int_gcgj(self):
        self.home_handle.click_ys()
        self.home_handle.click_gcgj()

    # 进入估价确认
    def test_int_gjqr(self):
        self.home_handle.click_gjqr()

    # 进入安装合同
    def test_int_azht(self):
        self.home_handle.click_ht()
        self.home_handle.click_azht()



