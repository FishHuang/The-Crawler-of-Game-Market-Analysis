#!/bin/sh

cd `dirname $0`

d=`date +'%Y-%m-%d %H:00:00'`

echo 'start crawl UC9game'
nohup /usr/local/bin/scrapy crawl UC9game > /data/GameRank/ChannelRank/ChannelRank/logs/UC9game_${d}.log 2>&1 &

echo 'start crawl UC9gameNewgame'
nohup /usr/local/bin/scrapy crawl UC9gameNewgame > /data/GameRank/ChannelRank/ChannelRank/logs/UC9gameNewgame_${d}.log 2>&1 &

echo 'start crawl game360App'
nohup /usr/local/bin/scrapy crawl game360App > /data/GameRank/ChannelRank/ChannelRank/logs/game360App_${d}.log 2>&1 &

echo 'start crawl yyb'
nohup /usr/local/bin/scrapy crawl yyb > /data/GameRank/ChannelRank/ChannelRank/logs/yyb_${d}.log 2>&1 &

echo 'start crawl game91App'
nohup /usr/local/bin/scrapy crawl game91App > /data/GameRank/ChannelRank/ChannelRank/logs/game91App_${d}.log 2>&1 &

echo 'start crawl baidu'
nohup /usr/local/bin/scrapy crawl baidu > /data/GameRank/ChannelRank/ChannelRank/logs/baidu_${d}.log 2>&1 &

echo 'start crawl XiaoMi'
nohup /usr/local/bin/scrapy crawl XiaoMi > /data/GameRank/ChannelRank/ChannelRank/logs/XiaoMi_${d}.log 2>&1 &

echo 'start crawl PP_WAP'
nohup /usr/local/bin/scrapy crawl PP_WAP > /data/GameRank/ChannelRank/ChannelRank/logs/PP_WAP_${d}.log 2>&1 &

echo 'start crawl tongbu'
nohup /usr/local/bin/scrapy crawl tongbu > /data/GameRank/ChannelRank/ChannelRank/logs/tongbu_${d}.log 2>&1 &

echo 'start crawl XYZS_APP'
nohup /usr/local/bin/scrapy crawl XYZS_APP > /data/GameRank/ChannelRank/ChannelRank/logs/XYZS_APP_${d}.log 2>&1 &

echo 'start crawl itools'
nohup /usr/local/bin/scrapy crawl itools > /data/GameRank/ChannelRank/ChannelRank/logs/itools_${d}.log 2>&1 &

echo 'start crawl App123456'
nohup /usr/local/bin/scrapy crawl App123456 > /data/GameRank/ChannelRank/ChannelRank/logs/App123456_${d}.log 2>&1 &
