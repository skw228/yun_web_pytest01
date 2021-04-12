# -*- coding: utf-8 -*-
# @Author : ShanMin
# @File : eee_Windows弹框处理.py
# @Project: bbb
# @CreateTime : 2020/12/24 12:12:28
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 需要下载 pypiwin32
import win32con
import win32gui

import time
def upload_file(browser: str, file: str):
    browser_type = {
        "firefox": "文件上传",
        "chrome": "打开",
        "ie": "选择要加载的文件"
    }
    time.sleep(2)
    dialog = win32gui.FindWindow("#32770", browser_type[browser])  # 谷歌浏览器为”文件上传“，谷歌为”打开“

    combobox_ex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)

    combobox = win32gui.FindWindowEx(combobox_ex32, 0, 'ComboBox', None)

    edit = win32gui.FindWindowEx(combobox, 0, 'Edit', None)

    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)

    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file)

    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)



if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(r'E:\python3\ccc\111\ddd.html')
    upload_element = driver.find_element_by_xpath('//*[@id="upload_file"]')
    action = ActionChains(driver)
    action.move_to_element(upload_element).click().perform()
    action.release()
    time.sleep(3)  # 为了看效果
    upload_file('chrome', r'C:\Users\4087\Desktop\测试规范\测试分析模板.doc')
