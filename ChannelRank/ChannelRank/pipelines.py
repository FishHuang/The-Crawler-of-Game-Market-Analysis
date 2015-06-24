# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi             #导入twisted的包
import MySQLdb.cursors
import sys
import MySQLdb
from datetime import datetime
import json
class ChannelRankPipeline(object):

    conn = None
    cur = None
    def __init__(self):
        self.conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db='de_rank',port=3307,charset='utf8')
        self.cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        if self.cur == None:
            print 'init  db conn failed'
            raise scrapy.exceptions.CloseSpider('init db conn failed')

    def process_item(self, item, spider):
        return self.process_spider(item)
    def process_spider(self,item):
        sql='insert ignore into dc_rank (ChannelID,GetTime,GameName,RankType,TopNow,PackageSize,GameType,VersionID,DownloadNum,iConURL,PlatForm,DownloadURL,WebURL,RunningType,Hot,HotTrend,TerminalID,Score,WeekDownload,Summary,CompanyName) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);' 
        self.cur.execute(sql,(str(item['ChannelID']),str(item['GetTime']),str(item['GameName']).strip().replace('"','').replace('\'',''),str(item['RankType']),str(item['TopNow']),str(item['PackageSize']),str(item['GameType']),str(item['VersionID']),str(item['DownloadNum']),str(item['iConURL']),str(item['PlatForm']),str(item['DownloadURL']),str(item['WebURL']),str(item['RunningType']),str(item['Hot']),str(item['HotTrend']),str(item['From']),str(item['Score']),str(item['WeekDownload']),str(item['Summary']),str(item['CompanyName'])))
        print '==================into database succ==============='
        return item
