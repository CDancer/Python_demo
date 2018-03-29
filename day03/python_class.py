__author__ = "gongwei"

class Person:
    cn = "中国"

    '''构造函数'''
    def __init__(self):
        self.name = 'gongwei'

    '''析构函数'''
    def __del__(self):
        print("析构函数！")

    def piao(self):
        print("in the class Person!")



class Man(Person):
    def piao(self):
        Person.piao(self)
        print("in the class man!")




pp = Person()
print(pp.name)
print(pp.cn)


print(Man.cn)

m = Man()
m.piao()
