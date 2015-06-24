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

Now=int(time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S')))
NowTime=time.strftime("%Y-%m-%d %H", time.localtime(Now))+':00:00'
Before=Now-7200
BeforeTime=time.strftime("%Y-%m-%d %H", time.localtime(Before))+':00:00'

ErrorChannelID=[]
ErrorRankType=[]
ErrorTxt=[]
ErrorContent=[]

def getRankData(ChannelID,RankType,getTime):
    getDataState=[]
    getDataSql='select * from dc_rank where ChannelID=%s and GetTime="%s" and RankType=%s'%(str(ChannelID),str(getTime),str(RankType))
    cursor1.execute(getDataSql)
    return cursor1.fetchall()

def getChannelRankType():
    getRankType=[]
    getDataSql='select * from dc_RankType'
    cursor1.execute(getDataSql)
    for line in cursor1.fetchall():
        getRankType.append(line)
    return getRankType

def getDataState(ChannelID,RankType,getTime):
    getDataState=[]
    getDataSql='select * from dc_rank where ChannelID=%s and GetTime="%s" and RankType=%s'%(str(ChannelID),str(getTime),str(RankType))
    print getDataSql
    cursor1.execute(getDataSql)
    return len(cursor1.fetchall())

for j in getChannelRankType():
    g=j[0]
    i=j[2]
    if getDataState(i,g,NowTime)>0 and getDataState(i,g,NowTime)<=100:
        if getDataState(i,g,NowTime)>0:
            for line in getRankData(i,g,NowTime):
                InsectDataSql='insert into dc_Rank_'+str(i)+' (ChannelID,GetTime,GameName,RankType,TopNow,PackageSize,GameType,VersionID,DownloadNum,iConURL,PlatForm,DownloadURL,WebURL,RunningType,HotTrend,Hot,TerminalID,Score,WeekDownload,Summary,CompanyName,iConLocal) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update ChannelId=0'
                cursor2.execute(InsectDataSql,(str(line[0]),str(line[1]),str(line[2]),str(line[3]),str(line[4]),str(line[5]),str(line[6]),str(line[7]),str(line[8]),str(line[9]),str(line[10]),str(line[11]),str(line[12]),str(line[13]),str(line[14]),str(line[15]),str(line[16]),str(line[17]),str(line[18]),str(line[19]),str(line[20]),str(line[21])))
                print '==================into database succ==============='
        else:
            ErrorChannelID.append(i)
            ErrorRankType.append(g)
            ErrorTxt.append('Channel has no data')
    elif getDataState(i,g,NowTime)>100 and getDataState(i,g,NowTime)>=(getDataState(i,g,BeforeTime)*0.6):
        for line in getRankData(i,g,NowTime):
            InsectDataSql='insert into dc_Rank_'+str(i)+' (ChannelID,GetTime,GameName,RankType,TopNow,PackageSize,GameType,VersionID,DownloadNum,iConURL,PlatForm,DownloadURL,WebURL,RunningType,HotTrend,Hot,TerminalID,Score,WeekDownload,Summary,CompanyName,iConLocal) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update ChannelId=0'
            cursor2.execute(InsectDataSql,(str(line[0]),str(line[1]),str(line[2]),str(line[3]),str(line[4]),str(line[5]),str(line[6]),str(line[7]),str(line[8]),str(line[9]),str(line[10]),str(line[11]),str(line[12]),str(line[13]),str(line[14]),str(line[15]),str(line[16]),str(line[17]),str(line[18]),str(line[19]),str(line[20]),str(line[21])))
            print '==================into database succ==============='
    elif getDataState(i,g,NowTime)==0:
        ErrorChannelID.append(i)
        ErrorRankType.append(g)
        ErrorTxt.append('Channel has no Data!')
    else:
        ErrorChannelID.append(i)
        ErrorRankType.append(g)
        ErrorTxt.append('There is  a Data-Missing Value')

for i in ErrorChannelID:
    for j in ErrorRankType:
        for k in ErrorTxt:
            txt='GetTime=%s,ChannelID:%s,RankType:%s,Error Content:%s'%(str(NowTime),str(i),str(j),str(k))
            ErrorContent.append(txt)

ErrorContent=list(set(ErrorContent))

EmailText='\n'.join(ErrorContent)
