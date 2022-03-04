import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import request

my_chrome_options = Options()
my_chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=my_chrome_options)
currentHandle = driver.current_window_handle

driver.get("https://www.xuexi.cn/")


def tologin(dr, wait_time, by_way, identy):
    try:
        login_button = WebDriverWait(dr, wait_time).until(
            EC.presence_of_element_located((by_way, identy))
        )
        login_button.click()
        print("登录倒计时...")
        countdown(20)
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(currentHandle)
        driver.refresh()
        print("刷新倒计时...")
        countdown(5)
    except RuntimeError as message:
        print("登录失败")


def countdown(t):
    count = 0
    while count < t:
        count_now = t - count
        # print(count_now)
        time.sleep(1)  # sleep 1 second
        count += 1
    # print('done')


def get_cookie():
    dictCookies = driver.get_cookies()
    jsonCookies = json.dumps(dictCookies)
    with open('./xuexi_login_cookies.txt', 'w') as f:
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
    _currentHandle = driver.current_window_handle
    for webElement in my_points_card_titles:
        print("当前:")
        print(driver.window_handles)
        print(_currentHandle)
        # print('开始', webElement.get_attribute('innerHTML'), '积分查询')
        driver.switch_to.window(_currentHandle)
        # driver.refresh()
        # time.sleep(6)
        # notify_result(idx, webElement.get_attribute('innerHTML'))
        if counts_reach(my_points_card_texts[idx]):
            print("恭喜，", webElement.get_attribute('innerHTML'), "得分今日份圆满啦！")
        else:
            notify_result(idx, webElement.get_attribute('innerHTML'))
        idx = idx + 1


"""
积分分类
1，首页读文章或者视频
2、每日答题
3、每周答题
4、专项答题
"""


def get_point_tab(s):
    score = s.get_attribute('innerHTML').split('/')
    # score = score.replace('分')
    print(score)
    return score


def counts_reach(s):
    score = s.get_attribute('innerHTML').split('/')
    if score[1] == score[0]:
        return True
    else:
        return False


def my_point_01_read_articles(msg):
    print('读取文章方法', msg)
    read_hot_index()
    driver.switch_to.window(driver.window_handles[-1])
    # 积分明细
    my_points_card_texts = driver.find_elements(By.XPATH,
                                                '/html/body//div[@class="my-points-content"]//div[@class="my-points-card"]//div[@class="my-points-card-text"]')
    if counts_reach(my_points_card_texts[1]):
        print("恭喜，你的文章阅读得分今日份圆满啦！")
    else:
        _currentHandle = driver.current_window_handle
        read_content_index()


