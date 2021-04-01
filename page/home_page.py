"""
主页面
"""
import time
import app
from selenium.webdriver.common.by import By
from base.base import BasePage, BaseHandle


# 对象库层
class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 工程项目按钮
        self.gcxm = (By.XPATH, '//*[contains(text(),"工程项目")]')
        # 立项按钮
        self.lx = (By.CSS_SELECTOR,
                   '#app > div > div.sidebar-container.shadow-md-x.el-scrollbar > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(1) > li > div > span')
        # 受理申请按钮
        self.slsq = (By.XPATH,
                     '//*[contains(text(),"受理申请")]')

    # 找到工程项目按钮
    def find_gcxm(self):
        return self.find_elt(self.gcxm)

    # 找到立项按钮
    def find_lx(self):
        return self.find_elt(self.lx)

    # 找到受理申请按钮
    def find_slsq(self):
        return self.find_elt(self.slsq)


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


# 业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 进入受理申请页面
    def test_int_slsq(self):
        self.home_handle.click_gcxm()
        time.sleep(1)
        # self.home_handle.click_lx()
        self.home_handle.click_slsq()
        time.sleep(1)
