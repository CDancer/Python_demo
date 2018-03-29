__author__ = "gongwei"
import json
import pickle


def test(name):
    print("hello world!", name)


# f = open("test.text","r")
# data = json.loads(f.read())
with open("test.text", "rb") as f:
    # data = json.loads(f.read())
    data = pickle.loads(f.read())
# print(data["age"])

data["func"]("gongwei")

f.close()


