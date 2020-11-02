# 导包
import allure
import pytest
from page.login_page import LoginProxy
from utils import *


# 定义测试类
@pytest.mark.run(order=1)
class TestLogin:
    def setup_class(self):
        self.driver = DriverUtils.get_driver()
        self.login_proxy = LoginProxy()

    # 定义测试方法
    @allure.severity(allure.severity_level.CRITICAL)
    # @allure.step("登录测试")
    @pytest.mark.parametrize("username, password, expect, is_suc", load_json(GET_PATH + "/data/login.json"))
    def test_login(self, username, password, expect, is_suc):
        logging.info("---------------->执行登陆用例")
        self.login_proxy.test_login(username, password)
        # 断言
        assert is_exists_element(self.driver, '工作台')
