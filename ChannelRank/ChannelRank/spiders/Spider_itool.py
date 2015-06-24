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

reload(sys)
sys.setdefaultencoding('utf8') 

class Spider_itools(scrapy.Spider):
    
    name = "itools"
    allowed_domains = ["itools.cn"]
    start_urls = []
    Device=['iphone','ipad']

    for deviceType in Device:
        for i in range(0,4):
            url='http://ios.itools.cn/game/'+str(deviceType)+'/gameall_'+str(i)
            start_urls.append(url)
        print start_urls

    def parse(self, response):
        url_type=re.compile('game\/(.*)\/gameall').search(response.url).group(1)
        li_list=response.xpath('//ul[@class="ios_app_list"]//li')
        x=0
        for li in li_list:
            x+=1
            iConURL=''.join(li.xpath('.//div[@class="ios_app_cur"]//p[@class="ios_app_curPic"]//a//img//@lazyurl').extract())
            GameName=''.join(li.xpath('.//div[@class="ios_app_cur"]//p[@class="ios_app_curTxt"]')[0].xpath('.//text()').extract())
            Score=''.join(li.xpath('.//div[@class="ios_app_cur"]//p[@class="ios_app_curTxt"]')[1].xpath('.//span/text()').extract()[0][2:])
            summary=''.join(li.xpath('.//div[@class="ios_app_on"]//p//a/text()').extract())
            VersionID=''.join(li.xpath('.//div[@class="ios_app_on"]//span')[0].xpath('.//text()').extract()[0][3:])
            PackageSize=''.join(li.xpath('.//div[@class="ios_app_on"]//span')[1].xpath('.//text()').extract()[0][3:])
            item=ChannelrankItem()
            item['ChannelID']=8
            item['GetTime']=str(time.strftime("%Y-%m-%d %H",time.localtime(time.time())))+':00:00'
            item['GameName']=GameName
            if response.url=='http://ios.itools.cn/game/iphone/gameall_0' or response.url=='http://ios.itools.cn/game/ipad/gameall_0':
                item['RankType']=36
            elif response.url=='http://ios.itools.cn/game/iphone/gameall_1' or response.url=='http://ios.itools.cn/game/ipad/gameall_1':
                item['RankType']=37
            elif response.url=='http://ios.itools.cn/game/iphone/gameall_2' or response.url=='http://ios.itools.cn/game/ipad/gameall_2':
                item['RankType']=38
            elif response.url=='http://ios.itools.cn/game/iphone/gameall_3' or response.url=='http://ios.itools.cn/game/ipad/gameall_3':
                item['RankType']=39
            item['TopNow']=x
            item['PackageSize']=PackageSize
            item['GameType']='未知'
            item['VersionID']=VersionID
            item['DownloadNum']='未知'
            item['iConURL']=iConURL

            if url_type=='iphone':
                item['PlatForm']=2
            if url_type=='ipad':
                item['PlatForm']=3

            item['DownloadURL']='未知'
            item['WebURL']='未知'
            item['RunningType']='未知'
            item['Hot']=0
            item['HotTrend']='未知'
            item['From']=2
            item['Score']=Score
            item['CompanyName']='未知'
            item['WeekDownload']='未知'
            item['Summary']=summary
            yield item
