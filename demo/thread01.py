import threading
import os
import time


def sing(name, lyric, times):
    for i in range(times):
        print("老王唱歌ID:", os.getpid())
        print(name + "： " + lyric)


def dance(name, danceStep, times):
    for i in range(times):
        print("老王跳舞ID:", os.getpid())
        print(name + ":" + danceStep)


if __name__ == '__main__':
    sing_process = threading.Thread(target=sing, args=("隔壁老王", "我爱你老婆", 10))
    dance_process = threading.Thread(target=dance,kwargs={"times": 10, "name": "老王", "danceStep": "I will will，fuck you!"})
    print("爸爸进程编号：", os.getpid())
    print("爷爷进程编号：", os.getppid())
    sing_process.daemon = True  # 设置子进程为守护进程
    dance_process.daemon = True  # 设置子进程为守护进程
    sing_process.start()
    dance_process.start()
    time.sleep(0.1)
    # dance_process.daemon = True
    print("主进程结束。。。。")
