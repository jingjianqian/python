from random import random
from re import T, U
import re
from tempfile import tempdir
import time
from tkinter import E
from traceback import print_tb
from unittest import result
from xml.etree.ElementPath import xpath_tokenizer
import uiautomator2 as u2
import os,subprocess

d = u2.connect('VED7N18C04000042') # alias for u2.connect_wifi('10.0.0.1')

# d.implicitly_wait(10.0) # 元素查找超时设置
# d.app_stop('cn.youth.news')
# d.app_start('cn.youth.news')
# time.sleep(5)


"""
关闭弹窗方法
"""
def closeDialog():
    if(d(resourceId="cn.youth.news:id/sq").exists):
            d(resourceId="cn.youth.news:id/sq").click()
            print("关闭弹窗")
    else:
        pass

"""
阅读首页热门文章方法 每三次刷新一次文章
"""
def readIndexHotArticls():
    d.app_stop('cn.youth.news')
    d.app_start('cn.youth.news')
    time.sleep(3)
    # #点击首页TAB
    # if d(resourceId="cn.youth.news:id/xj").exists:
    #     d(resourceId="cn.youth.news:id/xj").click()
    #     time.sleep(3)
    # else:
    #     print("文章首页按钮获取失败！！！")
    #     return
    print("开始阅读热点文章")
    time.sleep(3)

    #网络加载失败时监听器
    d.watcher('netError').when(xpath='//*[@resource-id="cn.youth.news:id/ana"]').click()
    d.watcher.start()

    # 阅读30片左右文章 一次三篇，循环十次
    for i in range(0, 10):
        temp = i
        print("=====================================================第"+ str(temp + 1) + "轮==========================================================")
        for j in range(0,3):
            print(i*3)
            print(j+1)
            indexAr = (i*3) + (j + 1)
            print(indexAr)
            print('第' + str(indexAr) + '篇')

            #文章连接
            try:
                d.xpath('//*[@resource-id="cn.youth.news:id/a5f"]/android.widget.LinearLayout['+ str(j + 1)+']').click()
                time.sleep(5)
            except u2.exceptions.XPathElementNotFoundError as e:
                print("第"+ str(i * 3 + j + 1) + "篇文章读取失败")
            #滚动阅读文章
            d.implicitly_wait(2)
            readMore = False
            for i in range(20):
                d.swipe_ext("up",0.6)
                time.sleep(3)
                if readMore == False and d.xpath('//*[@text="查看全文，奖励更多"]').exists:
                    try: 
                        d.xpath('//*[@text="查看全文，奖励更多"]').click()
                        # print("点击查看更多！！")
                        readMore = True
                    except u2.xpath.XPathElementNotFoundError as e:
                        pass
                        # print("还没到，继续")
            #返回连接
            if  d(resourceId="cn.youth.news:id/rb").exists:
                 d(resourceId="cn.youth.news:id/rb").click()
                 time.sleep(0.5)
            else:
                try:
                    d(resourceId="cn.youth.news:id/d5").click()
                except u2.xpath.XPathElementNotFoundError as e:
                    print("试图返回上一页失败！")
        #刷新首页文章
        if d(resourceId="cn.youth.news:id/xj").exists:
            d(resourceId="cn.youth.news:id/xj").click()
            time.sleep(3)
        else:
            print("读取首页文章失败")
            return
    print("阅读首页热点结束")
    d.watcher.stop()

