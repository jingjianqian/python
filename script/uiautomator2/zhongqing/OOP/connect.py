"""设备连接状态"""
from asyncio.windows_events import NULL
import subprocess

class PhoneStatus:
  def __init__(self) -> None:
    self.phoneStatus = self.phoneStatus()
    self.devices = self.getDevices() # 默认只允许一台手机连接adb
    self.network = self.network()




 
  def getDevices():
    try:
      devices = subprocess.getstatusoutput("adb devices")
      if devices[0] == 0:
         return 'VED7N18C04000042' # TODO 目前写死，后续改为实际返回设备名称
      else:
        return None
    except Exception as e:
      print("adb 环境错误！")
      return None
   

  """手机连接状态方法"""
  def  phoneStatus():
    pass
  
  def network():
    pass

  def connectPhoneByAdb():
    pass