#!/bin/sh

cd `dirname $0`

d=`date +'%Y-%m-%d %H:00:00'`

echo 'start crawl img_downloader'
nohup /usr/local/bin/scrapy crawl img_downloader > /data/GameRank/ChannelRank/ChannelRank/logs/img_downloader_${d}.log 2>&1 &
