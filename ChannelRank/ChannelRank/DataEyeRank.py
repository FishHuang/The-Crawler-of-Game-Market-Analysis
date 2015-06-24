#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import MySQLdb
import MySQLdb.cursors
import pandas as pd
import pandas.io.sql as sql
import time
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

con=MySQLdb.connect(host="127.0.0.1",port=3307,user="root",passwd="",db="de_GameRank_Trend",charset="utf8")
con1=MySQLdb.connect(host="127.0.0.1",port=3307,user="root",passwd="",db="de_rank",charset="utf8")
cursor=con.cursor()
cursor1=con1.cursor()


GetTime=time.strftime('%Y-%m-%d %H:',time.localtime(time.time()))+'00'
def GetRanks(ChannelID,RankType):
    
    
    GetRanksSql='select GameName,TopNow,iConURL,iConLocal from dc_rank where TopNow<=30 and  ChannelID='+str(ChannelID)+' and RankType='+str(RankType)+' and GetTime='+`str(GetTime)`

    Frame=sql.read_sql(GetRanksSql,con1)
    return Frame

def GetDataEyeRank(cid):
    Rank0=pd.DataFrame()
    for c in cid:

        Rank1=GetRanks(c[0],c[1])

        Rank0=pd.concat([Rank0,Rank1])
        
    DealBrackets1=Rank0.GameName.str.replace(u'\(.*','')
    DealBrackets2=DealBrackets1.str.replace(u'（.*','')
    Rank0.GameName=DealBrackets2    
    
    URLS=Rank0.drop('TopNow',axis=1)
    Rank2=Rank0.drop('iConURL',axis=1)
    Rank=Rank2.pivot_table(index=['GameName'],aggfunc=sum).sort_index(by='TopNow')

    GetTimes=[]
    rank=[]
    DataEyeType=[]
    
    n=0
    for i in range(1,len(Rank)+1):
        n+=1

        rank.append(i)
        GetTimes.append(GetTime)

        DataEyeType.append(c[2])

    Rank.insert(1,'GetTime',GetTimes)
    Rank.insert(2,'RankID',DataEyeType)
    Rank.insert(3,'GameName',Rank.index)
    Rank.insert(4,'NewTopNow',rank)
   
    
    Rank=pd.merge(Rank,URLS,on='GameName')
    


    return Rank

DownloadRanks=[(4,9,65),(8,37,65),(7,45,65)]
NewGameRanks=[(2,62,66),(4,10,66),(4,12,66)]
HotGameRanks=[(5,15,67),(6,20,67),(2,63,67)]

    
DataEyeDownloadRank=GetDataEyeRank(DownloadRanks)
DataEyeNewGameRank=GetDataEyeRank(NewGameRanks)
DataEyeHotGameRank=GetDataEyeRank(HotGameRanks)
  



for i in range(0,len(DataEyeHotGameRank)):

    if i!=len(DataEyeHotGameRank)-1:

        if DataEyeHotGameRank.NewTopNow[i]==DataEyeHotGameRank.NewTopNow[i+1]:
            continue


   
    SQL='insert into dc_DataEyeRank (RankType,GetTime,GameName,TopNow,iConURL,iConLocal) values ( '+`str(DataEyeHotGameRank.RankID[i])`+','+`str(DataEyeHotGameRank.GetTime[i])`+',"'+DataEyeHotGameRank.GameName[i]+'",'+`str(DataEyeHotGameRank.NewTopNow[i])`+',"'+DataEyeHotGameRank.iConURL[i]+'","'+DataEyeHotGameRank.iConLocal[i]+'") on duplicate key update TopNow=0'
 
    print SQL
    cursor.execute(SQL)
    con.commit()
    print 'Insert OK'
    print i

for i in range(0,len(DataEyeNewGameRank)):
    
    if i!=len(DataEyeNewGameRank)-1:

        if DataEyeNewGameRank.NewTopNow[i]==DataEyeNewGameRank.NewTopNow[i+1]:
            continue


    
    SQL='insert into dc_DataEyeRank (RankType,GetTime,GameName,TopNow,iConURL,iConLocal) values ( '+`str(DataEyeNewGameRank.RankID[i])`+','+`str(DataEyeNewGameRank.GetTime[i])`+',"'+DataEyeNewGameRank.GameName[i]+'",'+`str(DataEyeNewGameRank.NewTopNow[i])`+',"'+DataEyeNewGameRank.iConURL[i]+'","'+DataEyeNewGameRank.iConLocal[i]+'") on duplicate key update TopNow=0'


    cursor.execute(SQL)
    con.commit()
    print 'Insert OK'
for i in range(0,len(DataEyeDownloadRank)):

    if i!=len(DataEyeDownloadRank)-1:

        if DataEyeDownloadRank.NewTopNow[i]==DataEyeDownloadRank.NewTopNow[i+1]:
            continue

    SQL='insert into dc_DataEyeRank (RankType,GetTime,GameName,TopNow,iConURL,iConLocal) values ( '+`str(DataEyeDownloadRank.RankID[i])`+','+`str(DataEyeDownloadRank.GetTime[i])`+',"'+DataEyeDownloadRank.GameName[i]+'",'+`str(DataEyeDownloadRank.NewTopNow[i])`+',"'+DataEyeDownloadRank.iConURL[i]+'","'+DataEyeDownloadRank.iConLocal[i]+'") on duplicate key update TopNow=0'

    cursor.execute(SQL)
    con.commit()
    print 'Insert OK'


