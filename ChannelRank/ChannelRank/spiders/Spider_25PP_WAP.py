# -*- coding: utf-8 -*-
import sys
import scrapy
from ChannelRank.items import *
import os
import sys
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re
import json
import time
import datetime

class Spider_25PP_WAP(scrapy.Spider):
    name="PP_WAP"
    def start_requests(self):
        url= 'http://jsondata.25pp.com/index.html'
        for i in range(0,7):
            body = '{"resType":2,"dcType":8,"listType":5,"catId":0,"clFlag":1,"perCount":15,"page":%s}'%(str(i))
            r = scrapy.Request(url,method="POST",headers={'Tunnel-Command':'4261437488','Content-Type':'application/x-www-form-urlencoded'},body=body,callback=self.parse)
            yield r
            if i ==0:
                r.meta['TopNow']=1
            elif i==1:
                r.meta['TopNow']=16
            elif i==2:
                r.meta['TopNow']=31
            elif i==3:
                r.meta['TopNow']=46
            elif i==4:
                r.meta['TopNow']=61
            elif i==5:
                r.meta['TopNow']=76
            elif i==6:
                r.meta['TopNow']=91

    def parse(self,response):
        x=response.meta['TopNow']
        jsonbody=re.compile('"content":(.*)').search(response.body).group(1)[:-1]
        data=json.loads(jsonbody)
        item=ChannelrankItem()
        for dd in data:
            item['ChannelID']=11
            item['GetTime']= str(time.strftime("%Y-%m-%d %H",time.localtime(time.time())))+':00:00'
            item['GameName']=dd['title']
            item['RankType']=48
            item['TopNow']=x
            item['PackageSize']=dd['fsize']
            item['GameType']='未知'
            item['VersionID']='未知'
            item['DownloadNum']=dd['downloads']
            item['iConURL']=dd['thumb']
            item['PlatForm']=5
            item['DownloadURL']=dd['downurl']
            item['WebURL']='未知'
            item['RunningType']='未知'
            item['HotTrend']='未知'
            item['CompanyName']='未知'
            item['Hot']=0
            item['From']=3
            item['Score']=0.0
            item['WeekDownload']=dd['weekdowns']
            item['Summary']=dd['remark']
            x+=1
            yield item
