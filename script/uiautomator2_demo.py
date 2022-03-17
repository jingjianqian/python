import time
import uiautomator2 as u2

from chromedriver import ChromeDriver 



d = u2.connect('192.168.0.110:5555') # alias for u2.connect_wifi('10.0.0.1')
d.press("home")
d.app_stop('com.eg.android.AlipayGphone')
d.app_start('com.eg.android.AlipayGphone')

time.sleep(3)

d(resourceId="com.alipay.android.phone.openplatform:id/app_text", text="蚂蚁森林").click()