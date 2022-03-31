"""设备连接状态"""
import subprocess

class PhoneStatus:
  def __init__(self):
    pass


 
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
    print("12312312312312312312313123")
  
  def network():
    pass

  def connectPhoneByAdb():
    pass