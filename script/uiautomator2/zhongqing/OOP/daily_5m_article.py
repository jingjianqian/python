"""
阅读十分钟
"""
from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.daily_readArticle import ReadArticles
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class Read5mArticle:

    def __init__(self, device):
        self.device = device
        self.common = Common(self.device)
        self.setting = Settings()

    def start(self):
        """1 检测任务完成情况"""
        while self.common.check_daily("每日累计阅读10分钟可领取200青豆", 5,'阅读十分钟') is not True:
            read_article = ReadArticles(self.device)
            read_article.start()
