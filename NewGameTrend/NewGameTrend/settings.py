# -*- coding: utf-8 -*-

# Scrapy settings for NewGameTrend project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'NewGameTrend'

SPIDER_MODULES = ['NewGameTrend.spiders']
NEWSPIDER_MODULE = 'NewGameTrend.spiders'
ITEM_PIPELINES = {
    'NewGameTrend.pipelines.NewGameTrendPipeline': 100
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'NewGameTrend (+http://www.yourdomain.com)'
