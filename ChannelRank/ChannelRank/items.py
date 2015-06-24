# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChannelrankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ChannelID=scrapy.Field()
    GetTime=scrapy.Field()
    GameName=scrapy.Field()
    RankType=scrapy.Field()
    TopNow=scrapy.Field()
    PackageSize=scrapy.Field()
    GameType=scrapy.Field()
    VersionID=scrapy.Field()
    DownloadNum=scrapy.Field()
    iConURL=scrapy.Field()
    PlatForm=scrapy.Field()
    DownloadURL=scrapy.Field()
    WebURL=scrapy.Field()
    RunningType=scrapy.Field()
    Hot=scrapy.Field()
    HotTrend=scrapy.Field()
    Score=scrapy.Field()
    From=scrapy.Field()
    CompanyName=scrapy.Field()
    WeekDownload=scrapy.Field()
    Summary=scrapy.Field()
   