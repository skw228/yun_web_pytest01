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

GET_PATH = os.path.abspath(os.path.dirname(__file__))


# 根据文本判断元素是否存在-公用方法
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


# 定义浏览器驱动工具类
class DriverUtils:
    __driver = None
    __key = True

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(3)
            cls.__driver.get("http://10.200.6.159:8888/project/login")
        return cls.__driver

    # 修改开关的方法
    @classmethod
    def change_key(cls, key):
        cls.__key = key

    # 关闭浏览器驱动
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None and cls.__key:
            cls.__driver.quit()
            cls.__driver = None


# 定义读取json测试数据并且组织成parameterized.expand所要求的数据格式的函数
# 1.定义读取数据的函数
def load_json(file_path):
    test_dict = []
    with open(file_path, encoding="utf-8")as f:
        json_str = json.load(f)
        for i in json_str.values():
            test_dict.append(list(i.values()))
        print(test_dict)
    return test_dict


# 编写初始化日志的代码
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


# 截图
def screen_image(name="截图"):
    png_name = "./image" + os.sep + "%d.png" % int(time.time())
    # 截图
    DriverUtils.get_driver().get_screenshot_as_file(png_name)
    # 打开截图放到测试报告
    with open(png_name, "rb") as f:
        allure.attach(f.read(), name, attachment_type=allure.attachment_type.PNG)


# 数据库验证
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
