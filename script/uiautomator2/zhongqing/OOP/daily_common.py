"""公共类"""
import re
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

    # zhongqing
    def check_daily(self, unique_text, times, daily_name):
        print("===================" + str(daily_name) + "->任务获取开始=============================================")
        restart = 0
        while restart < self.setting.restartTimes:
            print("开始第" + str(restart) + "次获取")
            try:
                self.device.press("home")
                self.device.app_stop('cn.youth.news')
                self.device.app_start('cn.youth.news')
                time.sleep(3)
                self.device(resourceId="cn.youth.news:id/a7k").click()
                time.sleep(3)
                if self.device(resourceId="cn.youth.news:id/hl", text=unique_text).exists:
                    text = self.device(resourceId="cn.youth.news:id/hl", text=unique_text).sibling(resourceId="cn.youth.news:id/title").get_text()
                    restart = self.setting.restartTimes
                    p1 = re.compile(r'[(](.*?)[)]', re.S)
                    text = re.findall(p1, text)
                    print("获取成功")
                    print(text)
                    return text
                else:
                    print("任务已经完成！")
                    return [str(times) + '/' + str(times)]
            except XPathElementNotFoundError as e:
                print("获取异常")
                restart += 1
                print(restart < self.setting.restartTimes)
        print("===================" + str(daily_name) + "->获取任务结束=============================================")
