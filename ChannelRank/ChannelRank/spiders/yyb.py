#!/usr/local/bin/python
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

class yybSpider(scrapy.Spider):
    name='yyb'
    allowed_domains = ["qq.com"]
    start_urls=[]#'http://m5.qq.com/rank/apps.htm?cateId=-1&limit=100&orgame=2&rankType=2&start=0',]
    for rid in range(1,9):
        url='http://m5.qq.com/rank/apps.htm?cateId=-1&limit=100&orgame=2&rankType='+str(rid)+'&start=0'
        start_urls.append(url)
    
    def parse(self, response):
        
        GetTime=time.strftime('%Y-%m-%d %H:',time.localtime(time.time()))+'00'
       
        print GetTime
        
        result=json.loads(response.body)['obj']
        Getrankid=int(re.findall('rankType=(.*?)&',response.url)[0])

        print Getrankid
	print response.body

        n=1
        for games in result:
            item=ChannelrankItem()
            item['ChannelID']=6
            item['GetTime']=GetTime
            item['GameName']=games['appName']
            if Getrankid==1:
                item['RankType']=16
            if Getrankid==2:
                item['RankType']=17
            if Getrankid==3:
                item['RankType']=18
            if Getrankid==4:
                item['RankType']=19
            if Getrankid==5:
                item['RankType']=20
            if Getrankid==6:
                item['RankType']=21
            if Getrankid==7:
                item['RankType']=22
            if Getrankid==8:
                item['RankType']=23
            item['TopNow']=n
            n+=1
            item['PackageSize']=str(round(float(games['fileSize'])/float(1024)/float(1024),2))+'M'
            item['GameType']=games['categoryName']
            item['VersionID']=games['versionName']
            item['DownloadNum']=games['appDownCount']
            item['iConURL']=games['iconUrl']
            item['DownloadURL']=games['apkUrl']
            item['PlatForm']=1 
            item['WebURL']='δ֪'
            item['Hot']=0
            item['HotTrend']='δ֪'
            item['RunningType']='δ֪'
            item['Score']=round(games['averageRating'],2)
            item['From']=4
            item['CompanyName']=games['authorName']
            item['WeekDownload']=0
            item['Summary']=games['editorIntro']
            yield item
            
           
            

            
            
            
        
