"""热门文章分析"""
from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class HotShare:
    def __init__(self, device):
        self.common = Common()
        self.settings = Settings()
        self.hotShares = 0
        self.device = device

    def start(self):
        """检查任务完成情况"""
        self.common.start_app('cn.youth.news')

    def hava_finished(self):
        text = self.common.check_daily('', 2, '火热转发')
        if text is None:
            print("获取任务数据异常")
            return None
        elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
            print("===================" + str(self.__class__) + ":开始阅读文章=============================================")
            self.hotShares = int(str(text[0]).split('/')[0])
            return False
        elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
            print("今天已经完成阅读文章任务，请收取金币")
            return True
        elif text is True:
            print("今天已经完成阅读文章任务，请收取金币")
            return True

