#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import MySQLdb
import MySQLdb.cursors
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')

con=MySQLdb.connect(host="127.0.0.1",port=3307,user="root",passwd="",db="de_rank",charset="utf8")
cursor=con.cursor()

deleteTime=int(time.mktime(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S')))-1296000
deleteDate=str(time.strftime("%Y-%m-%d", time.localtime(deleteTime))+' 00:00:00')

sql =  "delete from dc_rank where GetTime < '%s'"%(deleteDate)
print sql
cursor.execute(sql)
con.commit()
con.close()
