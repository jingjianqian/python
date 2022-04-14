from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class Search:

    def __init__(self, device):
        self.device = device
        self.common = Common()
        self.settings = Settings()
        self.searchTimes = 0

    def start(self):
        pass

    def have_finish_daily(self):
        text = self.common.check_daily('完成全部搜索任务额外获得150青豆', 2, '搜索领京豆')
        if text is None:
            print("获取任务数据异常")
            return None
        elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
            print(
                "===================" + str(self.__class__) + ":开始观看福利视频=============================================")
            self.searchTimes = int(str(text[0]).split('/')[0])
            return False
        elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
            print("今天已完成改任务，请收取金币")
            return True
        elif text is True:
            print("今天已完成改任务，请收取金币")
            return True

