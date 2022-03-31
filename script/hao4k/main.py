"""main主线任务"""
from sign import Sign
from login import Login
class hao4k:
  def __init__(self) -> None:
      print('init')

  def run_script(self):
    login = Login()
    login.startLogin()
    
  
if __name__=='__main__':
  hao4k = hao4k()
  hao4k.run_script()