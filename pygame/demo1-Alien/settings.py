class Settings:
  """存储游戏《外星人入侵》中所设置的类"""
  def __init__(self):
    """初始化游戏的设置"""
    # 屏幕设置
    self.screen_width = 1100
    self.screen_height = 600
    self.bg_color = (230,230,230)
    
    #飞船设置
    self.ship_speed = 1.5
  