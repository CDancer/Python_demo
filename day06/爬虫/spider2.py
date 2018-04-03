__author__ = "gongwei"

import urllib.response
import urllib.request
import urllib.error
import requests
from bs4 import BeautifulSoup
import os
import os.path
import queue
import threading,time
import socket
socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒

# condition = threading.Condition()
# PICINFOS = queue.Queue()
# COUNT = [0]

sleep_time = 1
host_url = "http://seniu6.com"

# 1.需要加个线程管理（线程池）
# 2.目前线程可能会死锁
# 3.有些图片通过浏览器可以下载下来，但是程序爬不下来，还没分析具体是什么问题导致


class PicInfo:
    '''

    '''
    def __init__(self):
        self.picUrl = ''
        self.picName = ''
        self.pDir = ''


class PageInfo:
    '''

    '''
    def __init__(self):
        self.pageUrl = ''
        self.pageName = ''
        self.picInfos = []


def spider(url):
    global sleep_time
    request = urllib.request.Request(url)
    # 下面的两个header是为了模拟手机浏览器，因为慕课网app可以不用注册就可以访问视频，所以把咱们的程序模拟成手机浏览器，就可以直接下载了
    request.add_header('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36')
    while True:
        try:
            time.sleep(sleep_time)
            response = urllib.request.build_opener().open(request)
            if response.getcode() == 200:
                html = response.read()
                response.close()
                if html is not None:
                    if sleep_time > 5:
                        sleep_time -= 1
                    return html
                else:
                    continue
        except urllib.error.URLError as e:
            print(e.reason, ':', url)
        except socket.timeout as e:
            print("-----socket timout:", url)
        except:
            if sleep_time < 20:
                sleep_time += 1
            print('********************do not know why it is happened!*****************')
            print("************************ now sleep time is: %d *********************" % sleep_time )


def donwload_pic(pic_info):
    try:
        if not os.path.exists(pic_info.pDir):
            os.mkdir(pic_info.pDir)
            print(pic_info.pDir)
    except:
        pic_info.pDir = 'G:/Pic1/dirNameError'
        if not os.path.exists(pic_info.pDir):
            os.mkdir(pic_info.pDir)
    if os.path.exists(pic_info.pDir + '/' + pic_info.picName):
        return

    # 下载成功退出，失败再次下载，重复下载5次
    reload_count = 0
    while True:
        with open(pic_info.pDir + '/' + pic_info.picName, 'wb') as f:
            try:
                f.write(requests.get(pic_info.picUrl).content)
                if reload_count == 0:
                    f.close()
                    break
            except:
                f.close()
                pic_file_path = pic_info.pDir + '/' + pic_info.picName
                print(pic_file_path, 'failed!!!!!!')
                print(pic_info.picUrl)
                reload_count += 1
                print('reload {0} {1} time!'.format(pic_file_path, str(reload_count)))
                time.sleep(1)
                if reload_count == 5:
                    if os.path.exists(pic_file_path):
                        os.remove(pic_file_path)
                    break


def get_pic(host_url, index_url):
    page_html = spider(host_url + index_url)
    bs = BeautifulSoup(page_html, 'lxml', from_encoding='utf-8')
    link_pages = bs.find_all('a', target="_blank")
    page_infos = []
    if len(link_pages) != 0:
        for link in link_pages:
            page_info = PageInfo()
            page_info.pageName = link.h2.text
            page_info.pageUrl = link.get('href')
            page_infos.append(page_info)

    for page_info in page_infos:
        pic_html = spider(host_url + page_info.pageUrl)
        bs = BeautifulSoup(pic_html, 'lxml', from_encoding='utf-8')
        link_pics = bs.find_all('img', border="0")
        for link_pic in link_pics:
            pic_info = PicInfo()
            pic_info.pDir = 'G:/Pic1/' + page_info.pageName
            link = link_pic.get('src')
            pic_info.picName = link[-22:]
            pic_info.picUrl = link_pic.get('src')
            # PICINFOS.put(pic_info)
            donwload_pic(pic_info)


class SpiderThread(threading.Thread):
    global host_url

    def __init__(self):
        super().__init__()
        self.index = 0

    def run(self):
        page_index = 0
        for i in range(100):
            page_index = i*100 + self.index
            print('******************* now in page: %d********************' % page_index)
            if page_index != 0:
                get_pic(host_url, "/tupian/wangyouzipai/index%d.html" % page_index)
            else:
                get_pic(host_url, "/tupian/wangyouzipai/index.html")


list_thread = []
for i in range(100):
    st = SpiderThread()
    st.index = i
    list_thread.append(st)
    time.sleep(1)
    st.start()




# for i in range(3, 100):
#     get_pic("http://seniu6.com", "/tupian/yazhoutupian/index%d.html" % i)

#
# class Producer(threading.Thread):
#     '''生产者'''
#     ix = [0]  # 生产者实例个数
#
#     # 闭包，必须是数组，不能直接 ix = 0
#     def __init__(self, ix=0):
#         super().__init__()
#         self.ix[0] = 2
#         self.setName('生产者' + str(self.ix[0]))
#
#     def run(self):
#
#          condition, PICINFOS, COUNT
#
#         for i in range(100):
#             if i < 2:
#                 continue
#             if condition.acquire():
#                 if COUNT < 20:
#                     get_pic("http://seniu6.com", "/tupian/yazhoutupian/index%d.html" % i)
#                     condition.notify()
#                 else:
#                     print("{}库存充足(20+)。让我休息会儿，现在产品总数量 {}".format(self.getName(), COUNT))
#                     condition.wait()
#                 condition.release()
#
#
# class Consumer(threading.Thread):
#     '''消费者'''
#     ix = [0]  # 消费者实例个数
#
#     # 闭包，必须是数组，不能直接 ix = 0
#     def __init__(self):
#         super().__init__()
#         self.ix[0] += 1
#         self.setName('消费者' + str(self.ix[0]))
#
#     def run(self):
#         global condition, PICINFOS, COUNT
#
#         while True:
#             if condition.acquire():
#                 if len(PICINFOS) > 0:
#                     donwload_pic(PICINFOS.get())
#                     print("{}：我消费了1件产品，现在产品数量 {}".format(self.getName(), COUNT))
#                     condition.notify()
#                 else:
#                     print("{}：无产品可消费，我停止消费。现在产品数量 {}".format(self.getName(), COUNT))
#                     condition.wait()
#                 condition.release()
#
#
#
# if __name__ == "__main__":
#
#     p = Producer()
#     p.start()
#
#     for i in range(10):
#         c = Consumer()
#         c.start()
