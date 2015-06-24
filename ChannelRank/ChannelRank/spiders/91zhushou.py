# -*- coding: utf-8 -*-
import sys
import scrapy
from ChannelRank.items import ChannelrankItem
import os
import sys
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re 
import json
reload(sys)
sys.setdefaultencoding('utf8') 
import time

class game91AppSpider(scrapy.Spider):
    name='game91App'
    allowed_domains = ["91.com"]
    start_urls=['http://bbx2.sj.91.com/softs.ashx?act=291&mt=4&sv=3.9.8.6&osv=4.2.2&cpu=armeabi-v7a,armeabi&rslt=720*1232&imei=864737011730670&nt=10&dm=Lenovo+K860i&chl=1008370c&cuid=52F1487308EA760FD728BD128A1997B0|076037110737468&iv=1&pi=1&gpu=&imsi=',]
    def parse(self, response):
        GetTime=time.strftime('%Y-%m-%d %H:',time.localtime(time.time()))+'00'
        print GetTime
        result=json.loads(response.body)
        List=result['Result']['items']
        Num=1
        for l in List:
            item=ChannelrankItem()
            item['GameName']=l['name']
            item['GetTime']=GetTime
            item['ChannelID']=3
            item['RankType']=8
            item['TopNow']=Num
            item['PackageSize']=l['size']
            item['GameType']=l['cateName']
            item['VersionID']=l['versionName']
            item['DownloadNum']=l['downnum']
            item['iConURL']=l['icon']
            item['PlatForm']=1
            item['DownloadURL']='未知'
            item['Hot']=0
            item['HotTrend']=0
            item['RunningType']='未知'
            item['From']=1
            item['CompanyName']=l['author']
            item['Summary']='未知'
            item['WeekDownload']=0 
            item['WebURL']='未知'
            item['Score']=0.0
        
            Num+=1
            yield item
            
            


       
