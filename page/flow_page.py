"""
流程页面
"""
import time

import app
from selenium.webdriver.common.by import By

from base.base import BasePage, BaseHandle


# 对象库层
class FlowPage(BasePage):
    def __init__(self):
        super().__init__()
        # 流程中心按钮
        self.flow = (By.XPATH, '//*[contains(text(),"流程中心")]')
        # 流程配置按钮
        self.flow01 = (By.CSS_SELECTOR, '#app > div > div.sidebar-container.shadow-md-x.el-scrollbar > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(22) > li > ul > div:nth-child(1) > a > li > span')
        # 新建按钮
        self.add_btn = (By.XPATH, '//*[contains(text(),"新建")]')
        # 工程类型输入框
        self.gongcheng = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > form:nth-child(2) > div > div:nth-child(2) > div > div > div > div > input')
        # 选择工程类型
        self.gongcheng01 = (By.XPATH, f'//*[text()="{app.gongchengname}"]')
        # 出资方式输入框
        self.chuzi = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > form:nth-child(2) > div > div:nth-child(3) > div > div > div > div.el-input.el-input--suffix > input')
        # 选择出资方式
        self.chuzi01 = (By.XPATH, f'//*[text()="{app.chuziname}"]')
        # 绑定部门输入框
        self.bumen = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > form:nth-child(2) > div > div:nth-child(4) > div > div > div > div.el-input.el-input--suffix > input')
        # 勾选部门
        self.bumen01 = (By.CLASS_NAME, 'el-checkbox__inner')
        # 点击空白处-创建工作流
        self.aa = (By.CSS_SELECTOR, 'body > div:nth-child(9) > div > div.el-dialog__header > span')
        # 确定按钮
        self.yes = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div > div > div > button.el-button.el-button--primary')

    # 找到流程中心按钮
    def find_flow(self):
        return self.find_elt(self.flow)

    # 找到流程配置按钮
    def find_flow01(self):
        return self.find_elt(self.flow01)

    # 找到新建按钮
    def find_add_btn(self):
        return self.find_elt(self.add_btn)

    # 找到工程类型输入框
    def find_gongcheng(self):
        return self.find_elt(self.gongcheng)

    # 找到选择工程类型
    def find_gongcheng01(self):
        return self.find_elt(self.gongcheng01)

    # 找到出资方式输入框
    def find_chuzi(self):
        return self.find_elt(self.chuzi)

    # 找到选择出资方式
    def find_chuzi01(self):
        return self.find_elt(self.chuzi01)

    # 找到绑定部门输入框
    def find_bumen(self):
        return self.find_elt(self.bumen)

    # 找到勾选部门
    def find_bumen01(self):
        return self.find_elt(self.bumen01)

    # 找到空白处
    def find_aa(self):
        return self.find_elt(self.aa)

    # 找到确定按钮
    def find_yes(self):
        return self.find_elt(self.yes)


# 操作层

class FlowHandle(BaseHandle):
    def __init__(self):
        self.flow_page = FlowPage()

    # 点击流程中心
    def click_flow(self):
        self.flow_page.find_flow().click()

    # 点击流程配置
    def click_flow01(self):
        self.flow_page.find_flow01().click()

    # 点击新建
    def click_add_btn(self):
        self.flow_page.find_add_btn().click()

    # 点击工程类型输入框-选择工程类型
    def click_gongcheng(self):
        self.flow_page.find_gongcheng().click()
        time.sleep(0.5)
        self.flow_page.find_gongcheng01().click()

    # 点击出资方式输入框-选择出资方式
    def click_chuzi(self):
        self.flow_page.find_chuzi().click()
        time.sleep(0.5)
        self.flow_page.find_chuzi01().click()

    # 点击绑定部门输入框-选择部门
    def click_bumen(self):
        self.flow_page.find_bumen().click()
        time.sleep(0.5)
        self.flow_page.find_bumen01().click()

    # 点击空白-点击确定
    def click_yes(self):
        # self.flow_page.find_aa().click()
        # time.sleep(1)
        self.flow_page.find_yes().click()


# 业务层
class FlowProxy:
    def __init__(self):
        self.flow_handle = FlowHandle()

    # 新建流程
    def add_flow(self):
        self.flow_handle.click_flow()
        self.flow_handle.click_flow01()
        self.flow_handle.click_add_btn()
        time.sleep(1)
        self.flow_handle.click_gongcheng()
        self.flow_handle.click_chuzi()
        # self.flow_handle.click_bumen()
        self.flow_handle.click_yes()
        time.sleep(2)

