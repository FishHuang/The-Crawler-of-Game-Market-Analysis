#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import scrapy
from ChannelRank.items import *
import os
import sys
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.spiders import CrawlSpider, Rule
import re
import time
import MySQLdb
import json

reload(sys)
sys.setdefaultencoding('utf8')

class Spider_25PP(scrapy.Spider):
    name = "PP"

    def start_requests(self):
        url_list = ['http://www.25pp.com/iphone/top/list_weekdowns_71_1.html','http://www.25pp.com/iphone/top/list_monthdowns_71_1.html','http://www.25pp.com/iphone/top/list_downloads_71_1.html']
        orderby=['weekdowns','monthdowns','downloads']
        for url in url_list:
            for a in range(1,3):
                if a==1:
                    r=scrapy.Request(url,method="GET",callback=self.parse)
                    yield r
                else:
                    if url=='http://www.25pp.com/iphone/top/list_weekdowns_71_1.html':
                        for i in range(2,6):
                            body='devtype=iphone&orderby=%s&catid=71&page=1&group=%s'%('weekdowns',str(i))
                            r=scrapy.Request(url,method="POST",headers={'Content-Type': 'application/x-www-form-urlencoded'},body=body,callback=self.parse_post)
                            if i ==2:
                                r.meta['TopNow']=24
                            elif i==3:
                                r.meta['TopNow']=48
                            elif i==4:
                                r.meta['TopNow']=72
                            elif i==5:
                                r.meta['TopNow']=96
                            yield r
                    elif url=='http://www.25pp.com/iphone/top/list_monthdowns_71_1.html':
                        for i in range(2,6):
                            body='devtype=iphone&orderby=%s&catid=71&page=1&group=%s'%('monthdowns',str(i))
                            r=scrapy.Request(url,method="POST",headers={'Content-Type': 'application/x-www-form-urlencoded'},body=body,callback=self.parse_post)
                            if i ==2:
                                r.meta['TopNow']=24
                            elif i==3:
                                r.meta['TopNow']=48
                            elif i==4:
                                r.meta['TopNow']=72
                            elif i==5:
                                r.meta['TopNow']=96
                            yield r
                    elif url=='http://www.25pp.com/iphone/top/list_downloads_71_1.html':
                        for i in range(2,6):
                            body='devtype=iphone&orderby=%s&catid=71&page=1&group=%s'%('downloads',str(i))
                            r=scrapy.Request(url,method="POST",headers={'Content-Type': 'application/x-www-form-urlencoded'},body=body,callback=self.parse_post)
                            if i ==2:
                                r.meta['TopNow']=24
                            elif i==3:
                                r.meta['TopNow']=48
                            elif i==4:
                                r.meta['TopNow']=72
                            elif i==5:
                                r.meta['TopNow']=96
                            yield r

    def parse(self, response):
        item=ChannelrankItem()
        dl_list=response.xpath('//div[@id="contentArea"]//dl')
        for dl in dl_list:
            iConURL=''.join(dl.xpath('.//dt//a//img//@src').extract())
            dd=dl.xpath('.//dd')
            GameName=''.join(dd[0].xpath('.//h3//a/text()').extract())
            VersionID=''.join(dd[0].xpath('.//p/text()').extract()[0].split('|')[0])
            PackageSize=''.join(dd[0].xpath('.//p/text()').extract()[1].split('|')[0])
            DownloadNum=''.join(dd[0].xpath('.//p/text()').extract()[1].split('|')[1])
            TopNow=''.join(dd[1].xpath('.//text()').extract())
            item['ChannelID']=11
            item['GetTime']=str(time.strftime("%Y-%m-%d %H",time.localtime(time.time())))+':00:00'
            item['GameName']=GameName

            if response.url=='http://www.25pp.com/iphone/top/list_weekdowns_71_1.html':
                item['RankType']=42
            elif response.url=='http://www.25pp.com/iphone/top/list_monthdowns_71_1.html':
                item['RankType']=43
            elif response.url=='http://www.25pp.com/iphone/top/list_downloads_71_1.html':
                item['RankType']=44

            item['TopNow']=TopNow
            item['PackageSize']=PackageSize
            item['GameType']='未知'
            item['VersionID']=VersionID
            item['DownloadNum']=DownloadNum[:-3]
            item['iConURL']=iConURL
            item['PlatForm']=2
            item['DownloadURL']='未知'
            item['WebURL']='未知'
            item['RunningType']='未知'
            item['Hot']=0
            item['HotTrend']='未知'
            item['From']=2
            item['Score']=0.0
            item['CompanyName']='未知'
            item['WeekDownload']='未知'
            item['Summary']='未知'
            yield item

    def parse_post(self, response):
        x=response.meta['TopNow']
        item=ChannelrankItem()
        data=json.loads(response.body)['contentArea']
        for dd in data:
            x+=1
            item['ChannelID']=11
            item['GetTime']=str(time.strftime("%Y-%m-%d %H",time.localtime(time.time())))+':00:00'
            item['GameName']=dd['title']

            if response.url=='http://www.25pp.com/iphone/top/list_weekdowns_71_1.html':
                item['RankType']='42'
            elif response.url=='http://www.25pp.com/iphone/top/list_monthdowns_71_1.html':
                item['RankType']='43'
            elif response.url=='http://www.25pp.com/iphone/top/list_downloads_71_1.html':
                item['RankType']='44'

            item['TopNow']=x
            item['PackageSize']=dd['size']
            item['GameType']='未知'
            item['VersionID']=dd['appVersion']
            item['DownloadNum']=dd['downCount']
            item['iConURL']=dd['imgSrc']
            item['PlatForm']='2'
            item['DownloadURL']='未知'
            item['WebURL']='未知'
            item['RunningType']='未知'
            item['Hot']=0
            item['HotTrend']='未知'
            item['From']='3'
            item['Score']=dd['grade']
            item['CompanyName']='未知'
            item['WeekDownload']='未知'
            item['Summary']='未知'
            yield item
