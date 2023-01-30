from script.checkHomeWork.Class import Class


class Student(Class):
    # 初始化学号与姓名
    def __init__(self, number, name):
        self.number = number
        self.name = name

    # 获取名字
    def get_name(self):
        return self.name

    # 获取学号
    def get_number(self):
        return self.number
