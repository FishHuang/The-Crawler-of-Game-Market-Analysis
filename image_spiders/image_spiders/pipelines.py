# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
import MySQLdb
import scrapy
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

class ImageToDbPipeline(object):
        conn = None
        cur = None

        def __init__(self):

                self.conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db='de_rank',port=3307,charset='utf8')
                self.conn.autocommit(1)
                self.cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
                if self.cur == None:
                        print 'init indicator pipeline db conn failed'
                        raise scrapy.exceptions.CloseSpider('init indicator pipeline db conn failed')

        def process_item(self, item, spider):
		Now=int(time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S')))
		NowTime=time.strftime("%Y-%m-%d %H", time.localtime(Now))+':00:00'
		if item:
			for img in item['images']:
				print item['game_name']
				sql = 'update dc_rank set iConLocal="%s" where ChannelID=%d and RankType=%d and GameName="%s" and GetTime="%s"' % (img['path'],item['channel_id'],item['rank_type'],item['game_name'],str(NowTime))
				print sql
				self.cur.execute(sql)
		return item

class MyImagesPipeline(ImagesPipeline):
 	def file_path(self, request, response=None, info=None):
		path = 'game_icon/%d/%s.jpg' % (request.meta['channel_id'],request.meta['img_name'])
		print 'path:%s'% path
		return path

	def get_media_requests(self, item, info):
		print item
 		for image_url in item['image_urls']:
 			r = scrapy.Request(image_url)
			r.meta['channel_id'] = item['channel_id']
			r.meta['img_name'] = item['img_name']
			yield r

