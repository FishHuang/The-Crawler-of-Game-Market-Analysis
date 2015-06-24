#!/bin/sh

cd `dirname $0`

d=`date +'%Y-%m-%d %H:00:00'`

echo 'start MoveData to dc_GameRank_Trend'
nohup /data/GameRank/ChannelRank/ChannelRank/MoveData.py > /data/GameRank/ChannelRank/ChannelRank/MoveData.logs/MoveData_${d}.log 2>&1 &

echo 'start calculate DataEye Rank'
nohup /data/GameRank/ChannelRank/ChannelRank/DataEyeRank.py > /data/GameRank/ChannelRank/ChannelRank/MoveData.logs/DataEyeRank_${d}.log 2>&1 &
