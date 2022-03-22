import time
import uiautomator2 as u2

from chromedriver import ChromeDriver 



d = u2.connect('192.168.0.108:5555') # alias for u2.connect_wifi('10.0.0.1')
d.app_stop('cn.youth.news')
d.app_start('cn.youth.news')
time.sleep(5)
# 固定菜单点击位置
d.click(0.708, 0.964)
time.sleep(0.5)
#任务1 ，阅读文章，点击去阅读按钮
d.xpath('//*[@resource-id="cn.youth.news:id/adx"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
time.sleep(0.2)
# 阅读第一篇文章
d(resourceId="cn.youth.news:id/a0d").click()
for num in range(30):
    d.swipe_ext("up", 0.6)
    time.sleep(1)
d(resourceId="cn.youth.news:id/re").click()