#每日阅读文章20篇可 TODO 需要完善下翻引起的部分条码无法读取问题
def readRangeArticls():
    d.app_stop('cn.youth.news')
    d.app_start('cn.youth.news')
    time.sleep(3)
    if d(resourceId="cn.youth.news:id/xj").exists:
        d(resourceId="cn.youth.news:id/xj").click()
        time.sleep(0.5)
    else:
        print("文章首页按钮获取失败！！！")
        return
    print("开始阅读文章")
    d(resourceId="cn.youth.news:id/akx").click()
    time.sleep(5)
    
    d.click(0.495, 0.984)
    time.sleep(5)
    # 广告按钮
    # d.watcher("watchReadMore").when(xpath='//*[@text="查看全文，奖励更多"]').click()
    d.watcher("watchAds").when(xpath='//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]').click()
    d.watcher("isVideosAds").when(xpath="cn.youth.news:id/a3x").click()
    d.watcher.start()
    for count in range(0,10):
        print(count + 1)
        for i in range(0,3):
            #if d(resourceId="cn.youth.news:id/tv_empty").exists
            articleIndex = int(i) + 1 + int(count) * i 
            print("第"+ str(articleIndex) + "篇")
            try:
                xpathValue = '//*[@resource-id="cn.youth.news:id/a5i"]/android.widget.LinearLayout['+ str(i + 1) +']/android.widget.RelativeLayout[1]'
                xpath = d.xpath(xpathValue)
                print(xpath)
                d.xpath(xpathValue).click()
            except u2.exceptions.XPathElementNotFoundError as e:
                print("读取"+ "第"+ str(count*4 + (i + 1)) + "篇"  +"文章时异常！！")
                break
            print("这里啊这里啊这里啊这里啊")
            time.sleep(5)
            d.implicitly_wait(3)
            for i in range(10):
                d.swipe_ext("up",0.6)
                try: 
                    d.xpath('//*[@text="查看全文，奖励更多"]').click()
                    print("点击查看更多！！")
                except u2.xpath.XPathElementNotFoundError as e:
                    print("没有，继续")
            d(resourceId="cn.youth.news:id/rb").click()
            time.sleep(0.1)
        d.swipe_ext("up",1)
        d.swipe_ext("up",0.3)
        # d.swipe(10,)
        d.dump_hierarchy()
    d.watcher.stop()
    d.implicitly_wait(10)
    print("阅读排行榜文章结束")

