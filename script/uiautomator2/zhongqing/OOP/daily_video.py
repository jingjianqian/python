"""看视频任务"""
import re
import time

from uiautomator2.exceptions import XPathElementNotFoundError, UiObjectNotFoundError

from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class Videos:
    def __init__(self, device_name, device) -> None:
        self.settings = Settings()
        self.deviceName = device_name
        self.device = device
        self.readVideos = 0
        self.haveFinishDaily = False

    def start(self):
        """1 判断是否完成任务"""
        if self.have_finish_daily() is True:
            return True

        """2 重启app"""
        Common(self.device).start_app('cn.youth.news')

        """3 循环完成任务"""
        while self.haveFinishDaily is not True:
            try:
                print("观看视频")
                # 视频菜单
                self.device(resourceId="").click()
                time.sleep(0.3)
                temp_videos = self.device.xpath('').all()
                if len(temp_videos) > 0:
                    for video in temp_videos:
                        video.click()
                        time.sleep(3)
                        if self.device(resourceId="cn.youth.news:id/rb").exists:
                            self.device(resourceId="cn.youth.news:id/rb").click()
                            time.sleep(0.3)
                        elif self.device(resourceId="cn.youth.news:id/d5").exists:
                            self.device(resourceId="cn.youth.news:id/d5").click()
                            time.sleep(0.3)
                        else:
                            print("返回异常")
            except UiObjectNotFoundError as e:
                pass

        """4 结束"""

    # 判断任务是否完成
    def have_finish_daily(self) -> str:
        # 视频任务数据详情
        text = self.get_daily_details()
        if text is None:
            print("获取任务数据异常")
            return None
        elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
            print("===================" + str(self.__class__) + ":开始文章=============================================")
            self.readVideos = int(str(text[0]).split('/')[0])
            return False
        elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
            print("今天已经完成观看任务，请收取金币")
            return True

    # 获取任务
    def get_daily_details(self):
        print("===================" + str(self.__class__) + ":获取视频任务开始=============================================")
        restart = 0
        while restart < self.setting.restartTimes:
            print("开始第" + str(restart) + "次获取")
            try:
                self.device.press("home")
                self.device.app_stop('cn.youth.news')
                self.device.app_start('cn.youth.news')
                time.sleep(3)
                self.device(resourceId="cn.youth.news:id/a7k").click()
                time.sleep(1)
                if self.device(resourceId="cn.youth.news:id/hl", text="每看30秒可获得大量观看青豆，累计10个额外加奖100青豆").exists:
                    text = self.device(resourceId="cn.youth.news:id/hl", text="每看30秒可获得大量观看青豆，累计10个额外加奖100青豆").sibling(
                        resourceId="cn.youth.news:id/title").get_text()
                    restart = self.setting.restartTimes
                    p1 = re.compile(r'[(](.*?)[)]', re.S)
                    text = re.findall(p1, text)
                    print("获取成功")
                    return text
                else:
                    print("阅读文章任务已经完成！")
                    restart += 1
                    return [self.setting.articles, self.setting.articles]
            except XPathElementNotFoundError as e:
                print("获取异常")
                restart += 1
                print(restart < self.setting.restartTimes)
        print("===================" + self.__class__ + ":获取视频任务结束=============================================")
