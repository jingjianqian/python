"""公共类"""
import time

from uiautomator2.exceptions import XPathElementNotFoundError


class Common:
    def __init__(self, device):
        self.device = device

    # 启动app
    def start_app(self, apps_package_name):
        try:
            self.device.press("home")
            time.sleep(0.5)
            self.device.app_stop(apps_package_name)
            self.device.app_start(apps_package_name)
            time.sleep(5)
        except XPathElementNotFoundError as e:
            print(e)

    # 滑动处理
    def swipe(self):
        pass

    # 解锁
    def unlock(self):
        pass

    # 登录app
    def login_app(self):
        pass
