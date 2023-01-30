import uiautomator2 as u2

from script.uiautomator2.zhongqing.OOPNew.connect import PhoneStatus

"""
app每日任务主线
"""


# TODO add some init config
class Daily:
    def __init__(self):
        self.phoneStatus = PhoneStatus()
        self.deviceName = self.phoneStatus.get_devices()
        self.device = u2.connect(self.deviceName)
        pass

    # TODO begin daily things
    def start_daily(self):
        pass


if __name__ == '__main__':
    daily = Daily()
    daily.start_daily()
