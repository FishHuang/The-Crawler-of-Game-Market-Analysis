#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import scrapy
from scrapy import log
import re
import MySQLdb
import json
import datetime
from image_spiders.items import *
import sys
import time
import hashlib

reload(sys)
sys.setdefaultencoding('utf8')

class ImgSpider(scrapy.Spider):
	name = 'img_downloader'
	start_urls = []
	conn = None
	cur = None	

	def __init__(self,*args,**kwargs):
		self.conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="de_rank",port=3307,charset='utf8')
        	self.conn.autocommit(1)
		self.cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)


	def start_requests(self):
		yield scrapy.Request('http://www.baidu.com',callback=self.parse)	


	def parse(self,response):
		Now=int(time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S')))
		NowTime=time.strftime("%Y-%m-%d %H", time.localtime(Now))+':00:00'
		for i in range(1,12):
            		sql = 'select * from dc_rank where ChannelID=%s and iConLocal="" and GetTime="%s"'%(str(i),str(NowTime))
            		print sql
            		self.cur.execute(sql)
            		for item in self.cur.fetchall():
             	   		url = item['iConURL']
                		img = ImageItem()
                		img['image_urls']=[]
                		img['image_urls'].append(url)
               			img['channel_id']=item['ChannelID']
				img['rank_type']=item['RankType']
				img['game_name']=item['GameName']
				myMd5 = hashlib.md5()
				myMd5.update(item['iConURL'][0:])
				myMd5_Digest = myMd5.hexdigest()
				img_name = myMd5_Digest
				img['img_name'] = img_name
				print img_name
                		yield img

