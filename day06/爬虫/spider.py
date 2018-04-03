__author__ = "gongwei"

import urllib.response
import urllib.request
import requests
from bs4 import BeautifulSoup


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


class Spider:
    '''
    1.爬取网页
    2.解析网页信息
    '''
    def __init__(self, page_url, host_url = ''):
        self.pageUrl = page_url
        self.hostUrl = host_url
        self.pageHtml = ''

    def web_crawl(self):
        '''

        :return:
        '''
        if self.pageUrl is None:
            self.pageHtml = ''
        request = urllib.request.Request(self.pageUrl)
        # 下面的两个header是为了模拟手机浏览器，因为慕课网app可以不用注册就可以访问视频，所以把咱们的程序模拟成手机浏览器，就可以直接下载了
        request.add_header('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36')
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            self.pageHtml = response.read()

    def parse_web_html(self):
        '''

        :return:
        '''
        wp = WebParser(self.pageHtml, self.hostUrl)
        wp.parse()


class WebParser:
    '''
    1.解析网页html并获取页面信息pageInfo
    '''
    def __init__(self, html_text='', host_url=''):
        self.hostUrl = host_url
        self.htmlText = html_text
        self.pageInfos = []

    def parse(self):
        '''
        :return: self.indexInfo
        '''
        bs = BeautifulSoup(self.htmlText, 'lxml', from_encoding='utf-8')
        link_pics = bs.find_all('img', border="0")
        link_pages = bs.find_all('a', target="_blank")
        if len(link_pages) != 0:
            for link in link_pages:
                page_info = PageInfo()
                page_info.pageName = link.h2.text
                page_info.pageUrl = link.get('href')
                self.pageInfos.append(page_info)
                spider1 = Spider(self.hostUrl + page_info.pageUrl)
                spider1.web_crawl()
                spider1.parse_web_html()
                if len(link_pics) != 0:
                    for link_pic in link_pics:
                        pic_info = PicInfo()
                        pic_info.pDir = 'G:\\Pic\\' + page_info.pageName
                        link = link_pic.get('src')
                        pic_info.picName = link[-22:]
                        pic_info.picUrl = link_pic.get('src')
                        with open(pic_info.pDir + '\\' + pic_info.picName, 'w') as f:
                            f.write(requests.get(pic_info.picUrl).content)






spider = Spider("", "")
spider.web_crawl()
spider.parse_web_html()
