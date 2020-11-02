import logging
import time

import allure
from selenium.common.exceptions import NoSuchElementException
import app
from page.flow_page import FlowProxy
from page.set_page import SetProxy
from utils import DriverUtils, is_exists_element
import pytest


class TestAddGongcheng:
    def setup_class(cls):
        cls.driver = DriverUtils.get_driver()

    def teardown_class(cls):
        time.sleep(5)
        DriverUtils.quit_driver()

    def setup(self):
        self.set_proxy = SetProxy()
        self.flow_proxy = FlowProxy()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("添加工程类型")
    def test01_add_gongcheng(self):
        logging.info("---------------->执行添加工程类型用例")
        # 定义测试数据
        app.gongchengname = '测试一下_{}'.format(time.strftime('%d%H%M%S'))
        # 调用业务层方法
        self.set_proxy.add_gongcheng(app.gongchengname)
        # 断言
        assert is_exists_element(self.driver, '测试一下')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("添加出资方式")
    def test02_add_chuzi(self):
        logging.info("---------------->执行添加出资方式用例")
        # 定义测试数据
        app.chuziname = '测试一下_{}'.format(time.strftime('%d%H%M%S'))
        # 调用业务层方法
        self.set_proxy.add_chuzi(app.chuziname)
        # 断言
        assert is_exists_element(self.driver, '测试一下')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("添加关联设置")
    def test03_add_guanlian(self):
        logging.info("---------------->执行添加关联设置用例")
        # 调用业务层方法
        self.set_proxy.add_guanlian()
        # 断言
        assert is_exists_element(self.driver, f'{app.gongchengname}')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("添加流程")
    def test04_add_flow(self):
        logging.info("---------------->执行添加流程用例")
        # 调用业务层方法
        self.flow_proxy.add_flow()
        # 断言
        assert is_exists_element(self.driver, f'{app.gongchengname}')
