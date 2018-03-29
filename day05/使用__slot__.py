__author__ = "gongwei"


class student(object):
    pass

'''给student的对象s绑定属性'''
s = student()
s.name = "gongwei"
print(s.name)

'''给student的对象s绑定方法'''
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


'''给student类绑定方法'''
student.set_age = set_age
s.set_age(30)
print(s.age)

'''用关键字__slots__限定类的属性'''
class Human(object):
    __slots__ = ('sex', 'age', '__address')
    def __init__(self):
        self.__address = '山西省大同市'

    def get_address(self):
        return self.__address


Human.age = 25
Human.sex = 'man'
Human.height = 1.85

hh = Human()
print(hh.age)
print(hh.sex)
print(hh.height)
# print(hh.__address)   __address为私有变量，不允许对象直接访问

print(hh.get_address())
