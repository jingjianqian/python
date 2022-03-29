"""每日签到类"""
from connect import PhoneStatus

import uiautomator2 as u2

from setttings import Settings


"""签到类"""
class Sign:
  def __init__(self,deviceName,device):
    self.settings = Settings()
    self.phoneStatus = PhoneStatus()
    self.deviceName = deviceName
    self.device = device
    self.restartTimes = self.settings.restartTimes
    self.signStatus = None

  # 签到
  def start_sign(self):
    self.getSignStatus()
  # 判断签到状态
  def getSignStatus(self):
      try:
        self.device.app_start("cn.youth.news")
        self.device(resourceId="cn.youth.news:id/a7k").click()
        if 1:
          return True
        else:
          False
      except Exception as e:
        self.restartTimes  += 1
        print("第" + str(10-self.restartTimes) + "次获取签到状态失败")
        if self.restartTimes > 0:
          return self.getSignStatus(self.device)
        else:
          return None
          
  # # 启动app
  # def startApp(self):
  #   self.device.app_start("cn.youth.news")
  #   if self(resourceId="cn.youth.news:id/a7k").exists:
  #     return True
  #   else:
  #     return None