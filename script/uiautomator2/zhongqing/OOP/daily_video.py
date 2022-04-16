"""看视频任务"""
import re
import time

from uiautomator2.exceptions import XPathElementNotFoundError, UiObjectNotFoundError

from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class Videos:
    def __init__(self, device) -> None:
        self.settings = Settings()
        self.device = device
        self.readVideos = 0
        self.haveFinishDaily = False

    def start(self):

        """1 启动app"""
        Common(self.device).start_app()

        """2 阅读视频"""
        restart = 0
        while self.readVideos < 5:
            if restart > self.settings.restartTimes:
                break
            try:
                print("观看视频")
                # 视频菜单
                self.device(resourceId="cn.youth.news:id/a7l").click()
                time.sleep(3)
                temp_videos = self.device.xpath('//*[@resource-id="cn.youth.news:id/a5f"]/android.widget.FrameLayout').all()
                if len(temp_videos) > 0:
                    for video in temp_videos:
                        video.click()
                        time.sleep(30)
                        self.readVideos += 1
                        if self.device(resourceId="	cn.youth.news:id/ama").exists:
                            self.device(resourceId="cn.youth.news:id/ama").click()
                            time.sleep(0.2)
                        elif self.device(resourceId="cn.youth.news:id/d5").exists:
                            self.device(resourceId="cn.youth.news:id/d5").click()
                            time.sleep(0.2)
                        else:
                            print("返回异常")
                            self.start()
                else:
                    print("视频列表错误")
                    self.start()
            except UiObjectNotFoundError as e:
                restart += 1
                self.start()

        """4 结束"""

    # 判断任务是否完成
    def have_finish_daily(self) -> str:
        # 视频任务数据详情
        text = self.get_daily_details()
        print(text)
        if text is None:
            print("获取任务数据异常")
            return None
        elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
            print("===================" + str(self.__class__) + ":开始视频=============================================")
            self.readVideos = int(str(text[0]).split('/')[0])
            return False
        elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
            print("今天已经完成观看任务，请收取金币")
            return True

    # 获取任务
    def get_daily_details(self):
        print("===================" + str(self.__class__) + ":获取视频任务开始=============================================")
        restart = 0
        while restart < self.settings.restartTimes:
            print("开始第" + str(restart) + "次获取")
            try:
                self.device.press("home")
                self.device.app_stop('cn.youth.news')
                self.device.app_start('cn.youth.news')
                time.sleep(3)
                self.device(resourceId="cn.youth.news:id/a7k").click()
                time.sleep(3)
                if self.device(resourceId="cn.youth.news:id/hl", text="每看30秒可获得大量观看青豆，累计10个额外加奖100青豆").exists:
                    text = self.device(resourceId="cn.youth.news:id/hl", text="每看30秒可获得大量观看青豆，累计10个额外加奖100青豆").sibling(
                        resourceId="cn.youth.news:id/title").get_text()
                    restart = self.settings.restartTimes
                    p1 = re.compile(r'[(](.*?)[)]', re.S)
                    text = re.findall(p1, text)
                    print("获取成功")
                    return text
                else:
                    print("阅读文章任务已经完成！")
                    restart += 1
                    return [str(self.settings.videos-1) + '/' + str(self.settings.videos)]
            except XPathElementNotFoundError as e:
                print("获取异常")
                restart += 1
                print(restart < self.settings.restartTimes)
        print("===================" + self.__class__ + ":获取视频任务结束=============================================")
