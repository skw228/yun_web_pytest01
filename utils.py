# 导包
import os
import json
import time
import allure
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import logging
from logging import handlers
import pymysql
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

GET_PATH = os.path.abspath(os.path.dirname(__file__))


# 1.根据文本判断元素是否存在-公用方法
def is_exists_element(driver, text):
    xpath_string = "//*[contains(text(),'{}')]".format(text)
    try:
        aaa = driver.find_element_by_xpath(xpath_string)
        logging.info("成功！")
    except Exception as e:
        screen_image()
        aaa = False
        # NoSuchElementException('no find text is {} element'.format(text))
        logging.info("失败！no find text is {} element".format(text))
    return aaa


# 2.浏览器驱动工具类
class DriverUtils:
    __driver = None
    __key = True

    @classmethod
    def get_driver(cls):
        if not cls.__driver:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(3)
            cls.__driver.get("http://10.200.6.159:8888/project/login")
            return cls.__driver
        else:
            return cls.__driver

    # 修改开关的方法
    @classmethod
    def change_key(cls, key):
        cls.__key = key

    # 关闭浏览器驱动
    @classmethod
    def quit_driver(cls):
        if cls.__driver and cls.__key:
            cls.__driver.quit()
            cls.__driver = None


# 定义读取json测试数据并且组织成parameterized.expand所要求的数据格式的函数
# 3.定义读取数据的函数
def load_json(file_path):
    test_dict = []
    with open(file_path, encoding="utf-8")as f:
        json_str = json.load(f)
        for i in json_str.values():
            test_dict.append(list(i.values()))
        print(test_dict)
    return test_dict


# 4.编写初始化日志的代码
# 1 首先定义一个初始化日志的函数
def init_logging():
    # 2 在函数中，设置日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.INFO)
    # 4 设置控制台处理器
    sh = logging.StreamHandler()
    # 5 设置文件处理器（文件处理的作用是设置保存日志的文件地址的：需要使用项目根目录定位到日志文件）
    log_path = GET_PATH + "/log/yun.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path,
                                                   when='M',  # 分钟
                                                   interval=1,  # 间隔
                                                   backupCount=3,  # 保留
                                                   encoding='utf-8')
    # 6 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 7 将格式化器添加到文件处理器和控制台处理当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 8 将文件处理器和控制台处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)


# 5.截图
def screen_image(name="截图"):
    png_name = "./screen" + os.sep + "%s.png" % time.strftime('%Y-%m-%d-%H-%M-%S')
    # 截图
    DriverUtils.get_driver().get_screenshot_as_file(png_name)
    # 打开截图放到测试报告
    with open(png_name, "rb") as f:
        allure.attach(f.read(), name, attachment_type=allure.attachment_type.PNG)


# 6.数据库验证
def sql(sql):
    # 建立连接，建立连接时要设置自动提交事务开发，并设置为True
    conn = pymysql.connect(host='10.200.6.159',
                           user='panggu',
                           password='123456',
                           database='books',
                           autocommit=True,
                           port=3306,
                           charset='utf8')
    # 获取游标
    cursor = conn.cursor()
    # 执行SQL
    cursor.execute(sql)
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


# 7.切换窗口
def to_swtich():
    handles = DriverUtils.get_driver().window_handles
    DriverUtils.get_driver().switch_to.window(handles[-1])


# 8.显示等待
def wait(element):
    return WebDriverWait(DriverUtils.get_driver(), 10, 1.0).until(lambda x: x.find_element(*element))


# 9.获取弹出框信息
def get_msg():
    time.sleep(2)
    msg = DriverUtils.get_driver().find_element_by_css_selector(".layui-layer-content").text
    print(msg)
    return msg


# 10.获取alert弹出框信息并关闭
def get_alert():
    time.sleep(2)
    alert = DriverUtils.get_driver().switch_to.alert
    msg = alert.text  # 获取弹出框文本信息
    alert.accept()  # 接受
    print(msg)
    return msg


# 11.获取toast
def get_toast(mess):
    toast_xpath = (By.XPATH, f'//*[text()="{mess}"]')
    return wait(toast_xpath)


# 12.frame切换
def to_frame(ele):
    DriverUtils.get_driver().switch_to.frame(ele)


# 13.窗口滑动
def move_windows(x, y):
    js = f"window.scrollTo({x},{y})"
    DriverUtils.get_driver().execute_script(js)


# 14.公用选择下拉框选项
def select_option(ele1, ele2, target_option):
    # 点击控件
    wait(ele1).click()
    # 是否找到的标识
    is_element = False
    # 获取所有选项
    option_list = DriverUtils.get_driver().find_elements(ele2)
    # 遍历选项文本并和目标选项进行对比
    for i in option_list:
        # 如果相等则点击
        if i.text == target_option:
            i.click()
            is_element = True
            break
        # 不相等则鼠标悬浮到该选项并按下按键
        else:
            ActionChains(DriverUtils.get_driver()).move_to_element(i).send_keys(Keys.DOWN).perform()
            is_element = False
    # 如果最后都没有找到选项，则抛出提示
    if is_element is False:
        NoSuchElementException(f"can not find {target_option} option")
