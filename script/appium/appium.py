from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, random
from MyAutomation import MyAutomation

class DongFangTouTiao(MyAutomation):

    def __init__(self, APP_PACKAGE, APP_ACTIVITY):

        # floaticon
        self.coin_float_ele = 'cn.youth.news:id/mm'#mm 新   m1 老

        # read
        self.subject = '//*[@text="健康"]'
        self.list_item_ele = 'cn.youth.news:id/z2'#z2 新   a_r 老

        # video
        self.tryplay_ele = 'cn.youth.news:id/pd'# pd 新
        # 视频列表play键
        self.tryplay_btn_ele = 'cn.youth.news:id/ab2'# ml 新
        # self.time_text_ele = 'cn.youth.news:id/acc'


        # minivideo
        self.trysmplay_ele = 'cn.youth.news:id/oh' #on 新
        self.trysmplay_item_ele = 'cn.youth.news:id/mi'#m4 新

        # 全局
        # 推送新闻框的忽略按钮
        self.ignore_push_news = 'com.songheng.eastnews:id/ea'
        # 升级框关闭叉叉
        self.close_update = 'com.songheng.eastnews:id/pj'

        super().__init__(APP_PACKAGE, APP_ACTIVITY)


    # minivideo
    def smallvideo(self, interval):
        video = self.wait.until(EC.presence_of_element_located((By.ID, self.trysmplay_ele)))
        video.click()
        print('点击底部菜单:点击短视频...')

        time.sleep(3)
        video2 = self.wait.until(EC.presence_of_element_located((By.ID, self.trysmplay_item_ele)))
        video2.click()

        try:
            start = time.time()
            count = 0
            while True:
                time.sleep(random.randint(6, 12))
                self.swipeUp()
                end = start + interval
                now = time.time()
                count += 1
                print('page:' + str(count))
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))
                if now >= end:
                    print('结束小视频循环')
                    break
        except:
            print('打开短视频失败')

    # video
    def video(self, interval):
        # video = self.wait.until(EC.presence_of_element_located((By.ID, self.tryplay_ele)))
        # video.click()
        print('点击底部菜单:视频...')
        time.sleep(random.randint(5, 7))
        t = 0
        start = time.time()
        while True:
            try:
                content = self.driver.find_elements_by_id(self.tryplay_btn_ele)
                print('视频数量', len(content))
                for i in range(len(content)):
                    print('第{}次进入循环.. 点击第{}视频'.format(t, i + 1))
                    content[i].click()
                    try:
                        time.sleep(random.randint(50, 60))
                        # 返回
                        self.driver.press_keycode(4)
                    except:
                        print('无coin_float，应退回列表')
            except:
                print('没有可播放视频')
            t += 1
            now = time.time()
            print('page:' + str(t))
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))

            for i in range(random.randint(2, 3)):
                time.sleep(random.randint(1, 3))
                print('列表向下滑动')
                self.swipeUp()

            end = start + interval
            now = time.time()
            if now >= end:
                print('结束视频循环')
                break

    # read
    def read_article(self, interval):
        time.sleep(3)
        suject = self.wait.until(EC.presence_of_element_located((By.XPATH, self.subject)))
        suject.click()
        # self.swipeDown()
        time.sleep(3)

        start = time.time()
        while True:
            try:
                articles = self.wait.until(EC.presence_of_all_elements_located((By.ID, self.list_item_ele)))
                print('新闻数量', len(articles))
                for article in articles:
                    try:
                        article.click()
                        print('进入新闻')
                        try:
                            # 新闻
                            coin_float = self.wait.until(EC.presence_of_element_located((By.ID, self.coin_float_ele)))
                            if coin_float == 'null':
                                print('此为广告，应直接退出')
                            else:
                                for i in range(2):
                                    time.sleep(random.randint(4, 6))
                                    self.swipeUp()

                                try:
                                    more = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@text="查看全文，奖励更多"]')))
                                    more.click()
                                    print('点击查看更多')
                                    self.swipeUp()
                                except:
                                    aaa=0

                                for i in range(random.randint(2, 3)):
                                    time.sleep(random.randint(4, 6))
                                    self.swipeUp()

                                # for i in range(random.randint(2, 6)):
                                #     time.sleep(random.randint(3, 6))
                                #     self.swipeDown()

                        except :
                            print('在详情页报错，应直接退出')

                        # 返回
                        self.driver.press_keycode(4)
                        print('退出详情,回到列表1')


                    except:
                        print('退出详情,回到列表2')
                        # self.swipeUp()
            except:
                print('报错')


            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


            # if random.randint(2, 6) > 4:
            #     suject = self.wait.until(EC.presence_of_element_located((By.XPATH, self.subject)))
            #     suject.click()
            #     time.sleep(random.randint(2, 3))
            #     self.swipeUp()
            # else:
            for i in range(random.randint(2, 3)):
                time.sleep(random.randint(1, 3))
                print('列表向下滑动')
                try:
                    self.swipeUp()
                except:
                    print('滑动异常')


            end = start + interval
            now = time.time()
            if now >= end:
                print('结束新闻循环')
                break
            else:
                print('未到结束时间')





    # 入口函数
    def main(self):
        print('打开 {} App ...'.format('dftt'))
        # func_list = [ 'read_article', 'video']  # 新闻阅读，小视频，视频三个方法随机
        func_list = ['read_article']
        for i in range(12):
            exp = 'self.{}({})'.format(random.choice(func_list), random.randint(6000, 8000))
            print(exp)
            eval(exp)
            print('App {} 今日任务完成！'.format('dftt'))
            # home键
            self.driver.press_keycode(3)
            self.driver.close()



#zhongqing
qutoutiao_appPackage = 'cn.youth.news'
qutoutiao_appActivity = 'cn.youth.news.ui.SplashActivity'


if __name__ == '__main__':
    qutoutiao = DongFangTouTiao(qutoutiao_appPackage, qutoutiao_appActivity)
    qutoutiao.main()