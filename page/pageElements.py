from selenium.webdriver.common.by import By


class PageElements:
    """管理所有页面元素"""

    # ---登录页面元素----
    # 用户名
    username = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/div/div/div[1]/input')
    # 密码
    password = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/div/div/input')
    # 登录按钮
    login_btn = (By.CLASS_NAME, 'el-button')
