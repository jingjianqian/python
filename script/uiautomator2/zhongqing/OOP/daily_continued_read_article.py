from script.uiautomator2.zhongqing.OOP.daily_readArticle import ReadArticles


class ContinueReadArticle:

    def __init__(self, device):
        self.device = device

    def start(self):
        while True:
            read_articles = ReadArticles(self.device, 100)
            read_articles.start()
