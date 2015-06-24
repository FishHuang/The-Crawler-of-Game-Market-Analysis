# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewgametrendItem(scrapy.Item):
    ChannelId=scrapy.Field()
    OpenTime=scrapy.Field()
    GameName=scrapy.Field()
    ServerName=scrapy.Field()
    CompanyName=scrapy.Field()
    Hot=scrapy.Field()
    GameType=scrapy.Field()
    TestType=scrapy.Field()