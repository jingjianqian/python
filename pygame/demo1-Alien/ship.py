import pygame

class Ship:
  """管理飞船的类"""

  def __init__(self,ai_game):
      self.screen = ai_game.screen
      self.screen_rect = ai_game.screen.get_rect()
      self.settings = ai_game.setttings
      #加载飞船图像并获取外接矩形
      self.image = pygame.image.load('D:\code\python\python\pygame\demo1-Alien\static\ship.bmp')
      self.rect = self.image.get_rect()
      #对于没搜新飞船，都将其放在屏幕底部的中央
      self.rect.midbottom = self.screen_rect.midbottom

      self.moving_right = False
      self.moving_left = False

  def update(self):
    """根据移动标识调整飞船的位置"""
    if self.moving_right:
      self.x +=  self.settings.ship_speed
    if self.moving_left:
      self.x -=  self.settings.ship_speed
    self.rect.x = self.x
    
  def blitme(self):
    """指定位置绘制飞船"""
    self.screen.blit(self.image,self.rect)
