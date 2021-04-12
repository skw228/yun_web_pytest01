from selenium.webdriver.common.by import By
import app

class PageElements:
    """管理所有页面元素"""

    # ---登录页面元素----
    # 用户名
    username = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/div/div/div[1]/input')
    # 密码
    password = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/div/div/input')
    # 登录按钮
    login_btn = (By.CLASS_NAME, 'el-button')

    # ---受理申请页面元素---
    # 新增按钮
    xz = (By.CSS_SELECTOR,
               '#app > div > div.main-container > section > div > div > div.col_left.el-col.el-col-24 > div.query > div.edit_btn > button.el-button.el-button--primary')
    # 申报单位输入框
    sbdw = (By.CSS_SELECTOR,
                 '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(1) > div > div > div > div > button')
    # 新增申报单位按钮
    xzsbdw = (By.CSS_SELECTOR,
                   '#app > div > div.main-container > section > div > div > div:nth-child(3) > div > div.el-dialog__body > div.dialogTable-wrap > div.el-col.el-col-24 > form > div > button:nth-child(4)')
    # 单位名称输入框
    dwmc = (By.CSS_SELECTOR,
                 'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div > div:nth-child(1) > div > div > div.el-input > input')
    # 新增联系人按钮
    xzlxr = (
        By.CSS_SELECTOR,
        'body > div.el-dialog__wrapper > div > div.el-dialog__body > div:nth-child(2) > div > button')
    # 默认按钮
    mr = (By.CSS_SELECTOR,
               'body > div.el-dialog__wrapper > div > div.el-dialog__body > div:nth-child(3) > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr > td.el-table_35_column_138 > div > label > span.el-radio__input > span')
    # 联系人输入框
    lxr = (By.CSS_SELECTOR,
                'body > div.el-dialog__wrapper > div > div.el-dialog__body > div:nth-child(3) > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr > td.el-table_17_column_83 > div > div > input')
    # 联系电话输入框
    lxdh = (By.CSS_SELECTOR,
                 'body > div.el-dialog__wrapper > div > div.el-dialog__body > div:nth-child(3) > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr > td.el-table_17_column_84 > div > div > input')
    # 保存单位按钮
    bcdw = (By.CSS_SELECTOR,
                 'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary')
    # 客户名称
    khmc = (By.XPATH, f'//*[text()="{app.dwmc}"]')

    # 第一个客户
    kh = (By.CSS_SELECTOR,
               '#app > div > div.main-container > section > div > div > div:nth-child(3) > div > div.el-dialog__body > div.dialogTable-wrap > div.el-table.el-table--fit.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1)')
    # 客户确定按钮
    khqd = (By.CSS_SELECTOR,
                 '#app > div > div.main-container > section > div > div > div:nth-child(3) > div > div.el-dialog__footer > span > button.el-button.el-button--primary > span')
    # 工程地点
    gcdd = (By.CSS_SELECTOR,
                 '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(5) > div > div > div.el-input.el-input--suffix > input')
    # 地址输入框
    dz = (By.CSS_SELECTOR,
               'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.search-box > div.mgl8.el-input.el-input--suffix > input')
    # 地址确定按钮
    dzqd = (By.CSS_SELECTOR,
                 'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary')
    # 业务部门选择框
    ywbm = (By.CSS_SELECTOR,
                 '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(7) > div > div > div > div > input')
    # 选择业务部门
    xzywbm = (By.XPATH, f'//*[text()="{app.ywbm}"]')
    # 工程类型选择框
    gclx = (By.CSS_SELECTOR,
                 '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(8) > div > div > div > div > input')
    # 选择工程类型
    xzgclx = (By.XPATH, f'//*[text()="{app.gclx}"]')

    # 出资方式选择框
    czfs = (By.CSS_SELECTOR,
                 '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(9) > div > div > div > div > input')
    # 选择出资方式
    xzczfs = (By.XPATH, f'//*[text()="{app.czfs}"]')

    # 规范范围选择框
    gffw = (By.CSS_SELECTOR,
                 '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(11) > div > div > div > div > input')
    # 选择规范范围
    xzgffw = (By.CSS_SELECTOR,
                   'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.hover')
    # 推送按钮
    ts = (By.CSS_SELECTOR,
               '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div:nth-child(1) > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--default')