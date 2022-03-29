"""配置文件类"""

from connect import PhoneStatus 

class Settings:
  def __init__(self) -> None:
    self.phoneStatus = PhoneStatus().phoneStatus # 手机连接状态
    self.restartTimes = 10 # 重试次数
    self.phonePassword = 920221 # 手机解锁密码
    
    