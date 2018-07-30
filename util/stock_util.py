#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 18-7-12
@Author  : leemiracle
"""
import math

import requests
import re
import os
import json

STOCK_CODE_PATH = "stock_codes.conf"


def update_stock_code():
    rep = requests.get('http://quote.eastmoney.com/stocklist.html')
    data = re.findall(r"<li>(.*?)</li>", rep.text)
    all_stock_codes = list()
    for s in data:
        # <a target="_blank" href="http://quote.eastmoney.com/sh201000.html">R003(201000)</a>
        # pa = s.partition('http://quote.eastmoney.com/')
        pa = s.split('http://quote.eastmoney.com/')
        # print(pa)
        if len(pa) == 2:
            p = pa[1].partition('.html')
            # print(p)
            if len(p[0].split('/')) == 1:
                all_stock_codes.append(p[0])
    with open("china_stock_code.json", 'w+') as f:
        f.write(json.dumps(dict(stock=all_stock_codes)))


def get_stock_codes(is_update=False):
    if is_update:
        update_stock_code()
    else:
        with open("china_stock_code.json", 'r+') as f:
            return json.loads(f)["stock"]


def stock_code_path():
    return os.path.join(os.path.dirname(__file__), STOCK_CODE_PATH)


def get_quarter(month):
    return math.ceil(int(month) / 3)


def main():
    '''
    实时股价查询：http://qt.gtimg.cn/q=sh900957,sh900956
    :return:
    '''
    ''
    # update_stock_code()
    import tushare as ts
    d = ts.get_hist_data('000063')
    basic = ts.get_today_all() #
    print(d)


if __name__ == '__main__':
    main()
