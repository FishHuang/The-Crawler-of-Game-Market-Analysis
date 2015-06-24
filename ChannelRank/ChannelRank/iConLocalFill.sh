#!/bin/sh

cd `dirname $0`

d=`date +'%Y-%m-%d %H:00:00'`

echo 'start iConLocal fill'
nohup /data/GameRank/ChannelRank/ChannelRank/iConLocalFill.py > /data/GameRank/ChannelRank/ChannelRank/MoveData.logs/iConLocalFill_${d}.log 2>&1 &
