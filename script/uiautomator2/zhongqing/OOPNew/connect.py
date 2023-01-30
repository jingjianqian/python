"""设备连接状态"""
import subprocess


class PhoneStatus:
    def __init__(self):
        # adb 环境变量配置
        self.ADBStatus = False

    # 获取adb环境问题
    def get_adb_status(self):
        if self.ADBStatus:
            pass
        else:
            adb_info = subprocess.getstatusoutput("adb --version")
            print("adbInfo:" + adb_info);
            self.ADBStatus = True
            # if adb_info[0] == 0:
            #     self.ADBStatus = True
            # else:
            #     self.ADBStatus = False

    # 获取设备名称
    def get_devices(self):
        if self.ADBStatus is False:
            print("adb环境异常，请安装adb工具！！")
            return False
        else:
            print("查找设备，，，")
            devices = subprocess.getstatusoutput("adb devices")
            print(devices)
            if devices[0] == 0:
                print("找到设备：" + devices[0])
                return 'VED7N18C04000042'  # TODO 目前写死，后续改为实际返回设备名称
            else:
                print("未找到设备")
                return None

    """手机连接状态方法"""

    def phone_status(self):
        pass

    def network(self):
        pass

    def connect_phone_by_db(self):
        pass
