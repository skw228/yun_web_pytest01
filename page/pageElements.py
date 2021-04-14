from selenium.webdriver.common.by import By
import app


class PageElements:
    """管理所有页面元素"""

    # --------------------------------------------------登录页面元素------------------------------------------------------------------------------
    # 用户名
    username = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/div/div/div[1]/input')
    # 密码
    password = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/div/div/input')
    # 登录按钮
    login_btn = (By.CLASS_NAME, 'el-button')

    # --------------------------------------------------主页面元素--------------------------------------------------------------------------------
    # 工程项目按钮
    gcxm = (By.XPATH, '//*[contains(text(),"工程项目")]')
    # 立项按钮
    lx = (By.XPATH, '//*[text()="立项"]')
    # 受理申请按钮
    slsq = (By.XPATH, '//*[text()="受理申请"]')
    # 设计按钮
    sj = (By.XPATH, '//*[text()="设计"]')
    # 设计委托按钮
    sjwt = (By.XPATH, '//*[text()="设计委托"]')
    # 设计出图按钮
    sjct = (By.XPATH, '//*[text()="设计出图"]')
    # 图纸审核按钮
    tzsh = (By.XPATH, '//*[text()="图纸审核"]')
    # 图纸签收按钮
    tzqs = (By.XPATH, '//*[text()="图纸签收"]')
    # 预算按钮
    ys = (By.XPATH, '//*[text()="预算"]')
    # 工程估价按钮
    gcgj = (By.XPATH, '//*[text()="工程估价"]')
    # 估价确认按钮
    gjqr = (By.XPATH, '//*[text()="估价确认"]')
    # 合同按钮
    ht = (By.XPATH, '//*[text()="合同"]')
    # 安装合同按钮
    azht = (By.XPATH, '//*[text()="安装合同"]')
    # -----------------------------------------------受理申请页面元素------------------------------------------------------------------------------
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
    # 一点点
    ydd = (By.CSS_SELECTOR,
           'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.table > ul > li:nth-child(1) > div.info > p.name')

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

    # -----------------------------------------------设计委托页面元素------------------------------------------------------------------------------
    # 派工
    pg = (By.CSS_SELECTOR,
          '#app > div > div.main-container > section > div > div > div > div.col_right.el-col.el-col-12 > div.dialog-footer.btn-dispatch > button > span')
    # 确定
    sjwt_qd = (By.CSS_SELECTOR,
               'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span')
    # -----------------------------------------------设计出图页面元素------------------------------------------------------------------------------
    # 登记
    sjct_dj = (By.CSS_SELECTOR,
               '#app > div > div.main-container > section > div > div > div.row_height.el-row > div.col_left.el-col.el-col-12 > div.query > div.edit_btn > button.el-button.el-button--primary')

    # 保存
    sjct_bc = (By.CSS_SELECTOR,
               '#app > div > div.main-container > section > div > div > div.row_height.el-row > div.col_right.el-col.el-col-12 > div.dialog-footer.btn-save > div > button.el-button.el-button--primary')

    # 推送
    sjct_ts = (By.CSS_SELECTOR,
               '#app > div > div.main-container > section > div > div > div.row_height.el-row > div.col_right.el-col.el-col-12 > div.dialog-footer.btn-save > div > button.el-button.el-button--default')
    # -----------------------------------------------图纸审核页面元素------------------------------------------------------------------------------
    # 通过
    tzsh_tg = (By.XPATH,
               '//*[@id="app"]/div/div[3]/section/div/div/div/div[2]/div[1]/form/div/div[1]/div/div/div/label[1]/span[1]')
    # 审核意见
    tzsh_shyj = (By.CSS_SELECTOR,
                 '#app > div > div.main-container > section > div > div > div > div.col_right.el-col.el-col-12 > div.form-wrapper > form > div > div.el-col.el-col-24 > div > div > div.inptW.el-textarea > textarea')
    # 提交审核
    tzsh_tjsh = (By.CSS_SELECTOR,
                 '#app > div > div.main-container > section > div > div > div > div.col_right.el-col.el-col-12 > div.form-wrapper > form > div > div:nth-child(2) > div > button > span')
    # -----------------------------------------------图纸签收页面元素------------------------------------------------------------------------------
    # 登记
    tzqs_dj = (By.CSS_SELECTOR,
               '#app > div > div.main-container > section > div > div > div.col_left.el-col.el-col-12 > div.query > div.edit_btn > button.el-button.el-button--primary')
    # 图纸份数
    tzfs = (By.CSS_SELECTOR,
            '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-12 > div > div.form-wrap > form > div > div:nth-child(16) > div > div > div > input')
    # 每份张数
    mfzs = (By.CSS_SELECTOR,
            '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-12 > div > div.form-wrap > form > div > div:nth-child(17) > div > div > div > input')
    # 保存
    tzqs_bc = (By.CSS_SELECTOR,
               '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-12 > div > div:nth-child(1) > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--primary')
    # 推送
    tzqs_ts = (By.CSS_SELECTOR,
               '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-12 > div > div:nth-child(1) > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--default')
    # -----------------------------------------------工程估价页面元素------------------------------------------------------------------------------
    # 编辑
    gcgj_bj = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_left.el-col.el-col-24 > div.query > div.edit_btn > button')
    # 金额类型
    jelx = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > form > div > div:nth-child(9) > div > div > div > div.el-input.el-input--suffix > input')
    # 选择金额类型
    xzjelx = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]')
    # 估价
    gj = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > form > div > div:nth-child(10) > div > div > div.el-input.el-input--suffix > input')
    # 任务编号
    rwbh = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > form > div > div:nth-child(11) > div > div > div.el-input > input')
    # 保存
    gcgj_bc = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--default')
    # 推送
    gcgj_ts = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--primary')

    # -----------------------------------------------估价确认页面元素------------------------------------------------------------------------------
    # 编辑
    gjqr_bj = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_left.el-col.el-col-24 > div.query > div.edit_btn > button')
    # 保存
    gjqr_bc = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--default')
    # 推送
    gjqr_ts = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--primary')
    # -----------------------------------------------安装合同页面元素------------------------------------------------------------------------------
    # 登记
    azht_dj = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_left.el-col.el-col-24 > div.query > div.edit_btn > button.el-button.el-button--primary')
    # 合同金额
    htje = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(23) > div > div > div.el-input.el-input--suffix > input')
    # 签订日期
    qdrq = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div.form-wrap > form > div > div:nth-child(28) > div > div > div.el-date-editor.el-input.el-input--prefix.el-input--suffix.el-date-editor--datetime > input')
    # 保存
    azht_bc = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div:nth-child(1) > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--primary')
    # 推送
    azht_ts = (By.CSS_SELECTOR, '#app > div > div.main-container > section > div > div > div.col_right.el-col.el-col-24 > div > div:nth-child(1) > form > div.control-wrap.el-row > div.right.el-col.el-col-12 > div > button.el-button.el-button--default')




