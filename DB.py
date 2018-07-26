#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @author: WuBingBing

import pymysql
import re
import config


# 数据库查询
def get_dbdata(sql):
    conn = pymysql.connect(host=config.HOST, port=3306, user='root', passwd='123456', db='mtbill',
                           charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()
    cur.close()
    conn.close()


def get_code():
    code = get_dbdata("SELECT smsParam FROM sms_record WHERE smsParam like '%code%' ORDER BY id DESC LIMIT 1;")
    return str((re.compile(r'\d+').findall(str(code)))[0])






