from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.daily_readArticle import ReadArticles
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class Read60MArticle:
    def __init__(self, device):
        self.device = device
        self.common = Common(device)
        self.settings = Settings()
        self.watchMinutes = 0

    def start(self):
        while self.common.check_daily_unique('每日累计阅读10分钟可领取200青豆', '《 阅读10分钟 》') is not True:
            ReadArticles(self.device, 10).start()
        print("done")

    def have_finish_daily(self):
        text = self.common.check_daily('每日累计阅读60分钟可领取400青豆奖励', 2, '阅读60分钟')
        if text is None:
            print("获取任务数据异常")
            return None
        elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
            print(
                "===================" + str(self.__class__) + ":开始观看福利视频=============================================")
            self.watchMinutes = int(str(text[0]).split('/')[0])
            return False
        elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
            print("今天已经完成阅读文章任务，请收取金币")
            return True
        elif text is True:
            print("今天已经完成阅读文章任务，请收取金币")
            return True
