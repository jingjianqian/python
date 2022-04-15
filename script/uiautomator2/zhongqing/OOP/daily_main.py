import uiautomator2 as u2

from connect import PhoneStatus
from daily_sign import Sign
from script.uiautomator2.zhongqing.OOP.daily_60m_article import Read60MArticle
from script.uiautomator2.zhongqing.OOP.daily_hot_share import HotShare
from script.uiautomator2.zhongqing.OOP.daily_readArticle import ReadArticles
from script.uiautomator2.zhongqing.OOP.daily_search import Search
from script.uiautomator2.zhongqing.OOP.daily_video import Videos
from script.uiautomator2.zhongqing.OOP.daily_welfare_watch import WelfareWatch

"""
app每日任务主线
"""


# TODO add some init config
class Daily:
    def __init__(self):
        self.phoneStatus = PhoneStatus()
        self.deviceName = self.phoneStatus.get_devices()
        self.device = u2.connect(self.deviceName)
        pass

    # TODO begin daily things
    def start_daily(self):
        print("阅读5分钟")
        read_60m_article = Read60MArticle(self.device)
        read_60m_article.start()
        # print("签到！")
        # sign = Sign(self.deviceName, self.device)
        # sign.start_sign()
        # print("阅读文章")
        # read_articles = ReadArticles(self.deviceName, self.device)
        # read_articles.start()
        # print("观看视频")
        # read_videos = Videos(self.deviceName, self.device)
        # read_videos.start()
        # print("火爆转发")
        # hot_share = HotShare(self.device)
        # hot_share.start()
        # print("观看福利视频")
        # welfare_watch = WelfareWatch(self.device)
        # welfare_watch.start()
        # print("搜索")
        # search = Search(self.device)
        # search.start()


if __name__ == '__main__':
    daily = Daily()
    daily.start_daily()
