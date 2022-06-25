"""配置文件类"""

from connect import PhoneStatus


class Settings:
    def __init__(self) -> None:
        self.restartTimes = 10  # 重试次数
        self.phonePassword = 920221  # 手机解锁密码
        self.articles = 20  # 默认需要阅读文章的次数
        self.appPackageName = 'cn.youth.news'  # app包名
        self.videos = 10  # 默认需要观看视频的次数
        self.HotShares = 3  # 默认需要分享的文章
        self.base_daily_list = {"sign": "每日签到", 'read5min': '阅读5分钟', 'read10min': '阅读十分钟', 'read60min': '阅读60分钟',
                                'watch10video': '观看10次视频'}
        self.other_daily_list = {"search3time": '搜索领青豆'}

        self.dailyTag = 'cn.youth.news:id/x_'
        self.signXpath = '//*[@resource-id="cn.youth.news:id/a4z"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]'
        self.signSuccessLogId = 'cn.youth.news:id/awf'

        self.readArticleUniqueXpath = "cn.youth.news:id/hj"
        self.readArticleTab = "cn.youth.news:id/wa"
