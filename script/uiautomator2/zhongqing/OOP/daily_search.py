import time

from uiautomator2 import UiObjectNotFoundError

from script.uiautomator2.zhongqing.OOP.daily_common import Common
from script.uiautomator2.zhongqing.OOP.setttings import Settings


class Search:

    def __init__(self, device):
        self.device = device
        self.common = Common(device)
        self.settings = Settings()
        self.searchTimes = 0

    def start(self):
        if self.have_finish_daily() is True:
            return True
        try:
            print("12313123")
            self.common.start_app('cn.youth.news')
            self.device(resourceId="cn.youth.news:id/xl").click()
            time.sleep(1)
            self.device(resourceId="cn.youth.news:id/hl", text='完成全部搜索任务额外获得150青豆').right(resourceId="cn.youth.news:id/eb").click()
            time.sleep(2)
            for i in range(3):
                print(i)
                temp_xpath = '//android.widget.ListView/android.view.View['+str(i+1)+']/android.view.View[2]'
                self.device.xpath(temp_xpath).click()
                time.sleep(1)
                search_titles = self.device(resourceId='wordListWrapper').child(className='android.view.View')
                print(len(search_titles))
                print(search_titles[0].get_text())

            # self.device(resourceId="cn.youth.news:id/nz").click()
            # if
        except UiObjectNotFoundError as e:
            print(e)
            self.start()

    def have_finish_daily(self):
        text = self.common.check_daily('完成全部搜索任务额外获得150青豆', 2, '搜索领京豆')
        if text is None:
            print("获取任务数据异常")
            return None
        elif text is not None and int(str(text[0]).split('/')[0]) < int(str(text[0]).split('/')[1]):
            print(
                "===================" + str(self.__class__) + ":开始搜索任务check=============================================")
            self.searchTimes = int(str(text[0]).split('/')[0])
            return False
        elif text is not None and int(str(text[0]).split('/')[0]) == int(str(text[0]).split('/')[1]):
            print("今天已完成改任务，请收取金币")
            return True
        elif text is True:
            print("今天已完成改任务，请收取金币")
            return True

