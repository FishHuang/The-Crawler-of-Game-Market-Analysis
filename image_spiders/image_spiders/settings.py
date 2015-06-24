# -*- coding: utf-8 -*-

# Scrapy settings for image_spiders project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'image_spiders'

SPIDER_MODULES = ['image_spiders.spiders']
NEWSPIDER_MODULE = 'image_spiders.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'image_spiders (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
	'image_spiders.pipelines.MyImagesPipeline': 1,
	'image_spiders.pipelines.ImageToDbPipeline': 2
}

#ITEM_PIPELINES = {'image_spiders.pipelines.MyImagesPipeline': 1}
IMAGES_STORE = '/data/GameRank/img'
