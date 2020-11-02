"""
客服云产品页面
"""
import time
import app
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base import BasePage, BaseHandle


# 对象库层
class SetPage(BasePage):
    def __init__(self):
        super().__init__()
        # 设置按钮
        self.set_btn = (By.CLASS_NAME, 'setting')

        # 标准按钮
        self.bz_btn = (By.CSS_SELECTOR,
                       '#app > div > div.sidebar-container.shadow-md-x.el-scrollbar > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(2) > li > div > span')

        # 工程类型按钮
        self.gongcheng_btn = (By.CSS_SELECTOR,
                              '#app > div > div.sidebar-container.shadow-md-x.el-scrollbar > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(2) > li > ul > div:nth-child(1) > a > li > span')
        # 工程类型名称
        self.gongcheng_name = (By.CSS_SELECTOR,
                               '#app > div > div.main-container > section > div > div > div.row_height.el-row > div.col_right.el-col.el-col-12 > div.form-wrapper > div > form > div:nth-child(2) > div > div > div.inptW.el-input > input')
        # 出资方式按钮
        self.chuzi_btn = (By.CSS_SELECTOR,
                          '#app > div > div.sidebar-container.shadow-md-x.el-scrollbar > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(2) > li > ul > div:nth-child(3) > a > li > span')
        # 出资方式名称
        self.chuzi_name = (By.CSS_SELECTOR,
                           '#app > div > div.main-container > section > div > div > div.row_height.el-row > div.col_right.el-col.el-col-12 > div.form-wrapper > div > form > div:nth-child(2) > div > div > div.inptTe.el-input > input')
        # 新增按钮
        self.add_btn = (By.XPATH, '//*[text()="新增"]')
        # 删除按钮
        self.del_btn = (By.XPATH, '//*[text()="删除"]')
        # 编辑按钮
        self.edit_btn = (By.XPATH, '//*[text()="编辑"]')
        # 保存按钮
        self.save_btn = (By.XPATH, '//*[text()="保存"]')
        # 关联设置
        self.guanlian_btn = (By.CSS_SELECTOR,
                             '#app > div > div.sidebar-container.shadow-md-x.el-scrollbar > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(2) > li > ul > div:nth-child(10) > a > li > span')
        # 点击部门类型
        self.guanlian_bumen = (By.CSS_SELECTOR,
                               '#app > div > div.main-container > section > div > div > div > div.col_right.el-col.el-col-12 > div.form-wrapper > form > div > div:nth-child(1) > div > div > div > div > input')
        # 选择部门类型
        self.guanlian_bumen01 = (By.CSS_SELECTOR,
                                 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li > span')
        # 点击工程类型
        self.guanlian_gongcheng = (By.CSS_SELECTOR,
                                   '#app > div > div.main-container > section > div > div > div > div.col_right.el-col.el-col-12 > div.form-wrapper > form > div > div:nth-child(2) > div > div > div > div > input')
        # 选择工程类型
        self.guanlian_gongcheng01 = (By.XPATH, f'//*[text()="{app.gongchengname}"]')

        # 点击出资类型
        self.guanlian_chuzi = (By.CSS_SELECTOR,
                               '#app > div > div.main-container > section > div > div > div > div.col_right.el-col.el-col-12 > div.form-wrapper > form > div > div:nth-child(3) > div > div > div > div > input')
        # 选择出资类型
        self.guanlian_chuzi01 = (By.XPATH, f'//*[text()="{app.chuziname}"]')

    # 找到设置按钮
    def find_set_btn(self):
        return self.find_elt(self.set_btn)

    # 找到标准按钮
    def find_bz_btn(self):
        return self.find_elt(self.bz_btn)

    # 找到工程类型按钮
    def find_gongcheng_btn(self):
        return self.find_elt(self.gongcheng_btn)

    # 找到工程类型名称
    def find_gongcheng_name(self):
        return self.find_elt(self.gongcheng_name)

    # 找到出资方式按钮
    def find_chuzi_btn(self):
        return self.find_elt(self.chuzi_btn)

    # 找到出资方式名称
    def find_chuzi_name(self):
        return self.find_elt(self.chuzi_name)

    # 找到新增按钮
    def find_add_btn(self):
        return self.find_elt(self.add_btn)

    # 找到删除按钮
    def find_del_btn(self):
        return self.find_elt(self.del_btn)

    # 找到编辑按钮
    def find_edit_btn(self):
        return self.find_elt(self.edit_btn)

    # 找到保存按钮
    def find_save_btn(self):
        return self.find_elt(self.save_btn)

    # 找到关联设置按钮
    def find_guanlian_btn(self):
        return self.find_elt(self.guanlian_btn)

    # 找到点击部门类型
    def find_guanlian_bumen(self):
        return self.find_elt(self.guanlian_bumen)

    # 找到选择部门类型
    def find_guanlian_bumen01(self):
        return self.find_elt(self.guanlian_bumen01)

    # 找到点击工程类型
    def find_guanlian_gongcheng(self):
        return self.find_elt(self.guanlian_gongcheng)

    # 找到选择工程类型
    def find_guanlian_gongcheng01(self):
        return self.find_elt(self.guanlian_gongcheng01)

    # 找到点击出资类型
    def find_guanlian_chuzi(self):
        return self.find_elt(self.guanlian_chuzi)

    # 找到选择出资类型
    def find_guanlian_chuzi01(self):
        return self.find_elt(self.guanlian_chuzi01)


# 操作层

class SetHandle(BaseHandle):
    def __init__(self):
        self.set_page = SetPage()

    # 点击设置按钮
    def click_set_btn(self):
        self.set_page.find_set_btn().click()

    # 点击标准按钮
    def click_bz_btn(self):
        self.set_page.find_bz_btn().click()

    # 点击工程类型按钮
    def click_gongcheng_btn(self):
        self.set_page.find_gongcheng_btn().click()

    # 输入工程类型名称
    def input_gongcheng_name(self, name):
        self.input_text(self.set_page.find_gongcheng_name(), name)

    # 点击出资方式按钮
    def click_chuzi_btn(self):
        self.set_page.find_chuzi_btn().click()

    # 输入出资方式名称
    def input_chuzi_name(self, name):
        self.input_text(self.set_page.find_chuzi_name(), name)

    # 点击新增按钮
    def click_add_btn(self):
        # Select(self.set_page.find_cost_item()).select_by_value(item)
        self.set_page.find_add_btn().click()

    # 点击删除按钮
    def click_del_btn(self):
        self.set_page.find_del_btn().click()

    # 点击编辑按钮
    def click_edit_btn(self):
        self.set_page.find_edit_btn().click()

    # 点击保存按钮
    def click_save_btn(self):
        self.set_page.find_save_btn().click()

    # 点击关联设置按钮
    def click_guanlian_btn(self):
        self.set_page.find_guanlian_btn().click()

    # 点击部门类型-选择部门类型
    def click_guanlian_bumen(self):
        self.set_page.find_guanlian_bumen().click()
        time.sleep(0.5)
        self.set_page.find_guanlian_bumen01().click()

    # 点击工程类型-选择工程类型
    def click_guanlian_gongcheng(self):
        self.set_page.find_guanlian_gongcheng().click()
        time.sleep(0.5)
        self.set_page.find_guanlian_gongcheng01().click()

    # 点击出资类型-选择出资类型
    def click_guanlian_chuzi(self):
        self.set_page.find_guanlian_chuzi().click()
        time.sleep(0.5)
        self.set_page.find_guanlian_chuzi01().click()


# 业务层
class SetProxy:
    def __init__(self):
        self.set_handle = SetHandle()

    # 添加工程类型
    def add_gongcheng(self, name):
        self.set_handle.click_set_btn()
        time.sleep(1)
        self.set_handle.click_bz_btn()
        time.sleep(1)
        self.set_handle.click_gongcheng_btn()
        time.sleep(1)
        self.set_handle.click_add_btn()
        self.set_handle.input_gongcheng_name(name)
        self.set_handle.click_save_btn()
        time.sleep(1)

    # 添加出资方式
    def add_chuzi(self, name):
        self.set_handle.click_chuzi_btn()
        time.sleep(1)
        self.set_handle.click_add_btn()
        time.sleep(1)
        self.set_handle.input_chuzi_name(name)
        self.set_handle.click_save_btn()
        time.sleep(1)

    # 添加关联设置
    def add_guanlian(self):
        self.set_handle.click_guanlian_btn()
        time.sleep(1)
        self.set_handle.click_add_btn()
        self.set_handle.click_guanlian_bumen()
        self.set_handle.click_guanlian_gongcheng()
        self.set_handle.click_guanlian_chuzi()
        self.set_handle.click_save_btn()
        time.sleep(3)
