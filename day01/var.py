# Author:gongwei
import time
'''
print("hello world")

data = {
    "haha":"niubi"
}

while True:
    for i in data:
        print(i)


    choice = input("选择进入>>")
    if choice in data:
        print("it is in the data",choice)
'''

def timer(func):
    def deco(*argc, **argv):
        star_time = time.time()
        func(*argc, **argv)
        end_time = time.time()
        print("the func run tiem is %s" %(end_time - star_time))
    return deco

@timer     # test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the time1")
    pass

@timer
def test2(name):
    time.sleep(2)
    print("in the time2")
    pass

test1()
test2("haha")



        


