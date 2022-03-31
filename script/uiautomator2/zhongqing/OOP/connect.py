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
            devices = subprocess.getstatusoutput("adb --version")
            if devices[0] == 0:
                self.ADBStatus = True
            else:
                self.ADBStatus = False

    # 获取设备名称
    def get_devices(self):
        if self.ADBStatus is False:
            return False
        else:
            devices = subprocess.getstatusoutput("adb devices")
            if devices[0] == 0:
                return 'VED7N18C04000042'  # TODO 目前写死，后续改为实际返回设备名称
            else:
                return None

    """手机连接状态方法"""

    def phone_status(self):
        pass

    def network(self):
        pass

    def connect_phone_by_db(self):
        pass
