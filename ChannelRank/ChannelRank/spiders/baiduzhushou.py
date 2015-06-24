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
    name='baidu'
    allowed_domains = ["baidu.com"]
    start_urls=['http://m.baidu.com/appsrv?uid=_aSei_OYv8_KOSa6_a2DulaX2t0fi28ujivqtja5HiqjuHi3_avWiguH2ig5u2iU3dqqC&native_api=1&psize=3&abi=armeabi-v7a&cll=_asv8_av28jFRvaEga2iNgaO-8m6xqqqB&usertype=0&is_support_webp=true&ver=16785162&from=1000606p&cct=q8vJkluJVagxRSiIqOSCkluheaghMHf3odfqA&pc_channel=&operator=&network=WF&pkname=com.baidu.appsearch&country=CN&cen=cuid_cut_cua_uid&gms=false&platform_version_id=17&firstdoc=&name=game&action=ranklist&pu=cua%40_avLC_uw2i4SywoUfpw1zyaBsizluL8bxLqqC%2Cosname%40baiduappsearch%2Cctv%401%2Ccfrom%401000606p%2Ccuid%40_aSei_OYv8_KOSa6_a2DulaX2t0fi28ujivqtja5Hi6ouviJ0u24iguGv8_quviE_a20fqqHB%2Ccut%405ymy6fprsPYBav6qyaXrizubL8g4IQu85t3-PqqHB&language=zh&apn=&&native_api=1&pn=0',]
    #for rid in range(1,9):
        #url='http://m5.qq.com/rank/apps.htm?cateId=-1&limit=100&orgame=2&rankType='+str(rid)+'&start=0'
        #start_urls.append(url)
    n=1
    def parse(self, response):
        
        GetTime=time.strftime('%Y-%m-%d %H:',time.localtime(time.time()))+'00'
        print 'yyyy'
        print GetTime
        print 'yyyy'
        result=json.loads(response.body)['result']
        GetPageid=int(response.url[-1])
        print GetPageid
        print result
        data=result['data']
        if result['hasNextPage']==True:
            for d in data:
                item=ChannelrankItem()
                item['ChannelID']=10
                item['GetTime']=GetTime
                item['RankType']=40
                item['TopNow']=self.n
                self.n+=1 
                item['GameName']=d['itemdata']['sname']
                item['PackageSize']=str(round(float(d['itemdata']['sizeb'])/float(1024)/float(1024),2))+'M'
                item['GameType']=d['itemdata']['catename']
                item['VersionID']=d['itemdata']['versionname']
                item['DownloadNum']=d['itemdata']['display_download']
                item['PlatForm']=1
                item['WebURL']='未知'
                item['Hot']=d['itemdata']['popularity']
                item['HotTrend']='未知'
                item['iConURL']=d['itemdata']['icon']
                item['DownloadURL']=d['itemdata']['download_inner']
                item['RunningType']='未知'
                item['Score']=d['itemdata']['score']
                item['From']=1
                item['WeekDownload']=0 
                item['CompanyName']='未知'
                item['Summary']=d['itemdata']['manual_short_brief']
                yield item
                
                #item['PackageSize']=
                
            pageid0=GetPageid
            GetPageid+=1
            url=response.url.replace('pn='+str(pageid0),'pn='+str(GetPageid))
            r=scrapy.Request(url, callback=self.parse)
            yield r
        
            
                

            
        
        """n=1
        for games in result:
            item=ChannelrankItem()
            item['ChannelID']=6
            item['GetTime']=GetTime
            item['GameName']=games['appName']
            
            item['TopNow']=n
            n+=1
            item['PackageSize']=str(round(float(games['fileSize'])/float(1024)/float(1024),2))+'M'
            item['GameType']=games['categoryName']
            item['VersionID']=games['versionName']
            item['DownloadNum']=games['appDownCount']
            item['iConURL']=games['iconUrl']
            item['DownloadURL']=games['apkUrl']
            item['PlatForm']=1 
            item['WebURL']='δ?'
            item['Hot']=0
            item['HotTrend']='δ?'
            item['RunningType']='δ?'
            item['Score']=round(games['averageRating'],2)
            item['From']=4
            item['CompanyName']=games['authorName']
            item['WeekDownload']=0
            item['Summary']=games['editorIntro']
            yield item"""
            
           
            

            
            
            
        
