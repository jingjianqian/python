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


def tologin(dr, wait_time, by_way, identy):
    try:
        login_button = WebDriverWait(dr, wait_time).until(
            EC.presence_of_element_located((by_way, identy))
        )
        login_button.click()
    except RuntimeError as message:
        print("登录失败")


def get_cookie():
    time.sleep(15)
    dictCookies = driver.get_cookies()
    jsonCookies = json.dumps(dictCookies)
    with open('xuexi_login_cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookie save success！')


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


def login_with_cookies():
    with open('xuexi_login_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        if check_expiry(cookie.get('expiry')) == 'True':
            print(cookie.get('name'), '超时了')
            # TODO 增加消息推送
            print('cookie超时，需要重新获取cookie')
            break
        else:
            print(cookie.get('name'), '未超时')

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
        driver.add_cookie(cookie_dict)
    driver.refresh()
    print('按道理说应该成功了呀')


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
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
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
    my_points_content = driver.find_elements(By.XPATH,
                                             '/html/body//div[@class="my-points-content"]//div[@class="my-points-card"]')
    # 积分主题
    my_points_card_titles = driver.find_elements(By.XPATH,
                                                 '/html/body//div[@class="my-points-content"]//div[@class="my-points-card"]//p[@class="my-points-card-title"]')
    # 积分明细
    my_points_card_texts = driver.find_elements(By.XPATH,
                                                '/html/body//div[@class="my-points-content"]//div[@class="my-points-card"]//div[@class="my-points-card-text"]')
    # 主题跳转获取积分按钮
    my_points_card_buttonboxs = driver.find_elements(By.XPATH,
                                                     '/html/body//div[@class="my-points-content"]//div[@class="my-points-card"]//div[@class="buttonbox"]')
    # 开始处理各主题积分
    if len(my_points_content) == len(my_points_card_titles) == len(my_points_card_texts) == len(
            my_points_card_buttonboxs):
        print('积分面板获取正常')
    else:
        print('积分面板获取异常')

    idx = 0
    for webElement in my_points_card_titles:
        # print('开始', webElement.get_attribute('innerHTML'), '积分查询')
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        notify_result(idx, webElement.get_attribute('innerHTML'))
        idx = idx + 1


"""
积分分类
1，首页读文章或者视频
2、每日答题
3、每周答题
4、专项答题
"""


def my_point_01_read_articles(msg):
    print('读取文章方法', msg)
    driver.switch_to.window(currentHandle)
    # 轮播图列表
    slick_slides = driver.find_elements(By.XPATH, '/html/body//section[@id="0f74"]//div[@class="slick-list"]//div[@class="slick-track"]//div[@class="slick-slide" or @class="slick-slide slick-active slick-current"]')
    # 左键
    left_button = driver.find_elements(By.XPATH, '/html/body//section[@id="0f74"]//div[@class="slick-arrow slick-prev arrow prev-arrow"]')
    # 右键
    right_button = driver.find_elements(By.XPATH, '/html/body//section[@id="0f74"]//div[@class="slick-arrow slick-next arrow next-arrow"]')
    _idx = 0
    while _idx < len(slick_slides)-1:
        time.sleep(2)
        right_button[0].click()
        _idx = _idx + 1

    print(_idx)


def my_point_02_answer_days(msg):
    print('每日答题', msg)


def my_point_03_answer_weeks(msg):
    print('每周答题', msg)


def my_point_04_answer_groups(msg):
    print('专项答题', msg)


def my_point_05_others(msg):
    print('特殊', msg)


def notify_result(num, msg):
    numbers = {
        0: my_point_05_others,
        1: my_point_01_read_articles,
        2: my_point_01_read_articles,
        3: my_point_01_read_articles,
        4: my_point_02_answer_days,
        5: my_point_03_answer_weeks,
        6: my_point_04_answer_groups
    }

    method = numbers.get(num, my_point_05_others)
    if method:
        method(msg)


# 跳转登录
# tologin(driver, 10, By.CLASS_NAME, "login-icon")
# 获取cookie
# get_cookie()
# cookie登录
login_with_cookies()
time.sleep(5)
get_counts()
get_points_details()
driver.close()
