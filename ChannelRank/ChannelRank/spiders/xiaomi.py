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

class XiaoMiAppSpider(scrapy.Spider):
    name='XiaoMi'
    allowed_domains = ["xiaomi.com"]
    start_urls=[]#'http://app.migc.xiaomi.com/cms/interface/v5/rankgamelist1.php?uid=20140225_32751932&platform=android&os=VIBEROM_V2.0_1443_ST_K860i&stampTime=1418696368000&density=320&imei=864737011730670&pageSize=20&versionCode=1822&cid=gamecenter_100_1_android|864737011730670&clientId=4defdedf04609830a391a3b4c1759069&vn=MIGAMEAPPSTAND_1.8.22&co=CN&page=1&macWifi=0012FEDCA40B&la=zh&ua=LENOVO%257CLenovo%2BK860i%257C4.2.2%257CJDQ39%257C17%257CK860i&carrier=unknown&rankId=2&mnc=&fuid=&mid=&imsi=&sdk=17&mac3g=&bid=701']
    cur = None
    curr_site_id = 0
   
    url=['http://app.migc.xiaomi.com/cms/interface/v5/rankgamelist1.php?platform=android&os=VIBEROM_V2.0_1443_ST_K860i&density=320&imei=864737011730670&pageSize=20&versionCode=1822&cid=gamecenter_100_1_android|864737011730670&clientId=4defdedf04609830a391a3b4c1759069&vn=MIGAMEAPPSTAND_1.8.22&co=CN&page=&macWifi=0012FEDCA40B&la=zh&ua=LENOVO%257CLenovo%2BK860i%257C4.2.2%257CJDQ39%257C17%257CK860i&carrier=unknown&rankId=2&mnc=&fuid=&mid=&imsi=&sdk=17&mac3g=&bid=701',]
    RankID=[2,3,12,13]
    for Rid in RankID:
        url='http://app.migc.xiaomi.com/cms/interface/v5/rankgamelist1.php?platform=android&os=VIBEROM_V2.0_1443_ST_K860i&density=320&imei=864737011730670&pageSize=20&versionCode=1822&cid=gamecenter_100_1_android|864737011730670&clientId=4defdedf04609830a391a3b4c1759069&vn=MIGAMEAPPSTAND_1.8.22&co=CN&page=1&macWifi=0012FEDCA40B&la=zh&ua=LENOVO%257CLenovo%2BK860i%257C4.2.2%257CJDQ39%257C17%257CK860i&carrier=unknown&rankId='+str(Rid)+'&mnc=&fuid=&mid=&imsi=&sdk=17&mac3g=&bid=701'
        start_urls.append(url)
    n1=1
    n2=1
    n3=1
    n4=1
   
   
    
    def parse(self, response):

        
        
        
        
        GetTime=time.strftime('%Y-%m-%d %H:',time.localtime(time.time()))+'00'
        print 'yyyy'
        print GetTime
        print 'yyyy'
        result=json.loads(response.body)
        #x=self.start_request
        #print self.start_request
        
        #if response.has_key('gameList'):
            
        print response.url
   
        if result.has_key('gameList'):
            page=int(re.findall('page=(.*?)&',response.url)[0])
            print page
            GetRankid=int(re.findall('rankId=(.*?)&',response.url)[0])
            GameList=result['gameList']
            print 'aaaaaa'
            print GetRankid
            print 'bbbbbbs'
            if GetRankid==2:
                for games in GameList:
                    item=ChannelrankItem()
                    item['ChannelID']=4
                    item['GetTime']=GetTime
                    item['GameName']=games['displayName']
                    item['RankType']=9
                    item['TopNow']=self.n1
                    self.n1+=1
                    item['PackageSize']=str(round(float(games['apkSize'])/float(1024)/float(1024),2))+'M'
                    item['GameType']=games['className']
                    item['VersionID']=games['versionName']
                    item['DownloadNum']=int(games['downloadCount'])
                    item['DownloadURL']=games['gameApk']
                    item['iConURL']=games['icon']
                    item['WebURL']='δ֪'
                    item['Hot']=0
                    item['HotTrend']='δ֪'
                    item['RunningType']='δ֪'
                    item['Score']=games['ratingScore']
                    item['From']=1
                    item['CompanyName']=games['publisherName']
                    GetWeekDownload='δ֪'
                    item['WeekDownload']=GetWeekDownload
                    item['Summary']=games['introduction']

                    item['PlatForm']=1
                    yield item
                    
                    
                    
     
                
            if GetRankid==3:
                n=1
                for games in GameList:
                    item=ChannelrankItem()
                    item['ChannelID']=4
                    item['GetTime']=GetTime
                    item['GameName']=games['displayName']
                    item['RankType']=10
                    item['TopNow']=self.n2
                    self.n2+=1
                    item['PackageSize']=str(round(float(games['apkSize'])/float(1024)/float(1024),2))+'M'
                    item['GameType']=games['className']
                    item['VersionID']=games['versionName']
                    item['DownloadNum']=int(games['downloadCount'])
                    item['DownloadURL']=games['gameApk']
                    item['iConURL']=games['icon']
                    item['WebURL']='δ֪'
                    item['Hot']=0
                    item['HotTrend']='δ֪'
                    item['RunningType']='δ֪'
                    item['Score']=games['ratingScore']
                    item['From']=1
                    item['CompanyName']=games['publisherName']
                    GetWeekDownload='δ֪'
                    item['WeekDownload']=GetWeekDownload
                    item['Summary']=games['introduction']
                    item['PlatForm']=1

                    yield item
                    
                   
            if GetRankid==12:
                n=1
                for games in GameList:
                    item=ChannelrankItem()
                    item['ChannelID']=4
                    item['GetTime']=GetTime
                    item['GameName']=games['displayName']
                    item['RankType']=11
                    item['TopNow']=self.n3
                    self.n3+=1
                    item['PackageSize']=str(round(float(games['apkSize'])/float(1024)/float(1024),2))+'M'
                    item['GameType']=games['className']
                    item['VersionID']=games['versionName']
                    item['DownloadNum']=int(games['downloadCount'])
                    item['DownloadURL']=games['gameApk']
                    item['iConURL']=games['icon']
                    item['WebURL']='δ֪'
                    item['Hot']=0
                    item['HotTrend']='δ֪'
                    item['RunningType']='δ֪'
                    item['Score']=games['ratingScore']
                    item['From']=1
                    item['CompanyName']=games['publisherName']
                    GetWeekDownload='δ֪'
                    item['WeekDownload']=GetWeekDownload
                    item['Summary']=games['introduction']
                    item['PlatForm']=1
                    yield item
                    
    
            if GetRankid==13:
                n=1
                for games in GameList:
                    item=ChannelrankItem()
                    item['ChannelID']=4
                    item['GetTime']=GetTime
                    item['GameName']=games['displayName']
                    item['RankType']=12
                    item['TopNow']=self.n4
                    self.n4+=1
                    item['PackageSize']=str(round(float(games['apkSize'])/float(1024)/float(1024),2))+'M'
                    item['GameType']=games['className']
                    item['VersionID']=games['versionName']
                    item['DownloadNum']=int(games['downloadCount'])
                    item['DownloadURL']=games['gameApk']
                    item['iConURL']=games['icon']
                    item['WebURL']='δ֪'
                    item['Hot']=0
                    item['HotTrend']='δ֪'
                    item['RunningType']='δ֪'
                    item['Score']=games['ratingScore']
                    item['From']=1
                    item['CompanyName']=games['publisherName']
                    GetWeekDownload='δ֪'
                    item['WeekDownload']=GetWeekDownload
                    item['Summary']=games['introduction']
                    item['PlatForm']=1
                    yield item

            response.meta['page']=page
            r=response.meta
            page=r['page']
            page0=page
            page+=1
            url=response.url.replace('page='+str(page0),'page='+str(page))
            r=scrapy.Request(url, callback=self.parse)
            yield r
        
        
        
        """
    z
        if response.has_key('gameList'):
            
       
        if result['LIST'] and  len(result['LIST']) > 0:
            xxxx item   
            yield item
            
            page = response.meta['page']
            page += 1
            page_str = 'page=%d' % response.meta['page']
            new_page_str = 'page=%d' % (page)
            response.url.replace(page_str,new_page_str)
            url = response.url.
            
            r = scrapy.Request(url,callback=self.parse)
            r.meta['page'] = page
            yield r"""
            
                
            
        
        """List=result['Result']['items']
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
            item['DownloadNum']=l['downloadUrl']
            item['iConURL']=l['icon']
            item['PlatForm']=1
            item['DownloadURL']='δ֪'
            item['Hot']=0
            item['HotTrend']=0
            item['RunningType']='δ֪'
            item['From']='App'
            item['CompanyName']=l['author']
            Num+=1
            yield item"""
            
            


       
