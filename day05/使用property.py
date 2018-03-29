__author__ = "gongwei"

class Student(object):
    # def __init__(self):
    #     self.name = None
    #     self.age = None
    #     self.score = None

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

ss = Student()

ss.name = 'gongwei'
print(ss.name)