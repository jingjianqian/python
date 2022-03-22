from ast import arguments
from operator import truediv
from re import A
import time
import json
from unittest import BaseTestSuite

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


my_chrome_options = Options()
# my_chrome_options.add_argument('--headless')
my_chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(options=my_chrome_options)
currentHandle = driver.current_window_handle

#填报地址
driver.get("https://pm.ucap.com.cn")

#登录状态
LOGIN_STATUS = False

#登录方法
def tologin(dr, wait_time, by_way, identy):
    global LOGIN_STATUS 
    try:
        #等待登录按钮出来后
        login_button = WebDriverWait(dr, wait_time).until(
            EC.presence_of_element_located((by_way, identy))
        )
        username = driver.find_elements(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/span[1]/span[1]/input[1]')
        password = driver.find_elements(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[1]/span[1]/span[1]/input[1]')
        username[0].send_keys("jingjq")
        password[0].send_keys("jjq*#%0615")
        login_button.click()
        LOGIN_STATUS = True
    except RuntimeError as message:
        LOGIN_STATUS = False
        print("登录失败")

#跳转到日志填写页面
def toLogPage(xpathValueList):
    print('开始跳转到日志填写页面')
    if LOGIN_STATUS is True:
        try: 
            login_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"))
            )
            login_button.click()
        except RuntimeError as errorMessage:
            print("跳转日志页面失败！")
    else:
        print('登录状态异常！！')

def logsCount():
    print("开始日志统计功能")

tologin(driver,10,'xpath','/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[4]/div[1]/div[1]/span[1]/div[1]/div[1]/button[1]')
toLogPage(['/html[1]/body[1]/div[1]/section[1]/aside[1]/div[1]/ul[1]/li[6]/div[1]','/html[1]/body[1]/div[1]/section[1]/aside[1]/div[1]/ul[1]/li[6]/ul[1]/li[1]/a[1]'])
time.sleep(5)
driver.close()

