#!/bin/sh

cd `dirname $0`

d=`date +'%Y-%m-%d %H:00:00'`

echo 'start fill iConLocal'
nohup /data/GameRank/ChannelRank/ChannelRank/CalculateLocalIcon.py > /data/GameRank/ChannelRank/ChannelRank/MoveData.logs/MoveImg_${d}.log 2>&1 &
