import uiautomator2 as u2

from connect import PhoneStatus
from daily_sign import Sign

"""
app每日任务主线
"""
#TODO add some init confige
class Daily:
  def __init__(self):
    # self.phoneStatus = PhoneStatus()
    # self.deviceName = self.phoneStatus.getDevices()
    pass

  # TODO begin daily things
  def start_daily(self):
    print("签到！")
    phontStatus = PhoneStatus()
    sign = Sign(phontStatus.getDevices,None)
    sign.start_sign()
    print(sign.signStatus)



daily = Daily()

daily.start_daily()

