# -*- coding: utf-8 -*-
import sys
sys.path.append('F:\Py\Splider_all\ChannelRank')
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
import MySQLdb



class UC9gameSpider(scrapy.Spider):
    name='UC9game'
    allowed_domains = ["9game.cn"]
    start_urls=['http://www.9game.cn/rank/',]
        
    def parse(self, response):
        GetTime=time.strftime('%Y-%m-%d %H:',time.localtime(time.time()))+'00'
 

        Box=response.xpath('//div[@class="box-text"]//div[@class="game-rank-con"]')
        for b in Box:
            rank=b.xpath('.//ul[@class="game-poker "]//li[contains(@class,"")]')
            
            for r in rank:
            
            
                GameType_PackageSize=''.join(r.xpath('.//p[@class="type"]/text()').extract())
                TopNow_GameName=''.join(r.xpath('.//a[@class="info"]//p/text()').extract())
                iCon=r.xpath('.//a[@class="info"]/img/@src').extract()
                Apk=r.xpath('.//a[@class="down"]/@href').extract()
                Web=r.xpath('.//a[@class="info"]/@href').extract()
                TopNow_GameName1=TopNow_GameName.split('.')
                print TopNow_GameName1[0]
                item=ChannelrankItem()
                item['GameType']=GameType_PackageSize[0:2]
                item['PackageSize']=GameType_PackageSize[5:]
                item['TopNow']=TopNow_GameName1[0]
                item['GameName']=''.join(TopNow_GameName1[1:])
                item['Hot']=0
                item['ChannelID']=1
                item['RankType']=1
                item['PlatForm']=4
                item['VersionID']='未知'
                item['DownloadNum']='未知'
                item['GetTime']=GetTime
                item['iConURL']=''.join(iCon)
                item['WebURL']=''.join(Web)
                item['DownloadURL']=''.join(Apk)
                item['RunningType']='未知'
                item['HotTrend']='未知'
                item['From']=2
                item['CompanyName']='未知'
                item['Summary']='未知'
                item['WeekDownload']=0
                item['Score']=0.0
                yield item
                
class UC9game2Spider(scrapy.Spider):
    name='UC9gameNewgame'
    allowed_domains = ["9game.cn"]
    start_urls=['http://www.9game.cn/xyrb/1_0/','http://www.9game.cn/xyrb/2_0/','http://www.9game.cn/xyrb/3_0/']

    for i in range(1,11):
        urls='http://www.9game.cn/xyqdb/'+str(i)+'_0/'
        start_urls.append(urls)


        

        

        
    def parse(self, response):
        GetTime=time.strftime('%Y-%m-%d %H:',time.localtime(time.time()))+'00'

        print response.url
        Trs=response.xpath('//div[@class="box hope-rank-con"]//div[@class="box-text"]//table//tr')
        x=0
       
        for tr in Trs:
            print x
            if x>0:
                print x
                item=ChannelrankItem()
                GameName=''.join(tr.xpath('.//td[@class="name"]//a[@class="name"]//text()').extract())
                GameType=''.join(tr.xpath('.//td[@class="type"]//text()').extract())
                Hot=''.join(tr.xpath('.//td[@class="hottr hot"]//span//text()').extract())
                HotTrend=''.join(tr.xpath('.//td[@class="hottr hot"]//span//@class').extract())
                RunningType=''.join(tr.xpath('.//td[@class="time time1"]//div[@class="t"]//text()').extract())
                
           

                
                
                if  response.url[22]=='q':
                    RunningType=''.join(tr.xpath('.//td[@class="time time1"]//div[@class="t"]//text()').extract())
                if  response.url[22]=='r':
                    RunningType=''.join(tr.xpath('.//td[@class="static"]//span[@class="p"]//text()').extract())
                WebURLPath=tr.xpath('.//td[@class="name"]//a//@href').extract()
                WebURL='www.9game.cn'+''.join(WebURLPath)
                TopNow=''.join(tr.xpath('.//td[contains(@class,"num ")]//span[@class="n "]//text()').extract())
          
                item['GameType']=GameType
                item['PackageSize']='未知'
                item['TopNow']=TopNow
                item['GameName']=GameName
                item['Hot']=Hot
                item['ChannelID']=1
                item['PlatForm']=4
                item['VersionID']='未知'
                if response.url[22]=='q':
                    item['RankType']=3
                if response.url[22]=='r':
                    item['RankType']=2
                item['DownloadNum']='未知'
                item['GetTime']=GetTime
                item['iConURL']='未知'
                item['WebURL']=WebURL
                item['DownloadURL']='未知'
                item['RunningType']=RunningType
                item['HotTrend']=HotTrend
                item['From']=2
                item['CompanyName']='未知'
                item['WeekDownload']=0
                item['Summary']='未知'
                item['Score']=0.0
                GameidStr=''.join(tr.xpath('.//td[@class="name"]//a//@data-statis').extract())
                
                GameId=GameidStr.split('-')[-1]
                GetiConURL='http://www.9game.cn/suggest4pc.html?kwd='+str(GameName)+'&limit=1'
                gid=scrapy.Request(GetiConURL,meta={'GameId':GameId,'item':item},callback=self.parse_icon)
                yield gid

   
            x+=1
    def parse_icon(self,response):
        
        GetiConURL=json.loads(response.body)
       
        item=ChannelrankItem()
        for g in GetiConURL:
            print g
            iConURL='http://image.game.uc.cn/'+g['image']
                
            
            response.meta['item']['iConURL']=iConURL
            print 'xxxxxxxxx'
            print response.meta['item']
            print 'yyyyyyyyy'
            yield response
            
        item=response.meta['item']
        yield item
        
  
            


        
        
        
        
        
          
        
            
            
            

    
          
         