def read_hot_index():
    driver.switch_to.window(currentHandle)
    # 轮播图列表
    slick_slides = driver.find_elements(By.XPATH,
                                        '/html/body//section[@id="0f74"]//div[@class="slick-list"]//div[@class="slick-track"]//div[@class="slick-slide" or @class="slick-slide slick-active slick-current"]')
    # 左键
    # left_button = driver.find_elements(By.XPATH, '/html/body//section[@id="0f74"]//div[@class="slick-arrow slick-prev arrow prev-arrow"]')
    # 右键
    right_button = driver.find_elements(By.XPATH,
                                        '/html/body//section[@id="0f74"]//div[@class="slick-arrow slick-next arrow next-arrow"]')
    _idx = 0
    while _idx < len(slick_slides) - 1:
        slick_slides[_idx].click()
        driver.switch_to.window(driver.window_handles[-1])
        countdown(3)
        # 文章div
        article_div = driver.find_elements(By.XPATH,
                                           '//html/body//div[@class ="grid-cell"]//div[@class ="render-detail-article"]')
        # 视频div
        video_div = driver.find_elements(By.XPATH,
                                         '//html/body//div[@class ="grid-cell"]//div[@class ="videoSet-article-wrap"]')

        if len(article_div) > 0:
            temp_height = 0
            while True:
                # 循环将滚动条下拉
                driver.execute_script("window.scrollBy(0,1)")
                # sleep一下让滚动条反应一下
                # countdown(10)
                # 获取当前滚动条距离顶部的距离
                check_height = driver.execute_script(
                    "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
                # 如果两者相等说明到底了
                if check_height == temp_height:
                    countdown(40)
                    break
                temp_height = check_height
                print(check_height)

        # print(video_div)
        # print(len(video_div))
        if len(video_div) > 0:
            # 视频div
            # video_div = driver.find_elements(By.XPATH, '//html/body//div[@class ="grid-cell"]//div[contains(@class,"pause")]')
            countdown(60)
        driver.close()
        driver.switch_to.window(currentHandle)
        right_button[0].click()
        _idx = _idx + 1


def read_content_index():
    print("TODO read content")
    driver.switch_to.window(currentHandle)
    # 中间内容文章
    content_articles = driver.find_elements(By.XPATH,
                                            '//section[@id="d6df"]//div[@class ="Iuu474S1L6y5p7yalKQbW grid-cell"]')
    if len(content_articles) < 0:
        print('获取中间文章错误')
    _idx = 0
    while _idx < len(content_articles):
        content_articles[_idx].click()
        driver.switch_to.window(driver.window_handles[-1])
        countdown(3)
        # 文章div
        article_div = driver.find_elements(By.XPATH,
                                           '//html/body//div[@class ="grid-cell"]//div[@class ="render-detail-article"]')
        # 视频div
        video_div = driver.find_elements(By.XPATH,
                                         '//html/body//div[@class ="grid-cell"]//div[@class ="videoSet-article-wrap"]')

        if len(article_div) > 0:
            temp_height = 0
            while True:
                # 循环将滚动条下拉
                driver.execute_script("window.scrollBy(0,1)")
                # sleep一下让滚动条反应一下
                # countdown(10)
                # 获取当前滚动条距离顶部的距离
                check_height = driver.execute_script(
                    "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
                # 如果两者相等说明到底了
                if check_height == temp_height:
                    countdown(50)
                    break
                temp_height = check_height
                # print(check_height)
            # print(video_div)
            # print(len(video_div))
            if len(video_div) > 0:
                # 视频div
                # video_div = driver.find_elements(By.XPATH, '//html/body//div[@class ="grid-cell"]//div[contains(@class,"pause")]')
                countdown(60)
            driver.close()
            driver.switch_to.window(currentHandle)
        _idx = _idx + 1


def my_point_02_read_video(msg):
    print("看视频", msg)
    _currentHandle = driver.current_window_handle
    driver.switch_to.window(currentHandle)
    videos_link = driver.find_elements(By.XPATH,
                                       '/html/body//section[@id="6a61"]//section[@class="_3GhgGH8Y4Zh8H0uBP5aUMD _3mVsbsHWKWuZwBS5zIrFO9"]//div[@class="_1PcbELBKVoVrF5XKNSE_SF"]')
    # print(driver.window_handles)
    videos_link[0].click()
    # print(driver.window_handles)
    countdown(5)
    # print(driver.window_handles)
    # print(driver.current_window_handle)
    temp_wh = driver.window_handles[-1]
    driver.switch_to.window(temp_wh)
    # print(driver.current_window_handle)
    videos_link_details = driver.find_elements(By.XPATH,
                                               '/html/body//section[@class="_3GhgGH8Y4Zh8H0uBP5aUMD _3mVsbsHWKWuZwBS5zIrFO9"]//div[@class="oSnRgpdW2BnrDruxKh9We _3mVsbsHWKWuZwBS5zIrFO9"]//div[@class="Iuu474S1L6y5p7yalKQbW grid-cell"]')
    _idx = 0
    # print(len(videos_link_details))
    while _idx < len(videos_link_details):
        videos_link_details[_idx].click()
        countdown(3)
        driver.switch_to.window(driver.window_handles[-1])
        # 文章div
        article_div = driver.find_elements(By.XPATH,
                                           '//html/body//div[@class ="grid-cell"]//div[@class ="render-detail-article"]')
        # 视频div
        video_div = driver.find_elements(By.XPATH,
                                         '//html/body//div[@class ="grid-cell"]//div[@class ="videoSet-article-wrap"]')

        if len(article_div) > 0:
            temp_height = 0
            while True:
                # 循环将滚动条下拉
                driver.execute_script("window.scrollBy(0,1)")
                # sleep一下让滚动条反应一下
                # countdown(2)
                # 获取当前滚动条距离顶部的距离
                check_height = driver.execute_script(
                    "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
                # 如果两者相等说明到底了
                if check_height == temp_height:
                    countdown(40)
                    break
                temp_height = check_height
                # print(check_height)

        # print(video_div)
        # print(len(video_div))
        if len(video_div) > 0:
            # 视频div
            # video_div = driver.find_elements(By.XPATH, '//html/body//div[@class ="grid-cell"]//div[contains(@class,"pause")]')
            countdown(60)
        driver.close()
        # driver.switch_to.window(_currentHandle)
        # driver.close()
        driver.switch_to.window(temp_wh)
        _idx = _idx + 1


def my_point_03_read_visual(msg):
    print("看视频长度", msg)
    driver.switch_to.window(currentHandle)
    # 视听
    video_div = driver.find_elements(By.XPATH,
                                     '/html/body//div[@class="menu"]//div[@class="menu-row"][2]//a[2]')
    video_div[0].click()
    driver.switch_to.window(driver.window_handles[-1])
    countdown(3)
    # 视听
    channel_one = driver.find_elements(By.XPATH,
                                       '/html/body//section[@class="_3GhgGH8Y4Zh8H0uBP5aUMD _3mVsbsHWKWuZwBS5zIrFO9 _19bO69jmSWdAdrKAzSJzl7"]/div/div/div/div[1]/div[1]')

    channel_one[0].click()
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    countdown(60)
    # 试听链接
    channel_one_links = driver.find_elements(By.XPATH, '/html/body//div[@class="grid-gr"]//div[@class="Iuu474S1L6y5p7yalKQbW grid-cell"]')

    _idx = 0
    _currentH = driver.current_window_handle
    print("长度")
    print(len(channel_one_links))
    while _idx < len(channel_one_links):
        print(_idx)
        driver.switch_to.window(_currentH)
        channel_one_links[_idx].click()
        driver.switch_to.window(driver.window_handles[-1])
        countdown(60)
        driver.close()
        _idx = _idx + 1
    # for channel_one_link_webElement in channel_one_links:
    #     driver.switch_to.window(_currentH)
    #     channel_one_link_webElement[_idx].click
    #     driver.switch_to.window(driver.window_handles[-1])
    #     countdown(5)
    #     driver.close()


def my_point_04_answer_days(msg):
    print('每日答题', msg)


def my_point_05_answer_weeks(msg):
    print('每周答题', msg)


def my_point_06_answer_groups(msg):
    print('专项答题', msg)


def my_point_05_others(msg):
    print('特殊', msg)


def notify_result(num, msg):
    numbers = {
        0: my_point_05_others,
        1: my_point_01_read_articles,
        2: my_point_02_read_video,
        3: my_point_03_read_visual,
        4: my_point_04_answer_days,
        5: my_point_05_answer_weeks,
        6: my_point_06_answer_groups
    }

    method = numbers.get(num, my_point_05_others)
    if method:
        method(msg)


# 跳转登录
# tologin(driver, 10, By.CLASS_NAME, "login-icon")
# 获取cookie
# time.sleep(10)
# get_cookie()
# cookie登录
login_with_cookies()
print("跳转积分页倒计时....")
countdown(5)
get_counts()
get_points_details()
# driver.close()
