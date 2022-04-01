"""阅读文章"""
import re
import time

from uiautomator2.exceptions import XPathElementNotFoundError, UiObjectNotFoundError

from script.uiautomator2.zhongqing.OOP.setttings import Settings


class ReadArticles:
    def __init__(self, device_name, device) -> None:
        self.deviceName = device_name
        self.setting = Settings()
        self.device = device
        self.readArticles = 0

    def start(self):
        # 任务详情数据
        text = self.get_daily_details()
        if text is not None:
            print(str(text[0]).split('/'))
        else:
            print("获取任务数据异常")

        # 开始阅读文章
        print("===================" + str(self.__class__) + ":开始阅读文章=============================================")
        restart = 0
        while self.readArticles < self.setting.restartTimes and restart < 50:
            # 阅读文章
            try:
                self.device.press("home")
                self.device.app_stop('cn.youth.news')
                self.device.app_start('cn.youth.news')
                time.sleep(3)
                print("阅读文章")
                # 网络加载失败时监听器
                temp_articles = self.device.xpath('//*[@resource-id="cn.youth.news:id/a5f"]/android.widget.LinearLayout').all()
                if len(temp_articles) > 0:
                    for article in temp_articles:
                        article.click()
                        time.sleep(3)
                        self.device(resourceId="cn.youth.news:id/rb").click()
                        time.sleep(1)
                        self.readArticles += 1
                else:
                    raise XPathElementNotFoundError
                self.device.swipe_ext("up", 1)
                self.device.swipe_ext("up", 0.6)
                restart = self.setting.restartTimes
            except UiObjectNotFoundError as e:
                restart += 1
                print("读取文章异常，重启app充实")
        print("===================" + str(self.__class__) + ":结束阅读文章=============================================")

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
                time.sleep(2)
                if self.device(resourceId="cn.youth.news:id/hl", text="每看30秒可获得大量阅读青豆，累计20篇额外加奖200青豆").exists:
                    text = self.device(resourceId="cn.youth.news:id/hl", text="每看30秒可获得大量阅读青豆，累计20篇额外加奖200青豆").sibling(resourceId="cn.youth.news:id/title").get_text()
                    restart = self.setting.restartTimes
                    p1 = re.compile(r'[(](.*?)[)]', re.S)
                    text = re.findall(p1, text)
                    print("获取成功")
                    return text
                else:
                    print("阅读文章任务已经完成！")
                    restart += 1
                    print(restart < self.setting.restartTimes)
                    break
            except XPathElementNotFoundError as e:
                print("获取异常")
                restart += 1
                print(restart < self.setting.restartTimes)
        print("===================" + self.__class__ + ":获取任务结束=============================================")

    # 阅读文章
    def read_article(self):
        # self.device.
        pass
