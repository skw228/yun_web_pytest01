"""
受理申请页面
"""
import time
import app
from selenium.webdriver.common.by import By
from base.base import BasePage, BaseHandle


# 对象库层
class SlsqPage(BasePage):
    def __init__(self):
        super().__init__()
        # 新增按钮
        self.xz = (By.CSS_SELECTOR,
                   '#app > div > div.main-container > section > div > div > div.col_left.el-col.el-col-24 > div.query > div.edit_btn > button.el-button.el-button--primary')
        # 申报单位输入框
        self.sbdw = (By.CSS_SELECTOR,
                     '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(1) > div > div > div > div > button')
        # 新增申报单位按钮
        self.xzsbdw = (By.CSS_SELECTOR,
                       '#app > div > div.main-container > section > div > div > div:nth-child(3) > div > div.el-dialog__body > div.dialogTable-wrap > div.el-col.el-col-24 > form > div > button:nth-child(4)')
        # 单位名称输入框
        self.dwmc = (By.CSS_SELECTOR,
                     'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div > div:nth-child(1) > div > div > div.el-input > input')
        # 新增联系人按钮
        self.xzlxr = (
            By.CSS_SELECTOR,
            'body > div.el-dialog__wrapper > div > div.el-dialog__body > div:nth-child(2) > div > button')
        # 默认按钮
        self.mr = (By.CSS_SELECTOR,
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div:nth-child(3) > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr > td.el-table_35_column_138 > div > label > span.el-radio__input > span')
        # 联系人输入框
        self.lxr = (By.CSS_SELECTOR,
                    'body > div.el-dialog__wrapper > div > div.el-dialog__body > div:nth-child(3) > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr > td.el-table_17_column_83 > div > div > input')
        # 联系电话输入框
        self.lxdh = (By.CSS_SELECTOR,
                     'body > div.el-dialog__wrapper > div > div.el-dialog__body > div:nth-child(3) > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr > td.el-table_17_column_84 > div > div > input')
        # 保存单位按钮
        self.bcdw = (By.CSS_SELECTOR,
                     'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary')
        # 客户名称
        self.khmc = (By.XPATH, f'//*[text()="{app.dwmc}"]')

        # 第一个客户
        self.kh = (By.CSS_SELECTOR,
                   '#app > div > div.main-container > section > div > div > div:nth-child(3) > div > div.el-dialog__body > div.dialogTable-wrap > div.el-table.el-table--fit.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1)')
        # 客户确定按钮
        self.khqd = (By.CSS_SELECTOR,
                     '#app > div > div.main-container > section > div > div > div:nth-child(3) > div > div.el-dialog__footer > span > button.el-button.el-button--primary > span')
        # 工程地点
        self.gcdd = (By.CSS_SELECTOR,
                     '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(5) > div > div > div.el-input.el-input--suffix > input')
        # 地址输入框
        self.dz = (By.CSS_SELECTOR,
                   'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.search-box > div.mgl8.el-input.el-input--suffix > input')
        # 地址确定按钮
        self.dzqd = (By.CSS_SELECTOR,
                     'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary')
        # 业务部门选择框
        self.ywbm = (By.CSS_SELECTOR,
                     '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(7) > div > div > div > div > input')
        # 选择业务部门
        self.xzywbm = (By.CSS_SELECTOR,
                       'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li > span')
        # 工程类型选择框
        self.gclx = (By.CSS_SELECTOR,
                     '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(8) > div > div > div > div > input')
        # 选择工程类型
        self.xzgclx = (By.XPATH, '//*[text()="skw01"]')

        # 出资方式选择框
        self.czfs = (By.CSS_SELECTOR,
                     '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(9) > div > div > div > div > input')
        # 选择出资方式
        self.xzczfs = (By.XPATH, '//*[text()="skw01出资"]')

        # 规范范围选择框
        self.gffw = (By.CSS_SELECTOR,
                     '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(11) > div > div > div > div > input')
        # 选择规范范围
        self.xzgffw = (By.CSS_SELECTOR,
                       'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.hover')
        # 推送按钮
        self.ts = (By.CSS_SELECTOR,
                   '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div:nth-child(1) > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--default')

    # 找到新增按钮
    def find_xz(self):
        return self.find_elt(self.xz)

    # 找到申报单位输入框
    def find_sbdw(self):
        return self.find_elt(self.sbdw)

    # 找到新增申报单位按钮
    def find_xzsbdw(self):
        return self.find_elt(self.xzsbdw)

    # 找到单位名称输入框
    def find_dwmc(self):
        return self.find_elt(self.dwmc)

    # 找到新增联系人按钮
    def find_xzlxr(self):
        return self.find_elt(self.xzlxr)

    # 找到默认按钮
    def find_mr(self):
        return self.find_elt(self.mr)

    # 找到联系人输入框
    def find_lxr(self):
        return self.find_elt(self.lxr)

    # 找到联系电话输入框
    def find_lxdh(self):
        return self.find_elt(self.lxdh)

    # 找到保存单位按钮
    def find_bcdw(self):
        return self.find_elt(self.bcdw)

    # 找到客户名称
    def find_khmc(self):
        return self.find_elt(self.khmc)

    # 找到第一个客户
    def find_kh(self):
        return self.find_elt(self.kh)

    # 找到客户确定按钮
    def find_khqd(self):
        return self.find_elt(self.khqd)

    # 找到工程地点
    def find_gcdd(self):
        return self.find_elt(self.gcdd)

    # 找到地址输入框
    def find_dz(self):
        return self.find_elt(self.dz)

    # 找到地址确定按钮
    def find_dzqd(self):
        return self.find_elt(self.dzqd)

    # 找到业务部门选择框
    def find_ywbm(self):
        return self.find_elt(self.ywbm)

    # 找到选择业务部门
    def find_xzywbm(self):
        return self.find_elt(self.xzywbm)

    # 找到工程类型选择框
    def find_gclx(self):
        return self.find_elt(self.gclx)

    # 找到工程类型
    def find_xzgclx(self):
        return self.find_elt(self.xzgclx)

    # 找到出资方式选择框
    def find_czfs(self):
        return self.find_elt(self.czfs)

    # 找到出资方式
    def find_xzczfs(self):
        return self.find_elt(self.xzczfs)

    # 找到规范范围选择框
    def find_gffw(self):
        return self.find_elt(self.gffw)

    # 找到规范范围
    def find_xzgffw(self):
        return self.find_elt(self.xzgffw)

    # 找到推送按钮
    def find_ts(self):
        return self.find_elt(self.ts)


# 操作层

class SlsqHandle(BaseHandle):
    def __init__(self):
        self.slsq_page = SlsqPage()

    # 点击新增按钮
    def click_xz(self):
        self.slsq_page.find_xz().click()

    # 点击申报单位输入框
    def click_sbdw(self):
        self.slsq_page.find_sbdw().click()

    # 点击新增申报单位按钮
    def click_xzsbdw(self):
        self.slsq_page.find_xzsbdw().click()

    # 输入单位名称
    def input_dwmc(self, dwmc):
        self.input_text(self.slsq_page.find_dwmc(), dwmc)

    # 点击新增联系人按钮
    def click_xzlxr(self):
        self.slsq_page.find_xzlxr().click()

    # 点击默认按钮
    def click_mr(self):
        self.slsq_page.find_mr().click()

    # 输入联系人
    def input_lxr(self, lxr):
        self.input_text(self.slsq_page.find_lxr(), lxr)

    # 输入联系电话
    def input_lxdh(self, lxdh):
        self.input_text(self.slsq_page.find_lxdh(), lxdh)

    # 点击保存单位按钮
    def click_bcdw(self):
        self.slsq_page.find_bcdw().click()

    # 点击客户名称
    def click_khmc(self):
        self.slsq_page.find_khmc().click()

    # 点击第一个客户名称
    def click_kh(self):
        self.slsq_page.find_kh().click()

    # 点击客户确定按钮
    def click_khqd(self):
        self.slsq_page.find_khqd().click()

    # 点击工程地点，输入地址，点击确定
    def click_gcdd(self, dz):
        self.slsq_page.find_gcdd().click()
        time.sleep(0.5)
        self.input_text(self.slsq_page.find_dz(), dz)
        time.sleep(2)
        self.slsq_page.find_dzqd().click()

    # 点击业务部门并选择
    def click_ywbm(self):
        self.slsq_page.find_ywbm().click()
        self.slsq_page.find_xzywbm().click()

    # 点击工程类型并选择
    def click_gclx(self):
        self.slsq_page.find_gclx().click()
        time.sleep(0.5)
        self.slsq_page.find_xzgclx().click()

    # 点击出资方式并选择
    def click_czfs(self):
        self.slsq_page.find_czfs().click()
        time.sleep(0.5)
        self.slsq_page.find_xzczfs().click()

    # 找到规范范围并选择
    def click_gffw(self):
        self.slsq_page.find_gffw().click()
        self.slsq_page.find_xzgffw().click()

    # 点击推送
    def click_ts(self):
        self.slsq_page.find_ts().click()


# 业务层
class SlsqProxy:
    def __init__(self):
        self.slsq_handle = SlsqHandle()

    # 输入受理申请内容并推送
    def test_slsq(self, dz):
        time.sleep(1)
        self.slsq_handle.click_xz()
        time.sleep(1)
        self.slsq_handle.click_sbdw()
        time.sleep(2)
        # self.slsq_handle.click_xzsbdw()
        # time.sleep(1)
        # self.slsq_handle.input_dwmc(dwmc)
        # time.sleep(1)
        # self.slsq_handle.click_xzlxr()
        # time.sleep(1)
        # self.slsq_handle.click_mr()
        # time.sleep(1)
        # self.slsq_handle.input_lxr(lxr)
        # time.sleep(1)
        # self.slsq_handle.input_lxdh(lxdh)
        # time.sleep(1)
        # self.slsq_handle.click_bcdw()
        # time.sleep(1)
        # self.slsq_handle.click_khmc()
        # time.sleep(1)
        self.slsq_handle.click_kh()
        time.sleep(1)
        self.slsq_handle.click_khqd()
        time.sleep(1)
        self.slsq_handle.click_gcdd(dz)
        time.sleep(1)
        self.slsq_handle.click_ywbm()
        time.sleep(1)
        self.slsq_handle.click_gclx()
        time.sleep(1)
        self.slsq_handle.click_czfs()
        time.sleep(1)
        self.slsq_handle.click_ts()
        time.sleep(3)
