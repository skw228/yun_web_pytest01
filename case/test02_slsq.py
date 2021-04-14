# 导包
import pytest
from base.page import Page
from utils import *


# 定义测试类
class TestSlsq:
    def setup_class(cls):
        cls.driver = DriverUtils.get_driver()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("受理申请")
    @pytest.mark.parametrize("dwmc, dz, ass, ywbm, gclx, czfs", load_yaml(GET_PATH + "/data/slsq.yaml"))
    def test_slsq(self, dwmc, dz, ass, ywbm, gclx, czfs):
        logging.info("---------------->执行受理申请")
        Page.get_homePage().test_int_slsq()
        Page.get_slsqPage().test_slsq(dz)
        # 断言
        assert is_exists_element(self.driver, ass)



