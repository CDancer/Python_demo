__author__ = "gongwei"
import json
import pickle

def test(name):
    print("hello world!", name)

info = {
    'name':'gongwei',
    'age':'25',
    'func':test
}

f = open('test.text',"wb")
# f.write(str(info))
# f.write(json.dumps(info))
f.write(pickle.dumps(info))

