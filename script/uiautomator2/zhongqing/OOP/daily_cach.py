from daily_common import Common
from setttings import Settings


class Cash():

    def __init__(self, device):
        self.device = device
        self.common = Common()
        self.settings = Settings()

    def start(self):
        pass

    def have_finish_daily(self):
        text = self.common.check_daily('省时省力，秒赚青豆；完成一个任务额外获得100青豆', 2, '现金赚钱')
        print(text)
