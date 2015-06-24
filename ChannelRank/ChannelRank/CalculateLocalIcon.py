#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import MySQLdb
import MySQLdb.cursors
import time
import sys
import pandas as pd
import pandas.io.sql as sql

reload(sys)
sys.setdefaultencoding('utf-8')

con=MySQLdb.connect(host="127.0.0.1",port=3307,user="root",passwd="",db="de_rank",charset="utf8")
cursor=con.cursor()

Now=int(time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S')))
Before=Now-7200
NowTime=time.strftime("%Y-%m-%d %H", time.localtime(Now))+':00:00'
BeforeTime=time.strftime("%Y-%m-%d %H", time.localtime(Before))+':00:00'

def getData(ChannelID,RankType,GetTime):
    getDataSql = 'select GameName,iConLocal from dc_rank where ChannelID='+str(ChannelID)+' and RankType='+str(RankType)+' and GetTime='+`str(GetTime)`
    getData = sql.read_sql(getDataSql,con)
    return getData

def getRankType():
    getRankType=[]
    getDataSql='select * from dc_RankType'
    cursor.execute(getDataSql)
    for line in cursor.fetchall():
        getRankType.append(line)
    return getRankType

for item in getRankType():
    ChannelID=item[2]
    RankType=item[0]
    iConLocal1=getData(ChannelID,RankType,NowTime)
    iConLocal2=getData(ChannelID,RankType,BeforeTime)
    iConLocal=pd.merge(iConLocal1,iConLocal2,on='GameName')
    for i in range(0,len(iConLocal.GameName)):
        print iConLocal.GameName[i]
        incertSql = 'update dc_rank set iConLocal="%s" where ChannelID=%s and RankType=%s and GameName="%s" and GetTime="%s"' % (str(iConLocal.iConLocal_y[i]),str(ChannelID),str(RankType),str(iConLocal.GameName[i]),str(NowTime))
        print incertSql
        cursor.execute(incertSql)
        print '=================insert success============='

