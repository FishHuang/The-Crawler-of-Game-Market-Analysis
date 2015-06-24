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

class Spider_tongbu(scrapy.Spider):
    
    name = "tongbu"
    allowed_domains = ["tongbu.com"]
    start_urls = [
    'http://app.tongbu.com/iphone-paihang-tb-hot-6014-all/',
    'http://app.tongbu.com/iphone-paihang-tb-hot-6014-week/',
    'http://app.tongbu.com/iphone-paihang-tb-hot-6014-month/',
    'http://app.tongbu.com/ipad-paihang-tb-hot-6014-all/',
    'http://app.tongbu.com/ipad-paihang-tb-hot-6014-week/',
    'http://app.tongbu.com/ipad-paihang-tb-hot-6014-month/',
    ]

    def parse(self, response):
        url_type=re.compile('com\/(.*)-paihang').search(response.url).group(1)
        free_div_list=response.xpath('//div[@class="top-pod"]').xpath('.//div[@class="top-list free"]')
        nofree_div_list=response.xpath('//div[@class="top-pod"]').xpath('.//div[@class="top-list nofree"]')
        free_li_list=free_div_list.xpath('.//ul//li')
        for free_li in free_li_list:
            if free_li_list.index(free_li)<3:
                TopNow=''.join(free_li.xpath('.//span/text()').extract())
            else:
                TopNow=''.join(free_li.xpath('.//b/text()').extract())
            iConURL=''.join(free_li.xpath('.//a[@class="icon"]//img//@lz_src').extract())
            GameName=''.join(free_li.xpath('.//div[@class="info"]//div[@class="title"]//a/text()').extract())
            item=ChannelrankItem()
            item['ChannelID']=9
            item['GetTime']=str(time.strftime("%Y-%m-%d %H",time.localtime(time.time())))+':00:00'
            item['GameName']=GameName
            if response.url=='http://app.tongbu.com/iphone-paihang-tb-hot-6014-all/' or response.url=='http://app.tongbu.com/ipad-paihang-tb-hot-6014-all/':
                item['RankType']=30
            elif response.url=='http://app.tongbu.com/iphone-paihang-tb-hot-6014-week/' or response.url=='http://app.tongbu.com/ipad-paihang-tb-hot-6014-week/':
                item['RankType']=32
            elif response.url=='http://app.tongbu.com/iphone-paihang-tb-hot-6014-month/' or response.url=='http://app.tongbu.com/ipad-paihang-tb-hot-6014-month/':
                item['RankType']=34
            item['TopNow']=TopNow
            item['PackageSize']='未知'
            item['GameType']='未知'
            item['VersionID']='未知'
            item['DownloadNum']='未知'
            item['iConURL']=iConURL

            if url_type=='iphone':
                item['PlatForm']=2
            elif url_type=='ipad':
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

        nofree_li_list=nofree_div_list.xpath('.//ul//li')
        for nofree_li in nofree_li_list:
            if nofree_li_list.index(nofree_li)<3:
                TopNow=''.join(nofree_li.xpath('.//span/text()').extract())
            else:
                TopNow=''.join(nofree_li.xpath('.//b/text()').extract())
            iConURL=''.join(nofree_li.xpath('.//a[@class="icon"]//img//@lz_src').extract())
            GameName=''.join(nofree_li.xpath('.//div[@class="info"]//div[@class="title"]//a/text()').extract())
            item=ChannelrankItem()
            item['ChannelID']=9
            item['GetTime']=str(time.strftime("%Y-%m-%d %H",time.localtime(time.time())))+':00:00'
            item['GameName']=GameName
            if response.url=='http://app.tongbu.com/iphone-paihang-tb-hot-6014-all/' or response.url=='http://app.tongbu.com/ipad-paihang-tb-hot-6014-all/':
                item['RankType']=31
            elif response.url=='http://app.tongbu.com/iphone-paihang-tb-hot-6014-week/' or response.url=='http://app.tongbu.com/ipad-paihang-tb-hot-6014-week/':
                item['RankType']=33
            elif response.url=='http://app.tongbu.com/iphone-paihang-tb-hot-6014-month/' or response.url=='http://app.tongbu.com/ipad-paihang-tb-hot-6014-month/':
                item['RankType']=35
            item['TopNow']=TopNow
            item['PackageSize']='未知'
            item['GameType']='未知'
            item['VersionID']='未知'
            item['DownloadNum']='未知'
            item['iConURL']=iConURL

            if url_type=='iphone':
                item['PlatForm']=2
            elif url_type=='ipad':
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
