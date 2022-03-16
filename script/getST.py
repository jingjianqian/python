import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import request

my_chrome_options = Options()
my_chrome_options.add_argument('--headlesss')
driver = webdriver.Chrome(options=my_chrome_options)
currentHandle = driver.current_window_handle

driver.get("https://www.xuexi.cn/")


def login_with_cookies():
    with open('./xuexi_login_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    # print(listCookies)
    for cookie in listCookies:
        if check_expiry(cookie.get('expiry')) == 'True':
            print(cookie.get('name'), '超时了')
            # TODO 增加消息推送
            print('cookie超时，需要重新获取cookie')
            break
        else:
            pass
            # print(cookie.get('name'), '未超时')

        cookie_dict = {
            'domain': cookie.get('domain'),
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        # print(cookie_dict)
        driver.add_cookie(cookie_dict)
    driver.refresh()
    print('按道理说应该成功了呀')


def check_expiry(expiry):
    # 当前时间
    time_now = int(round(time.time() * 1000))
    # print(time_now)
    # cookie过期时间
    time_int = int(round(expiry * 1000))
    # print(time_int)
    if time_now < time_int:
        return False
    else:
        return True
    # format_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_int / 1000))
    # print(format_time)

    pass


def countdown(t):
    count = 0
    while count < t:
        count_now = t - count
        # print(count_now)
        time.sleep(1)  # sleep 1 second
        count += 1
    # print('done')


# 获取积分
def get_counts():
    # 查找是否还有登录按钮
    if_login = driver.find_elements(
        By.CLASS_NAME,
        "login-icon")

    if len(if_login) > 0:
        print("浏览器未登录成功!")
        return False
    else:
        print("检测到已经登录成功，准备跳转我的积分，，")

    print("开始跳转我的积分")
    # 我的积分跳转按钮
    my_count_link = driver.find_elements(
        By.XPATH,
        '/html/body//div[@id="page-main"]//div[@class="_2sd_CKPqo9yoERxZnUP_PX"]//div[contains(text(),"我的积分")]'
    )
    if len(my_count_link) > 0:
        print('找到我的积分按钮', type(my_count_link), my_count_link[0])
    # print(my_count_link)
    else:
        print('获取我的积分按钮失败。')
    my_count_link[0].click()
    time.sleep(10)
    # print(driver.window_handles)
    # print(driver.window_handles[-1])
    # print(driver.current_window_handle)
    driver.switch_to.window(driver.window_handles[-1])
    # driver.switch_to.window(driver.window_handles[-1])
    try:
        today_points = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body//span[@class="my-points-points"]'))
        )
        print('今日已获取积分', today_points.text)
    except RuntimeError as message:
        print("登录失败")
    pass


def get_points_details():
    # 积分面板
    my_points_content = driver.find_elements(By.XPATH, '/html/body//div[@class="my-points-content"]//div[@class="my-points-card"]')
    # 积分主题
    my_points_card_titles = driver.find_elements(By.XPATH, '/html/body//div[@class="my-points-content"]//div[@class="my-points-card"]//p[@class="my-points-card-title"]')
    # 积分明细
    my_points_card_texts = driver.find_elements(By.XPATH,  '/html/body//div[@class="my-points-content"]//div[@class="my-points-card"]//div[@class="my-points-card-text"]')
    # 主题跳转获取积分按钮
    my_points_card_buttonboxs = driver.find_elements(By.XPATH,  '/html/body//div[@class="my-points-content"]//div[@class="my-points-card"]//div[@class="buttonbox"]')
    # 开始处理各主题积分
    if len(my_points_content) == len(my_points_card_titles) == len(my_points_card_texts) == len(my_points_card_buttonboxs):
        print('积分面板获取正常')
    else:
        print('积分面板获取异常')
    pass


login_with_cookies()
print("跳转积分页倒计时....")
countdown(5)
get_counts()
get_points_details()
