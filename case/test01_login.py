# 导包
import pytest
from base.page import Page
from utils import *


# 定义测试类
@pytest.mark.run(order=1)
class TestLogin:
    def setup_class(self):
        self.driver = DriverUtils.get_driver()

    # def teardown_class(cls):
    #     time.sleep(5)
    #     DriverUtils.quit_driver()

    # 定义测试方法
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("登录测试")
    @pytest.mark.parametrize("username, password, ass", load_yaml(GET_PATH + "./data/login.yaml"))
    def test_login(self, username, password, ass):
        logging.info("---------------->执行登陆用例")
        # self.login_proxy.test_login(username, password)
        Page.get_loginPage().test_login(username, password)
        # 断言
        assert is_exists_element(self.driver, ass)
