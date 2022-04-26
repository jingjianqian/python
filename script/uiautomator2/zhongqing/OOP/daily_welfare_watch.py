import time

from uiautomator2 import UiObjectNotFoundError
from uiautomator2.exceptions import XPathElementNotFoundError

from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class WelfareWatch:
    def __init__(self, device):
        self.device = device
        self.common = Common(device)
        self.settings = Settings()

    def start(self):
        self.common.start_app()
        if self.common.check_daily_unique('今日观看6次激励视频额外奖励150青豆','看福利视频') is True:
            return
        try:
            self.device(resourceId=self.settings.dailyTag).click()
            time.sleep(2)
            for i in range(6):
                self.device(resourceId="cn.youth.news:id/hl", text='今日观看6次激励视频额外奖励150青豆').right(resourceId="cn.youth.news:id/eb").click()
                time.sleep(30)
                left_time = self.device(className="android.widget.TextView").get_text()
                time.sleep(int(left_time)+1)
                self.device.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
                self.device(resourceId=self.settings.dailyTag).click()
            self.start()
        except UiObjectNotFoundError as e:
            print(e)
            self.start()
        except XPathElementNotFoundError as e:
            self.start()
        except ValueError as e:
            self.start()

    def have_finish_daily(self):
        pass
