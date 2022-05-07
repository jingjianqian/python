from daily_common import Common
from daily_video import Videos
from setttings import Settings


class Read5mVideo:

    def __init__(self, device):
        self.device = device
        self.common = Common(self.device)
        self.setting = Settings()

    def start(self):
        while self.common.check_daily_unique("每日累计观看5分钟可领取100青豆", '观看5分钟') is not True:
            read_5m_videos = Videos(self.device)
            read_5m_videos.start()
