__author__ = "gongwei"

import os

first_path = os.path.abspath(__file__)
print(first_path)
sec_path = os.path.dirname(first_path)
print(sec_path)
thd_path = os.path.dirname(sec_path)
print(thd_path)

def login():
    print("welcome to atm!")



