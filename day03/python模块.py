__author__ = "gongwei"


import time

tt = time.time()

m = tt/3600/24/365

print(m)

print(1970+int(m))


print(time.localtime()[4])

print(time.timezone/3600)
print(time.daylight)
print(time.clock())
print(time.localtime(29999433234))