"""每日签到类"""

from sqlite3 import connect

from connect import PhoneStatus

class Sign:
  def __init__(self):
    self.signStatus = PhoneStatus()
  

  def start_sign(self):
    connect