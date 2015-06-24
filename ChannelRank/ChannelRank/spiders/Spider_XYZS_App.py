#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import scrapy
from ChannelRank.items import *
import os
import sys
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re 
import time
import MySQLdb
import json

reload(sys)
sys.setdefaultencoding('utf8') 

class Spider_XYZS(scrapy.Spider):
    
    name = "XYZS_APP"
    allowed_domains = ["xyzs.com"]
    start_urls = []
    rank_type=['download','soaring','praise']
    Now=int(time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S')))
    for i in rank_type:
        for j in range(1,6):
            url='http://interface.xyzs.com/ios/datacenter.php?function=recommendtop&timestamp=%s&clientversion=2.8.1&curpage=%s&pagesize=20&sort=downloadnum&t=game&subclass=%s'%(str(Now),str(j),str(i))
            start_urls.append(url)

    def parse(self, response):
        x=0
        print response.body
        jsondata=re.compile('"data":(.*),"page"').search(response.body).group(1)
        data=json.loads(jsondata)
        url_type=re.compile('subclass=(.*)').search(response.url).group(1)
        url_page=re.compile('curpage=(.*?)&').search(response.url).group(1)
        for dd in data:
            x+=1
            item=ChannelrankItem()
            item['ChannelID']=7
            item['GetTime']= str(time.strftime("%Y-%m-%d %H",time.localtime(time.time())))+':00:00'
            item['GameName']=dd['title']

            if str(url_type)=='download':
                item['RankType']=45
            elif str(url_type)=='soaring':
                item['RankType']=46
            elif str(url_type)=='praise':
                item['RankType']=47

            if str(url_page)=='1':
                item['TopNow']=x
            elif str(url_page)=='2':
                item['TopNow']=20+x
            elif str(url_page)=='3':
                item['TopNow']=40+x
            elif str(url_page)=='4':
                item['TopNow']=60+x
            elif str(url_page)=='5':
                item['TopNow']=80+x

            item['PackageSize']=dd['size']
            item['GameType']='未知'
            item['VersionID']=dd['version']
            item['DownloadNum']=dd['downloadnum']
            item['iConURL']=dd['pic']
            item['PlatForm']=5
            item['DownloadURL']='未知'
            item['WebURL']='未知'
            item['RunningType']='未知'
            item['Hot']=0
            item['HotTrend']='未知'
            item['From']=1
            item['Score']=dd['score']
            item['CompanyName']='未知'
            item['WeekDownload']='未知'
            item['Summary']=dd['desc']
            yield item
