from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.daily_readArticle import ReadArticles
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class Read20Article:

    def __init__(self, device):
        self.device = device
        self.common = Common(self.device)
        self.settings = Settings()

    def start(self):
        while self.common.check_daily_unique("每看30秒可获得大量阅读青豆，累计20篇额外加奖200青豆", "阅读20篇文章") is not True:
            read_article = ReadArticles(self.device, 10)
            read_article.start()
