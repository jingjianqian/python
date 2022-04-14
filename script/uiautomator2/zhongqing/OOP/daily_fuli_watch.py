from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class WelfareWatch:
    def __init__(self, device):
        self.device = device
        self.common = Common()
        self.settings = Settings()

    def start(self):
        pass

    def have_finish_daily(self):
        text = self.device().right()
