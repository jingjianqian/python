"""每日签到类"""
from connect import PhoneStatus

import uiautomator2 as device1

from setttings import Settings

"""签到类"""


class Sign:
    def __init__(self, device_name, device):
        self.settings = Settings()
        self.phoneStatus = PhoneStatus()
        self.deviceName = device_name
        self.device = device
        self.restartTimes = self.settings.restartTimes
        self.signStatus = None

    # 签到
    def start_sign(self):
        try:
            if self.get_sign_status() is True:
                if self.device(resourceId="cn.youth.news:id/awo").exists:
                    self.device(resourceId="cn.youth.news:id/awo").click()
                elif self.device(resourceId="cn.youth.news:id/title", text="今日签到").exists:
                    self.device.xpath('//*[@resource-id="cn.youth.news:id/a5f"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
                    self.device(resourceId="cn.youth.news:id/awo").click()
                else:
                    return False
        except device1.xpath.XPathElementNotFoundError as e:
            return False

    # 判断签到状态
    def get_sign_status(self):
        try:
            self.device.app_stop("cn.youth.news")
            self.device.app_start("cn.youth.news")
            self.device(resourceId="cn.youth.news:id/a7k").click()
            if 1:
                return True
            else:
                False
        except Exception as e:
            self.restartTimes += 1
            print("第" + str(10 - self.restartTimes) + "次获取签到状态失败")
            if self.restartTimes > 0:
                return self.get_sign_status()
            else:
                return True
