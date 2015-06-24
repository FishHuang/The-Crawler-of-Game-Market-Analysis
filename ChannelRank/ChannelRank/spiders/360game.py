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

class game360Spider(scrapy.Spider):
    name='game360'
    allowed_domains = ["360.cn"]
    start_urls=['http://u.360.cn/',]
    def parse(self, response):
        GetTime=time.strftime('%Y-%m-%d %H:',time.localtime(time.time()))+'00'
        print GetTime
        HotRankre=re.compile('renderRank\((.*),\s\'s_newrank')
        #('renderRank\((.*),\s\'s_downrank')
        DownloadRankre=re.compile('renderRank\((.*),\s\'s_downrank')
        BiaoShengRankre=re.compile('renderRank\((.*),\s\'s_jingrank')
        xiaobianRankre=re.compile('renderRank\((.*),\s\'s_xiaobian')
        res=[HotRankre,DownloadRankre,BiaoShengRankre,xiaobianRankre]
        x=1
        for r in res:
            print x
            m=r.search(response.body)
            rankslist=m.group(1)
            AllRanks=json.loads(rankslist)
            num=1
            for a in AllRanks:
                item=ChannelrankItem()
                if r==HotRankre:
                    item['RankType']=5
                if r==DownloadRankre:
                    item['RankType']=6
                if r==BiaoShengRankre:
                    item['RankType']=4
                if r==xiaobianRankre:
                    item['RankType']=7
                item['TopNow']=num
                item['GetTime']=GetTime
                item['GameName']=a['name']
                item['ChannelID']=2
                item['VersionID']=a['version_name']
                PackageSize=str(round(float(a['market']['360market']['size'])/float(1024)/float(1024),2))+'M'
                item['PackageSize']=PackageSize
                item['GameType']='未知'
                item['CompanyName']=a['company']
                item['DownloadNum']=a['total_download_count']
                item['iConURL']=a['logo']
                item['DownloadURL']=a['market']['360market']['download_url']
                item['PlatForm']=4
                item['Hot']=0
                item['HotTrend']='未知'
                item['Score']=a['poll']
                item['RunningType']='未知'
                item['From']=2
                item['WeekDownload']=int(a['week_download_count'])
                item['WebURL']='未知'
                item['Summary']='未知'
     
                num+=1
                yield item

class game360AppSpider(scrapy.Spider):
    name='game360App'
    allowed_domains = ["360.cn"]
    start_urls=['http://openbox.mobilem.360.cn/qcms/view/t/rank_game','http://openbox.mobilem.360.cn/html/data/rank/wy.json','http://openbox.mobilem.360.cn/html/data/rank/xy.json','http://openbox.mobilem.360.cn/html/data/rank/hot.json','http://openbox.mobilem.360.cn/html/data/rank/free.json']
    def parse(self, response):
        GetTime=time.strftime('%Y-%m-%d %H:',time.localtime(time.time()))+'00'
        print GetTime
        
        print response.url
        
        if response.url[-9:]=='rank_game':
            print 'xxxxxx'
            a=re.compile('G_data_dj=(.*?)</script').search(response.body).group(1)
            print a
            resutl=json.loads(re.compile('G_data_dj=(.*?)</script').search(response.body).group(1))
            
        else:
            resutl=json.loads(response.body)
        n=1
        for games in resutl:
            item=ChannelrankItem()

            
            if response.url[-7:-5]=='nk':
                item['RankType']=60 
		#item['RankType'] = self.RankType['单机']
            if response.url[-7:-5]=='wy':
                item['RankType']=61
            if response.url[-7:]=='NewGame':
                item['RankType']=62
            if response.url[-7:-5]=='ot':
                item['RankType']=63
            if response.url[-7:-5]=='ee':
                item['RankType']=64
            item['ChannelID']=2
            item['GetTime']=GetTime
            item['GameName']=games['name']
            item['TopNow']=n
            n+=1
            item['PackageSize']=str(round((float(games['size'])/float(1024)/float(1024)),2))+'M'
            item['GameType']='未知'
            item['VersionID']=games['version_code']
            item['DownloadNum']=0
            item['iConURL']=games['logo_url']
            item['WebURL']='未知'
            item['PlatForm']=1 
            item['DownloadURL']=games['down_url']
            item['Hot']=0
            item['HotTrend']='未知'
            item['RunningType']='未知'
            item['Score']=0.0 
            item['CompanyName']='未知'
            item['WeekDownload']=0
            item['Summary']='未知'
            item['From']=1
            yield item
            
            
                
                

        
        
   
