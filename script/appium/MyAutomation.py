from script.appnim.appium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time, random, re

# {
#   "platformName": "Android",
#   "deviceName": "66ef453c",
#   "appPackage": "tv.yixia.bobo",
#   "appActivity": "com.kg.v1.welcome.WelcomeActivity",
#   "platformVersion": "9.0",
#   "noReset": true
# }

# Appium 基本参数
PLATFORM = 'Android'
DEVICE_NAME = '66ef453c'#66ef453c（k20）  cdbdc2c6（old）  39678a33（vivo）  0693d4050403(hongmi note9)
UDID = '66ef453c'
PLATFORM_VERSION = '9.0'

DRIVER_SERVER = 'http://localhost:4723/wd/hub'
TIMEOUT = 800
NORESET = 'True'
FLICK_STRAT_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700

class MyAutomation():
    # 初始化 Appium 基本参数
    def __init__(self, APP_PACKAGE, APP_ACTIVITY):
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
            'noReset': NORESET,
            'newCommandTimeout': TIMEOUT,
            'autoGrantPermissions': 'True',
            'udid': UDID,
            'platformVersion': PLATFORM_VERSION,
            # 'marionette': 'True'
        }
        print('打开 appium 服务器...')
        print('配置 appium ...')

        # firefox_capabilities = DesiredCapabilities.FIREFOX
        # firefox_capabilities['platformName'] = PLATFORM
        # firefox_capabilities['deviceName'] = DEVICE_NAME
        # firefox_capabilities['appPackage'] = APP_PACKAGE
        # firefox_capabilities['appActivity'] = APP_ACTIVITY
        # firefox_capabilities['noReset'] = NORESET
        # firefox_capabilities['newCommandTimeout'] = TIMEOUT
        # firefox_capabilities['autoGrantPermissions'] = True
        # firefox_capabilities['marionette'] = True


        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 10)
        self.size = self.driver.get_window_size()

    # 屏幕方法
    def swipeUp(self):
        # 向上滑动屏幕
        x1 = self.size['width'] * random.uniform(0.60, 0.65)
        y1 = self.size['height'] * random.uniform(0.70, 0.75)
        x2 = self.size['width'] * random.uniform(0.60, 0.65)
        y2 = self.size['height'] * random.uniform(0.28, 0.30)
        r = random.uniform(500, 800)
        self.driver.swipe(x1,
                          y1,
                          x2,
                          y2
                          , r)
        print('向上滑动屏幕')

    def swipeUpScope(self,scopeBottom,scopeTop):
        # 向上滑动屏幕
        x1 = self.size['width'] * random.uniform(0.60, 0.65)
        y1 = self.size['height'] * random.uniform(scopeBottom, scopeBottom+0.05)
        x2 = self.size['width'] * random.uniform(0.60, 0.65)
        y2 = self.size['height'] * random.uniform(scopeTop, scopeTop+0.02)
        r = random.uniform(500, 800)
        self.driver.swipe(x1,
                          y1,
                          x2,
                          y2
                          , r)
        print('向上滑动屏幕')

    def swipeDown(self):
        # 向下滑动屏幕
        x1 = self.size['width'] * random.uniform(0.55, 0.65)
        y1 = self.size['height'] * random.uniform(0.25, 0.35)
        x2 = self.size['width'] * random.uniform(0.55, 0.65)
        y2 = self.size['height'] * random.uniform(0.65, 0.75),
        r = random.uniform(800, 1200)
        self.driver.swipe(x1,
                          y1,
                          x2,
                          y2,
                          r)
        print('向下滑动屏幕')

    def swipeRight(self):
        # 向右滑动屏幕
        x1 = self.size['width'] * random.uniform(0.01, 0.11)
        y1 = self.size['height'] * random.uniform(0.75, 0.89)
        x2 = self.size['width'] * random.uniform(0.89, 0.98)
        y2 = self.size['height'] * random.uniform(0.75, 0.89)
        r = random.uniform(800, 1200)
        self.driver.swipe(x1,
                          y1,
                          x2,
                          y2,
                          r)
        print('向右滑动屏幕')

    def swipeLeft(self):
        # 向左滑动屏幕
        self.driver.swipe(self.size['width'] * random.uniform(0.75, 0.80),
                          self.size['height'] * random.uniform(0.80, 0.85),
                          self.size['width'] * random.uniform(0.31, 0.41),
                          self.size['height'] * random.uniform(0.80, 0.85), random.uniform(800, 1200))
        print('向左滑动屏幕')