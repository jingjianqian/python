"""阅读文章"""
import re
import time

import uiautomator2.exceptions as u2exceptions
from uiautomator2.exceptions import XPathElementNotFoundError, UiObjectNotFoundError

from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class ReadArticles:
    def __init__(self, device, article_round) -> None:
        self.setting = Settings()
        self.device = device
        self.readArticles = 0
        self.haveFinishDaily = False
        self.round = article_round
        self.common = Common(self.device)

    def start(self):
        """
        1 启动app
        """
        print("==========================>开始阅读文章=========================")
        print("启动app中")

        self.common.start_app()
        """
        2 跳转到观看文章菜单开始观看文章
        """
        restart = 0
        while self.readArticles < self.round:
            if restart > self.setting.restartTimes:
                break
            try:
                for i in range(3):
                    print("跳转到文章TAB")
                    self.device(resourceId="cn.youth.news:id/a7h").click()
                    time.sleep(2)
                    temp_articles = self.device.xpath('//*[@resource-id="cn.youth.news:id/a5f"]/android.widget.LinearLayout').all()
                    if len(temp_articles) > 0:
                        for article in temp_articles:
                            article.click()
                            time.sleep(3)
                            self.readArticles += 1
                            if self.read_article() is False:
                                self.start()
                            if self.device(resourceId="cn.youth.news:id/rb").exists:
                                self.device(resourceId="cn.youth.news:id/rb").click()
                                time.sleep(0.2)
                                self.readArticles += 1
                            elif self.device(resourceId="cn.youth.news:id/d5").exists:
                                self.device(resourceId="cn.youth.news:id/d5").click()
                                time.sleep(0.2)
                            else:
                                print("返回异常")
                                restart += 1
                                self.start()
                    else:
                        restart += 1
                        self.start()
            except UiObjectNotFoundError:
                print("观看文章出现错误，重启再来")
                restart += 1
                self.start()
        #
        # if self.have_finish_daily() is True:
        #     return True
        # # 开始阅读文章
        # # 启动app
        # Common(self.device).start_app('cn.youth.news')
        # while self.haveFinishDaily is not True:
        #     # 阅读文章
        #     try:
        #         print("阅读文章")
        #         # 网络加载失败时监听器
        #         temp_articles = self.device.xpath('//*[@resource-id="cn.youth.news:id/a5f"]/android.widget.LinearLayout').all()
        #         if len(temp_articles) > 0:
        #             for article in temp_articles:
        #                 article.click()
        #                 time.sleep(1)
        #                 if self.read_article() is False:
        #                     self.start()
        #                 if self.device(resourceId="cn.youth.news:id/rb").exists:
        #                     self.device(resourceId="cn.youth.news:id/rb").click()
        #                     time.sleep(0.2)
        #                     self.readArticles += 1
        #                 elif self.device(resourceId="cn.youth.news:id/d5").exists:
        #                     self.device(resourceId="cn.youth.news:id/d5").click()
        #                     time.sleep(0.2)
        #                 else:
        #                     print("返回异常")
        #                     self.start()
        #         else:
        #             print("获取文章列表失败")
        #
        #             self.start()
        #         self.device.swipe_ext("up", 1)
        #         self.device.swipe_ext("up", 0.6)
        #         if self.readArticles > self.setting.articles:
        #             self.haveFinishDaily = self.have_finish_daily()
        #     except UiObjectNotFoundError as e:
        #         print("读取文章异常，重启app充实")
        #         self.start()
        # print("===================" + str(self.__class__) + ":结束此轮阅读文章=============================================")

    # 获取任务
    def get_daily_details(self):
        print("===================" + str(self.__class__) + ":获取任务开始=============================================")
        restart = 0
        while restart < self.setting.restartTimes:
            print("开始第" + str(restart) + "次获取")
            try:
                self.device.press("home")
                self.device.app_stop('cn.youth.news')
                self.device.app_start('cn.youth.news')
                time.sleep(3)
                self.device(resourceId="cn.youth.news:id/a7k").click()
                time.sleep(5)
                if self.device(resourceId="cn.youth.news:id/hl", text="每看30秒可获得大量阅读青豆，累计20篇额外加奖200青豆").exists:
                    text = self.device(resourceId="cn.youth.news:id/hl", text="每看30秒可获得大量阅读青豆，累计20篇额外加奖200青豆").sibling(resourceId="cn.youth.news:id/title").get_text()
                    restart = self.setting.restartTimes
                    p1 = re.compile(r'[(](.*?)[)]', re.S)
                    text = re.findall(p1, text)
                    print("获取成功")
                    print(text)
                    return text
                else:
                    print("阅读文章任务已经完成！")
                    return [str(self.setting.articles) + '/' + str(self.setting.articles)]
            except XPathElementNotFoundError as e:
                print("获取异常")
                restart += 1
                print(restart < self.setting.restartTimes)
        print("===================" + self.__class__ + ":获取任务结束=============================================")

    # 判断任务是否完成
    def have_finish_daily(self):
        # 任务详情数据
        text = self.get_daily_details()
        if text is None:
            print("获取任务数据异常")
            return None
        elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
            print("===================" + str(self.__class__) + ":开始阅读文章=============================================")
            self.readArticles = int(str(text[0]).split('/')[0])
            return False
        elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
            print("今天已经完成阅读文章任务，请收取金币")
            self.haveFinishDaily = True
            return True
        elif text is True:
            self.haveFinishDaily = True
            print("今天已经完成阅读文章任务，请收取金币")
            return True

    # 阅读文章
    def read_article(self):
        self.device.implicitly_wait(2)
        read_more = False
        for i in range(20):
            # 非正常文章排版 无返回按钮 直接过滤
            if str(self.device(resourceId="cn.youth.news:id/rb").exists) != "True" and str(self.device(resourceId="cn.youth.news:id/d5").exists) != "True":
                return False
            self.device.swipe_ext("up", 1)
            time.sleep(1.5)
            # 网络加载错误的情况
            if self.device(resourceId="cn.youth.news:id/ana").exists:
                self.device(resourceId="cn.youth.news:id/ana").click()
                time.sleep(2)
            if read_more is False and self.device.xpath('//*[@text="查看全文，奖励更多"]').exists:
                try:
                    self.device.xpath('//*[@text="查看全文，奖励更多"]').click()
                    # print("点击查看更多！！")
                    read_more = True
                except XPathElementNotFoundError as e:
                    pass
                    # print("还没到，继续")
        self.device.implicitly_wait(10)
