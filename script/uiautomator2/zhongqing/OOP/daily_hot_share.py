"""热门文章分析"""
from uiautomator2 import UiObjectNotFoundError

from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class HotShare:
    def __init__(self, device):
        self.common = Common(device)
        self.settings = Settings()
        self.hotShares = 0
        self.device = device

    def start(self):
        """检查任务完成情况"""
        self.common.start_app('cn.youth.news')

        """判断是否完成任务"""
        if self.hava_finished() is True:
            return True
        try:
            self.device.implicitly_wait(2)
            self.device(resourceId="cn.youth.news:id/hl", text='分享资讯到朋友圈或微信3次，被好友阅读后可共得1800青豆').right(resourceId="cn.youth.news:id/eb").click()
        except UiObjectNotFoundError as e:
            print()
            self.start()

    def hava_finished(self):
        text = self.common.check_daily('分享资讯到朋友圈或微信3次，被好友阅读后可共得1800青豆', 2, '火爆转发')
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

