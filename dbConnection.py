#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'cyf'

import mysql.connector
import pymysql

# 方式一  mysql-connector 是 MySQL 官方提供的驱动器
myDb = mysql.connector.connect( host="127.0.0.1",user="cyf",passwd="CYFtoo123")
myCursor = myDb.cursor()
selSql = " select * from adv.ad_rel "
myCursor.execute(selSql)
for x in myCursor:
    print(x)
myCursor.close()

# 方式二 python3.x常用的一种
db = pymysql.connect("127.0.0.1", "cyf", "CYFtoo123", "adv")
cursor = db.cursor()
cursor.execute(" select * from ad_game")
for y in cursor:
    print(y)
db.close()


