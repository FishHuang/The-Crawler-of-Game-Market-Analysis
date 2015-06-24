#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import MySQLdb
import MySQLdb.cursors
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')

con1=MySQLdb.connect(host="127.0.0.1",port=3307,user="root",passwd="",db="de_rank",charset="utf8")
con2=MySQLdb.connect(host="127.0.0.1",port=3307,user="root",passwd="",db="de_GameRank_Trend",charset="utf8")
cursor1=con1.cursor()
cursor2 = con2.cursor(cursorclass=MySQLdb.cursors.DictCursor)

def getLocalNull(ChannelID):
    getNull = []
    getiConLocalNullSql = "select GetTime,GameName,ChannelID,RankType from dc_Rank_%s where iConLocal=''"%(str(ChannelID))
    print getiConLocalNullSql
    cursor2.execute(getiConLocalNullSql)
    for line in cursor2.fetchall():
        getNull.append(line)
    return getNull

def getLocalNoNull(GameName,ChannelID,RankType):
    getNoNull = []
    getiConLocalNoNullSql = "select iConLocal from dc_rank where GameName='%s' and ChannelID=%s and RankType=%s and iConLocal<>'' order by GetTime desc limit 1"%(str(MySQLdb.escape_string(GameName)),str(ChannelID),str(RankType))
    cursor1.execute(getiConLocalNoNullSql)
    for line in cursor1.fetchall():
        getNoNull.append(line)
    return getNoNull

for i in range(1,12):
    print i
    iConLocalNull = getLocalNull(i)
    for item in iConLocalNull:
        iConLocalNoNull = getLocalNoNull(item.get('GameName'),item.get('ChannelID'),item.get('RankType'))
        print iConLocalNoNull
        if len(iConLocalNoNull) != 0:
            InsectDataSql = 'update dc_Rank_%s set iConLocal = "%s" where GameName="%s" and ChannelID=%s and RankType=%s and iConLocal=""'%(str(i),str(iConLocalNoNull[0][0]),str(MySQLdb.escape_string(item.get('GameName'))),str(item.get('ChannelID')),str(item.get('RankType')))
            print InsectDataSql
            cursor2.execute(InsectDataSql)
            print '-----------fill success---------------'
        else:
            print '-----------had no iConLocal-----------'
