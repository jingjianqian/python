from pydoc import classname
import time
import uiautomator2 as u2

d = u2.connect('192.168.0.106:5555') # alias for u2.connect_wifi('10.0.0.1')
d.implicitly_wait(10.0) # 元素查找超时设置
d.app_stop('cn.youth.news')
d.app_start('cn.youth.news')
time.sleep(5)
# 固定菜单点击位置
d.click(0.708, 0.964)
time.sleep(0.5)


def closeDialog():
    if(d(resourceId="cn.youth.news:id/sq").exists):
            d(resourceId="cn.youth.news:id/sq").click()
            print("关闭弹窗")
    else:
        pass

# #签到方法
# def signIn():
#     try:
#         print("开始签到")
#         closeDialog()
#         if(d(resourceId="cn.youth.news:id/ae5").exists):
#             d(resourceId="cn.youth.news:id/ae5").click()
#             print("签到成功")
#             time.sleep(1)
#         else:
#             print("今天已经签到过啦！")
#         closeDialog()
#     except Exception as e:
#         print("签到可能出现异常！！！！")

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


