#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 18-7-13
@Author  : leemiracle
"""
import tushare as ts
import sqlite3
import time


def excute_sql(sql):
    conn = sqlite3.connect('/home/lwz/project/chatBot/my_django/db.sqlite3')
    c = conn.cursor()
    result = c.execute(sql)
    conn.commit()
    conn.close()
    return result


def create_table():
    sql = '''CREATE TABLE if not exists stocks_{}
                 (code TEXT, name text, changepercent REAL, changepercent REAL, trade REAL, `open` REAL, high REAL, 
                 low  REAL, settlement REAL,  volume REAL, turnoverratio REAL, amount REAL, per REAL,  pb REAL, 
                 mktcap REAL, nmc REAL)'''.format()
    excute_sql(sql)


def process_stock_exchange_rate():
    # 代码，名称，涨跌幅，现价，开盘价，最高价，最低价，最日收盘价，成交量，换手率，成交额，市盈率，市净率，总市值，流通市值
    # code   name  changepercent   trade    open    high     low  settlement       volume  turnoverratio        amount      per       pb  mktcap  nmc
    while True:
        basic = ts.get_today_all()
        push = basic[(basic.turnoverratio > 0.3) & (basic.changepercent < 0.0)]
        print(push.code)
        break
        time.sleep(60)


def main():
    process_stock_exchange_rate()


if __name__ == '__main__':
    main()
