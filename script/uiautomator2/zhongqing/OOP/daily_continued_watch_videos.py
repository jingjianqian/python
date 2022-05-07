from daily_video import Videos


class ContinueWatchVideos:

    def __init__(self, device):
        self.device = device

    def start(self):
        while True:
            read_5m_videos = Videos(self.device, 100)
            read_5m_videos.start()
