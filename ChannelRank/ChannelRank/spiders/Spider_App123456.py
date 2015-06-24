#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import scrapy
from ChannelRank.items import ChannelrankItem
import os
import sys
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re
import time

reload(sys)
sys.setdefaultencoding('utf8')

Get1=0
Get2=0
class Spider_App123456(scrapy.Spider):
    name = "App123456"

 


    

    def start_requests(self):
        device=['iPhone','iPad']
        iPhone_pop_id=['27','30','38']
        iPad_pop_id=['44','47','46']
        Now=int(time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S')))-7200
        showtime1=24#time.strftime('%H',time.localtime(Now))
        showtime2=24
        showdate=str(time.strftime("%Y-%m-%d",time.localtime(time.time())))
        genre_id=['6014']
        print 'xxxxxx'
        for i in device:
            if i ==device[0]:
                for a in iPhone_pop_id:


                    url='http://www.app12345.com/?area=cn&store=Apple%store&device=%s&pop_id=%s&showdate=%s&showtime=%s&genre_id=%s'%('%20S',i,a,showdate,showtime1,genre_id[0])
                    r=scrapy.Request(url, callback=self.parse)
                    r.meta['showtime']=showtime1
                    

                    Get1=0
                    yield r
                    print r
        
            else:
                for b in iPad_pop_id:


                
                    
                    url='http://www.app12345.com/?area=cn&store=Apple%store&device=%s&pop_id=%s&showdate=%s&showtime=%s&genre_id=%s'%('%20S',i,b,showdate,showtime2,genre_id[0])
                    
                    r=scrapy.Request(url, callback=self.parse)
                    r.meta['showtime']=showtime2
                    yield r
                    print r
                    Get2=0


    def parse(self, response):
        div=response.xpath('//div[@class="divleftpanel"]')
        dl_list=div.xpath('.//dl[@class="dldefault"]')
        print dl_list
        if dl_list==[]:
            print 'aaaaaaa'
            showtime0=response.meta['showtime']
            showtime2=showtime0-2
            Url_new=response.url.replace('showtime='+str(showtime0),'showtime='+str(showtime2))
            print Url_new
            r=scrapy.Request(Url_new,callback=self.parse)
            r.meta['showtime']=showtime2
            yield r
        
        for dl in dl_list:
            Get1=1
            Get2=1
            Hot_iConURL=''.join(dl.xpath('.//dt//div[@class="dvimg"]//a//img//@src').extract())
            Hot_GameName=''.join(dl.xpath('.//dd[@class="ddappname"]/text()').extract()[0].split('.')[1])
            Hot_TopNow=''.join(dl.xpath('.//dd[@class="ddappname"]/text()').extract()[0].split('.')[0])
            url_device=re.compile('device=(.*?)&').search(response.url).group(1)
            url_pop_id=re.compile('pop_id=(.*?)&').search(response.url).group(1)
            url_showdate=re.compile('showdate=(.*?)&').search(response.url).group(1)
            url_showtime=re.compile('showtime=(.*?)&').search(response.url).group(1)
            url_genre_id=re.compile('genre_id=(.*)').search(response.url).group(1)
            item=ChannelrankItem()
            item['ChannelID']=5
            item['GetTime']=str(time.strftime("%Y-%m-%d %H",time.localtime(time.time())))+':00:00'
            item['GameName']=Hot_GameName

            if url_pop_id=='27':
                item['RankType']=13
            elif url_pop_id=='30':
                item['RankType']=14
            elif url_pop_id=='38':
                item['RankType']=15
            elif url_pop_id=='44':
                item['RankType']=13
            elif url_pop_id=='47':
                item['RankType']=14
            elif url_pop_id=='46':
                item['RankType']=15

            item['TopNow']=Hot_TopNow
            item['PackageSize']='未知'
            
            if url_device=='iPad':
                item['PlatForm']=3
            else:
                item['PlatForm']=2
            
            item['GameType']='未知'
            item['VersionID']='未知'
            item['DownloadNum']='未知'
            item['iConURL']=Hot_iConURL
            item['DownloadURL']='未知'
            item['WebURL']='未知'
            item['RunningType']='未知'
            item['HotTrend']='未知'
            item['Hot']=0
            item['From']='2'
            item['Score']=0.0
            item['WeekDownload']='未知'
            item['Summary']='未知'
            item['CompanyName']='未知'
            yield item
