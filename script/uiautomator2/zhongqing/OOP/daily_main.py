import uiautomator2 as u2

from connect import PhoneStatus
from daily_sign import Sign

"""
app每日任务主线
"""
#TODO add some init confige
class Daily:
  def __init__(self):
    self.deviceName = PhoneStatus.getDevices()

  # TODO begin daily things
  def start_daily(self):
    print("签到！")
    sign = Sign(self.deviceName,None)
    sign.start_sign()
    print(sign.signStatus)



daily = Daily()

daily.start_daily()

