"""配置文件类"""

from connect import PhoneStatus


class Settings:
    def __init__(self) -> None:
        self.restartTimes = 10  # 重试次数
        self.phonePassword = 920221  # 手机解锁密码
        self.articles = 20  # 默认需要阅读文章的次数
