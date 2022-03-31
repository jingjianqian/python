"""main主线任务"""
from sign import Sign
from login import Login


class Hao4k:
    def __init__(self) -> None:
        print('init')
        self.status = False

    def run_script(self):
        login = Login()
        self.status
        login.default_login_way()


if __name__ == '__main__':
    hao4k = Hao4k()
    hao4k.run_script()
