#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 18-7-12
@Author  : leemiracle
"""
import datetime
import math
import re
import sys
import json
import time
from pyquery import PyQuery

sys.path.append('.')
sys.path.append('..')

from stock_api.base import BaseQuotation
from util import stock_util
import requests


class Sina(BaseQuotation):
    max_num = 800
    grep_detail = re.compile(
        r"(\d+)=([^\s][^,]+?)%s%s" % (r",([\.\d]+)" * 29, r",([-\.\d:]+)" * 2)
    )
    grep_detail_with_prefix = re.compile(
        r"(\w{2}\d+)=([^\s][^,]+?)%s%s"
        % (r",([\.\d]+)" * 29, r",([-\.\d:]+)" * 2)
    )
    stock_api = "http://hq.sinajs.cn/?format=text&list="

    def format_response_data(self, rep_data, prefix=False):
        stocks_detail = "".join(rep_data)
        grep_str = self.grep_detail_with_prefix if prefix else self.grep_detail
        result = grep_str.finditer(stocks_detail)
        stock_dict = dict()
        for stock_match_object in result:
            stock = stock_match_object.groups()
            stock_dict[stock[0]] = dict(
                code=stock[0],
                name=stock[1],
                open=float(stock[2]),
                close=float(stock[3]),
                now=float(stock[4]),
                high=float(stock[5]),
                low=float(stock[6]),
                buy=float(stock[7]),
                sell=float(stock[8]),
                turnover=int(stock[9]),
                volume=float(stock[10]),
                bid1_volume=int(stock[11]),
                bid1=float(stock[12]),
                bid2_volume=int(stock[13]),
                bid2=float(stock[14]),
                bid3_volume=int(stock[15]),
                bid3=float(stock[16]),
                bid4_volume=int(stock[17]),
                bid4=float(stock[18]),
                bid5_volume=int(stock[19]),
                bid5=float(stock[20]),
                ask1_volume=int(stock[21]),
                ask1=float(stock[22]),
                ask2_volume=int(stock[23]),
                ask2=float(stock[24]),
                ask3_volume=int(stock[25]),
                ask3=float(stock[26]),
                ask4_volume=int(stock[27]),
                ask4=float(stock[28]),
                ask5_volume=int(stock[29]),
                ask5=float(stock[30]),
                date=stock[31],
                time=stock[32],
            )
        return stock_dict


class Day:
    # 历史复权信息，成交数据：需要像js那样动态请求各季度的数据
    SINA_API = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/stockid/{stock_code}.phtml'
    SINA_API_HOSTNAME = 'vip.stock.finance.sina.com.cn'
    STOCK_CODE_API = 'http://218.244.146.57/static/all.csv'

    def __init__(self, path='history', export='csv'):
        # self.store = store.use(export=export, path=path, dtype='D')
        pass

    def init(self):
        # stock_codes = self.store.init_stock_codes
        pass

    def init_stock_history(self, stock_code):
        all_history = self.get_all_history(stock_code)
        if len(all_history) <= 0:
            return
        # self.store.write(stock_code, all_history)

    def get_all_history(self, stock_code):
        years = self.get_stock_time(stock_code)
        all_history = []
        for year in years:
            year_history = self.get_year_history(stock_code, year)
            all_history += year_history
        all_history.sort(key=lambda day: day[0])
        return all_history

    def get_year_history(self, stock_code, year):
        year_history = []
        now_year = datetime.datetime.now().year
        now_month = datetime.datetime.now().month
        end_quarter = 5 if str(year) != str(now_year) else math.ceil(now_month / 3) + 1
        for quarter in range(1, end_quarter):
            quarter_data = self.get_quarter_history(stock_code, year, quarter)
            if quarter_data is None:
                continue
            year_history += quarter_data
        return year_history

    def get_stock_time(self, stock_code):
        # 获取年月日
        url = self.SINA_API.format(stock_code=stock_code)
        try:
            dom = PyQuery(url)
        except requests.ConnectionError:
            return []
        year_options = dom('select[name=year] option')
        years = [o.text for o in year_options][::-1]
        return years

    def get_quarter_history(self, stock_code, year, quarter):
        year = int(year)
        if year < 1990:
            return list()
        params = dict(
            year=year,
            jidu=quarter
        )
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        print('request {},{},{}'.format(stock_code, year, quarter))
        url = self.SINA_API.format(stock_code=stock_code)
        rep = list()
        loop_nums = 10
        for i in range(loop_nums):
            try:
                rep = requests.get(url, params, timeout=3, headers=headers)
                break
            except requests.ConnectionError:
                time.sleep(60)
            except Exception as e:
                with open('error.log', 'a+') as f:
                    f.write(str(e))

        print('end request {}, {}, {}'.format(stock_code, year, quarter))
        if rep is None:
            with open('error.txt', 'a+') as f:
                f.write('{},{},{}'.format(stock_code, year, quarter))
            return list()
        res = self.handle_quarter_history(rep.text)
        return res

    def handle_quarter_history(self, rep_html):
        dom = PyQuery(rep_html)
        raw_trows = dom('#FundHoldSharesTable tr')
        empty_history_nodes = 2
        if len(raw_trows) <= empty_history_nodes:
            return list()

        unused_head_index_end = 2
        trows = raw_trows[unused_head_index_end:]

        res = list()
        for row_td_list in trows:
            td_list = row_td_list.getchildren()
            day_history = []
            for i, td in enumerate(td_list):
                td_content = td.text_content()
                date_index = 0
                if i == date_index:
                    td_content = re.sub(r'\r|\n|\t', '', td_content)
                day_history.append(td_content)
            self.convert_stock_data_type(day_history)
            res.append(day_history)
        return res

    def convert_stock_data_type(self, day_data):
        """将获取的对应日期股票数据除了日期之外，转换为正确的 float / int 类型
        :param day_data: ['2016-02-19', '945.019', '949.701', '940.336', '935.653', '31889824.000', '320939648.000', '93.659']
        :return: ['2016-02-19', 945.019, 949.701, 940.336, 935.653, 31889824.000, 320939648.000, 93.659]
        """
        date_index = 0
        for i, val in enumerate(day_data):
            if i == date_index:
                continue
            day_data[i] = float(val)


def stock_history_test():
    d = Day()
    ping_an = '000001'
    d.init_stock_history(ping_an)
    all_history = d.get_all_history(ping_an)
    print(all_history)


def stock_codes_realtime_test():
    s = Sina()
    all_market = s.all_market
    stock_data = []
    for i, d in enumerate(all_market):
        print(i, d, all_market[d])
        stock_data.append(json.dumps(all_market[d]))
    with open('stock_data.txt', 'w+') as f:
        f.write("\n".join(stock_data))


def main():
    stock_history_test()


if __name__ == '__main__':
    main()
