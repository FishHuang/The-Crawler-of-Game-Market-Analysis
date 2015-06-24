# -*- coding: utf-8 -*-

# Scrapy settings for ChannelRank project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ChannelRank'

SPIDER_MODULES = ['ChannelRank.spiders']
NEWSPIDER_MODULE = 'ChannelRank.spiders'
DOWNLOAD_DELAY = 0.2
DOWNLOAD_TIMEOUT = 60
RANDOMIZE_DOWNLOAD_DELAY = True
ITEM_PIPELINES = {
    'ChannelRank.pipelines.ChannelRankPipeline': 100
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ChannelRank (+http://www.yourdomain.com)'