def watchVideo():
    d.app_stop('cn.youth.news')
    d.app_start('cn.youth.news')
    time.sleep(5)
    d(resourceId="cn.youth.news:id/xm").click()
    time.sleep(3)
    watchVideoCounts = 0
    #视频广告监听器
    d.watcher("watchVideoAds").when(xpath="cn.youth.news:id/ama").click()
    d.watcher.start()
    while(watchVideoCounts < 10):
        try:
            #每次读取两行
            for i in range(0,4):
                d.xpath('//*[@resource-id="cn.youth.news:id/a5f"]/android.widget.FrameLayout[' + str(i + 1) +']/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()
                print("开始计数")
                time.sleep(20)
                watchVideoCounts = watchVideoCounts + 1
                print("计数+1")
                print("开始返回")
                d(resourceId="cn.youth.news:id/d5").click()
                time.sleep(1)
        except u2.exceptions.XPathElementNotFoundError as e:
            print("可能有广告,滑动")
            d.swipe_ext("up",1)
            time.sleep(1)

    d.watcher.stop()
    print("今日观看视频数：" + str(watchVideoCounts) + "次")


    # for i in range(0,20):
        # d.xpath('//*[@resource-id="cn.youth.news:id/a5i"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
        #          //*[@resource-id="cn.youth.news:id/a5i"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]
    #     # for j in range(0,3):
    #     #     temp_xpath = '//*[@resource-id="cn.youth.news:id/a5j"]/android.widget.LinearLayout[' + str(j+1) + ']'
    #     #     d.xpath(temp_xpath).click()
    #     #     time.sleep(3)
    #     #     #滑动阅读文章
    #     #     for num in range(10):
    #     #         d.swipe_ext("up", 0.6)
    #     #         if d(text="查看全文，奖励更多").exists:
    #     #             d(text="查看全文，奖励更多").click()
    #     #         time.sleep(0.3) 
    #     #     if d(resourceId="cn.youth.news:id/re").exists:
    #     #         d(resourceId="cn.youth.news:id/re").click()
    #     #         time.sleep(0.3)
    #     temp_xpath = '//*[@resource-id="cn.youth.news:id/a5j"]/android.widget.LinearLayout[' + str(i+1) + ']'
    #     d.xpath(temp_xpath).click()
    #     for num in range(10):
    #         d.swipe_ext("up", 0.6)
    #         if d(text="查看全文，奖励更多").exists:
    #             d(text="查看全文，奖励更多").click()
    #             time.sleep(0.3) 
    #         if d(resourceId="cn.youth.news:id/re").exists:
    #             d(resourceId="cn.youth.news:id/re").click()
    #             time.sleep(0.3)
    #     d.swipe_ext("up", 1)
    #     #d(resourceId="cn.youth.news:id/a7l").click()
    #     time.sleep(1)

#签到方法
def signIn():
    try:
        d.app_stop('cn.youth.news')
        d.app_start('cn.youth.news')
        time.sleep(6)
        print("开始签到")
        closeDialog()
        if d(resourceId="cn.youth.news:id/xl").exists:
            d(resourceId="cn.youth.news:id/xl").click()
        else:
            print("签到页面获取失败！")
            return
        if(d(resourceId="cn.youth.news:id/ae5").exists):
            d(resourceId="cn.youth.news:id/ae5").click()
            print("签到成功")
            time.sleep(1)
        else:
            print("今天已经签到过啦！")
        closeDialog()
    except Exception as e:
        print("签到可能出现异常！！！！")

#  #任务1 ，阅读文章，点击去阅读按钮
# def readArticle():
#     try:
#         closeDialog()
#         if(d.xpath('//*[@resource-id="cn.youth.news:id/adx"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]')):
#             d.xpath('//*[@resource-id="cn.youth.news:id/adx"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
#             time.sleep(0.2)
#             # 阅读第一篇文章
#             closeDialog()
#             d(resourceId="cn.youth.news:id/a0d").click()
#             closeDialog()
#             if d(text="查看全文，奖励更多").exists:
#                 d(text="查看全文，奖励更多").click()
#                 print("点击查看全文，奖励更多")
#                 time.sleep(0.1)
#             for num in range(30):
#                 d.swipe_ext("up", 0.6)
#                 if d(text="查看全文，奖励更多").exists:
#                     d(text="查看全文，奖励更多").click()
#                 time.sleep(0.3)
#         else:
#             print("读取第一篇文章失败")

#         if d(resourceId="cn.youth.news:id/re").exists:
#             d(resourceId="cn.youth.news:id/re").click()#返回按钮
#             time.sleep(0.3)
#         #第二篇文章
#         d.xpath('//*[@resource-id="cn.youth.news:id/a5j"]/android.widget.LinearLayout[2]').click()
#         time.sleep(0.2)
#         for num in range(30):
#             d.swipe_ext("up", 0.6)
#             time.sleep(0.2)
#         #第三篇文章
       
            
#     except Exception as e:
#         print("阅读文章出现问题啦奶奶的！")
#         print(e)



# #获取任务清单
# def taskList():
#     tasks = d(className="android.widget.LinearLayout").child_selector(resourceId="cn.youth.news:id/ee")
#     for task in tasks:
#         print(task) 

# taskList()


def test():
    print(d.app_stop('cn.youth.news'))
    print(d.app_start('cn.youth.news'))
test()
 
 
def deal_cmd(cmd):
	# result = subprocess.getstatusoutput(cmd)
    return subprocess.getstatusoutput(cmd)


def deal_result():
    try:
        devices = subprocess.getstatusoutput("adb devices")
        print(devices[1].split("\n\t"))
    except Exception as e:
        print(e)
    

# deal_result()

# signIn()
try:
    readIndexHotArticls()
except Exception as e:
    print("阅读文章遇到问题！！！")
try:   
    watchVideo()
except Exception as e:
    print(e)
    print("看视频遇到问题")