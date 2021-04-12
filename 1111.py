import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.12306.cn/index/')

# 获取出发地元素
start_site=driver.find_element_by_id("fromStation")
start_site_text=driver.find_element_by_id("fromStationText")

# 设置出发地信息(使用web查找元素的方式，在进行js操作)，如果使用xpath定位元素的情况只能用这种方法，不能直接使用js语句
driver.execute_script("var start=arguments[0];var start_text=arguments[1];start.value='ZZF';start_text.value='郑州';",start_site,start_site_text)

# 设置目的地信息（使用js操作）
js='var to_site=document.getElementById("toStation");to_site.value="HZH";to_site_text=document.getElementById("toStationText");to_site_text.value="杭州";'
# 执行js语句
driver.execute_script(js)

# 设置出发日期
js='var start_time=document.getElementById("train_date");start_time.readOnly=false;start_time.value="2020-04-16";'
driver.execute_script(js)

# 获取查询按钮元素并点击
driver.find_element_by_id("search_one").click()
time.sleep(0.5)
# 获取句柄
handles=driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(0.5)
# 定位查找到的元素
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="menu-nav-hd"]')))
ele=driver.find_element_by_xpath('//a[@class="menu-nav-hd"]')
# 实例化ActionChains
ac=ActionChains(driver)
ac.move_to_element(ele)
ac.perform()
time.sleep(2)
driver.quit()