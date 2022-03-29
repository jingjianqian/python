"""配置文件类"""
from connect import PhoneStatus 
class Settings:
  def __init__(self) -> None:
    self.phoneStatus = PhoneStatus().phoneStatus
    