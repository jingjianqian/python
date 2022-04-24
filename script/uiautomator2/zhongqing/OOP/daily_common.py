"""公共类"""
import re
import time

from uiautomator2.exceptions import XPathElementNotFoundError, UiObjectNotFoundError
import uiautomator2.exceptions as u2exceptions
from script.uiautomator2.zhongqing.OOP.setttings import Settings

"""
公共类
"""


class Common:
    def __init__(self, device):
        self.device = device
        self.setting = Settings()

    # 启动app
    def start_app(self):
        try:
            self.device.press("home")
            time.sleep(0.5)
            self.device.app_stop(self.setting.appPackageName)
            self.device.app_start(self.setting.appPackageName)
            time.sleep(8)
            if self.device(resourceId="cn.youth.news:id/aio").exists:
                self.device(resourceId="cn.youth.news:id/aio").click()
        except UiObjectNotFoundError as e:
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

    """
    获取所有任务完成情况
    """

    def check_all_daily_unique(self):
        print("==========================>开始获取所有任务完成情况==========================")
        restart = 0
        while restart < self.setting.restartTimes:
            print("开始第" + str(restart) + "次获取任务完成完全情况")

    """
    根据任务唯一描述任务完成情况
    """

    def check_daily_unique(self, unique_text: str, daily_name: str):
        print("==========================>开始获取" + daily_name + "任务," + unique_text + "==========================")
        restart = 0
        while restart < self.setting.restartTimes:
            print("开始第" + str(restart) + "次获取" + daily_name + "任务完成完全情况")
            try:
                """1 重启app"""
                print("启动app中")
                self.start_app()
                """2 跳转到任务获取菜单"""
                print("跳转到任务列表TAB")
                self.device(resourceId="cn.youth.news:id/a7k").click()
                time.sleep(6)
                if self.device(text="领奖励").exists:
                    self.device(text="领奖励").click()
                    if daily_name == "搜索领京豆":
                        time.sleep(6)
                        self.device.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[2]').click()
                        self.device(text="领奖励").click()
                        time.sleep(0.5)
                        self.device(resourceId="cn.youth.news:id/rb").click()
                    time.sleep(2)
                if self.device(resourceId="cn.youth.news:id/sn").exists:
                    self.device(resourceId="cn.youth.news:id/sn").click()
                if self.device(resourceId="cn.youth.news:id/hl", text=unique_text).exists:
                    text = self.device(resourceId="cn.youth.news:id/hl", text=unique_text).sibling(
                        resourceId="cn.youth.news:id/title").get_text()
                    restart = self.setting.restartTimes
                    p1 = re.compile(r'[(](.*?)[)]', re.S)
                    text = re.findall(p1, text)
                    if text is None:
                        print("获取" + daily_name + "任务数据异常")
                        return None
                    elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
                        print(daily_name + "任务未完成")
                        print("=================>结束获取" + daily_name + "任务," + unique_text + "===================>")
                        return False
                    elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
                        print(daily_name + " 任务已经完成")
                        print( "===============>结束获取" + daily_name + "任务," + unique_text + "=====================")
                        return True
                    else:
                        print("获取" + daily_name + "任务数据异常")
                        print("========= =====>结束获取" + daily_name + "任务," + unique_text + "=========================")
                        return None
                else:
                    print(daily_name + " 任务已经完成")
                    print("==========================>结束获取" + daily_name + "任务," + unique_text + "==========================>")
                    return True
            except UiObjectNotFoundError as e:
                print("获取任务过程中寻找元素异常，准备重试")
                restart += 1
            except XPathElementNotFoundError as e:
                print("获取任务过程中寻找元素异常，准备重试")
                restart += 1
        print("=====》结束获取" + daily_name + "任务," + unique_text)

    def check_daily_unique2(self, unique_text: str, daily_name: str):
        if self.device(resourceId="cn.youth.news:id/hl", text=unique_text).exists:
            text = self.device(resourceId="cn.youth.news:id/hl", text=unique_text).sibling(
                resourceId="cn.youth.news:id/title").get_text()
            restart = self.setting.restartTimes
            p1 = re.compile(r'[(](.*?)[)]', re.S)
            text = re.findall(p1, text)
            if text is None:
                print("获取" + daily_name + "任务数据异常")
                return None
            elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
                print(daily_name + "任务未完成")
                print(
                    "==========================>结束获取" + daily_name + "任务," + unique_text + "==========================>")
                return False
            elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
                print(daily_name + " 任务已经完成")
                print(
                    "==========================>结束获取" + daily_name + "任务," + unique_text + "==========================")
                return True
            else:
                print("获取" + daily_name + "任务数据异常")
                print(
                    "==========================>结束获取" + daily_name + "任务," + unique_text + "==========================")
                return None

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
                    text = self.device(resourceId="cn.youth.news:id/hl", text=unique_text).sibling(
                        resourceId="cn.youth.news:id/title").get_text()
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
