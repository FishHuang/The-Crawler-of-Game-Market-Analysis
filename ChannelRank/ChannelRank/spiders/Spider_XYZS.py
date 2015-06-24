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
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8') 

class Spider_XYZS(scrapy.Spider):
    
    name = "XYZS"
    allowed_domains = ["xyzs.com"]
    start_urls = [
    'http://www.xyzs.com/top/game/',
    'http://ipad.xyzs.com/top/game/',
    ]

    def parse(self, response):
        list_body=response.xpath('//div[@class="in_top10_list"]//div[@class="list_body"]')
        for body in list_body:
            li_list=body.xpath('.//div[@class="t_list"]//ul//li')
            for li in li_list:
                TopNow=re.compile('icon_(.*?)$').search(li.xpath('.//div[@class="t_p1"]//span//@class').extract()[0]).group(1)
                GameName=''.join(li.xpath('.//div[@class="t_p2"]//a/text()').extract())
                DownloadNum=''.join(li.xpath('.//div[@class="t_p3"]//span/text()').extract())
                iConURL=''.join(li.xpath('.//div[@class="t_p4"]//div[@class="t_pho"]//a//img//@src').extract())
                VersionID=''.join(li.xpath('.//div[@class="t_info"]/text()').extract()[0].replace('\r',' ').replace('\n','').replace(' ','')[3:])
                PackageSize=''.join(li.xpath('.//div[@class="t_info"]/text()').extract()[1].replace('\r',' ').replace('\n','').replace(' ','')[3:])
                item=ChannelrankItem()
                item['ChannelID']=7
                item['GetTime']=str(time.strftime("%Y-%m-%d %H",time.localtime(time.time())))+':00:00'
                item['GameName']=GameName

                if body.xpath('.//div[@class="t_title"]//h5//span//a//@href').extract()[0]=='http://www.xyzs.com/game/action-0-time-1.html':
                    item['RankType']=24
                elif body.xpath('.//div[@class="t_title"]//h5//span//a//@href').extract()[0]=='http://www.xyzs.com/game/arcade-0-time-1.html':
                    item['RankType']=25
                elif body.xpath('.//div[@class="t_title"]//h5//span//a//@href').extract()[0]=='http://www.xyzs.com/game/puzzle-0-time-1.html':
                    item['RankType']=26
                elif body.xpath('.//div[@class="t_title"]//h5//span//a//@href').extract()[0]=='http://www.xyzs.com/game/racing-0-time-1.html':
                    item['RankType']=27
                elif body.xpath('.//div[@class="t_title"]//h5//span//a//@href').extract()[0]=='http://www.xyzs.com/game/roleplaying-0-time-1.html':
                    item['RankType']=28
                elif body.xpath('.//div[@class="t_title"]//h5//span//a//@href').extract()[0]=='http://www.xyzs.com/game/simulation-0-time-1.html':
                    item['RankType']=29
                else:
                    break

                item['TopNow']=TopNow
                item['PackageSize']=PackageSize
                item['GameType']=body.xpath('.//div[@class="t_title"]//h5//span//a[@target="_blank"]/text').extract()
                item['VersionID']=VersionID
                item['DownloadNum']=DownloadNum
                item['iConURL']=iConURL

                if response.url=='http://www.xyzs.com/top/game/':
                    item['PlatForm']=2
                else:
                    item['PlatForm']=3

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
