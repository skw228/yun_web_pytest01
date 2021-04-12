# 导包
import allure
import pytest
from page.slsq_page import SlsqProxy
from page.home_page import HomeProxy
from utils import *


# 定义测试类
@pytest.mark.run(order=1)
class TestLogin:
    def setup_class(cls):
        cls.driver = DriverUtils.get_driver()

    def teardown_class(cls):
        time.sleep(5)
        DriverUtils.quit_driver()

    def setup(self):
        self.home_proxy = HomeProxy()
        self.slsq_proxy = SlsqProxy()

    # 定义测试方法
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("进入受理申请")
    def test_int_slsq(self):
        logging.info("---------------->进入受理申请")
        self.home_proxy.test_int_slsq()
        # 断言
        assert is_exists_element(self.driver, "受理申请")

    @allure.severity(allure.severity_level.CRITICAL)
    # @allure.step("受理申请")
    @pytest.mark.parametrize("dwmc, lxr, lxdh, dz, ass", load_json(GET_PATH + "/data/slsq.json"))
    def test_slsq(self, dwmc, lxr, lxdh, dz, ass):
        logging.info("---------------->执行受理申请")
        self.slsq_proxy.test_slsq(dz)
        # 断言
        assert is_exists_element(self.driver, ass)
