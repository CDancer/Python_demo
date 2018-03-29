__author__ = "gongwei"

import requests
import time

begin_time = time.time()
response = requests.get("https://tbm.alicdn.com/vUAdB2SRl6Uwi7hn7WB/ZGX5RZ2uF00UQYp3jlk@@hd.mp4")
data = response.content
print(data.size())
with open("moive.mp4", "wb") as file_img:
    file_img.write(data)

end_time = time.time()

print("film is loaded! use time:%s" %(end_time - begin_time))