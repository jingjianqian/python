from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class AdsVideos:

    def __init__(self, device):
        self.device = device
        self.common = Common()
        self.settings = Settings()
        self.adsVideos = 0

    # 开始任务
    def start(self):
        pass

    # 进入任务是否完成
    def have_finish_daily(self):
        text = self.common.check_daily('今日观看6次激励视频额外奖励150青豆', 2, '看福利视频')
        if text is None:
            print("获取任务数据异常")
            return None
        elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
            print("===================" + str(self.__class__) + ":开始观看福利视频=============================================")
            self.adsVideos = int(str(text[0]).split('/')[0])
            return False
        elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
            print("今天已经完成阅读文章任务，请收取金币")
            return True
        elif text is True:
            print("今天已经完成阅读文章任务，请收取金币")
            return True
