import time

from uiautomator2 import UiObjectNotFoundError

from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class WelfareWatch:
    def __init__(self, device):
        self.device = device
        self.common = Common(device)
        self.settings = Settings()

    def start(self):
        self.common.start_app()
        try:
            self.device(resourceId="cn.youth.news:id/a7k").click()
            time.sleep(2)
            # for i in range(6):
            #     # self.device(resourceId="cn.youth.news:id/hl", text='今日观看6次激励视频额外奖励150青豆').right(resourceId="cn.youth.news:id/eb").click()
        except UiObjectNotFoundError as e:
            print(e)
            self.start()

    def have_finish_daily(self):
        pass
