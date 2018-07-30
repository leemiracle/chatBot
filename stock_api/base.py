#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 18-7-12
@Author  : leemiracle
"""
import json
import warnings
from multiprocessing.pool import ThreadPool
import requests
from util import stock, stock_util

STOCK_TERM = dict(
    code='股票代码',
    name='股票名称',
    open='开盘',
    close='昨收',
    now='现价',
    high='最高',
    low='最低',
    buy='买家叫价',
    sell='卖家叫价',
    turnover='成交量',
    volume='成交额',
    bid1_volume='买1',
    bid1='买1价',
    bid2_volume='买2',
    bid2='买2价',
    bid3_volume='买3',
    bid3='买3价',
    bid4_volume='买4',
    bid4='买4价',
    bid5_volume='买5',
    bid5='买5价',
    ask1_volume='卖1',
    ask1='卖1价',
    ask2_volume='卖2',
    ask2='卖2价',
    ask3_volume='卖3',
    ask3='卖3价',
    ask4_volume='卖4',
    ask4='卖4价',
    ask5_volume='卖5',
    ask5='卖5价',
    date='日期',
    time='时间',
)


class BaseQuotation(object):
    """
    行情获取基类
    向后复权价格 = 原始价格 * 复权因子
    前复权：
        找到最大的复权因子
        将复权因子除以最新复权因子，得到“前复权因子”
        将计算日收盘价乘以“前复权因子”即得到向前复权价格
    股票复权因子=[股权登记日收盘价*（1 每股派红股 每股公积金转增 每股配股）]/(股权登记日收盘价-每股派现 每股配股*配股价格)

    买盘： 表示以比市价高的价格进行委托买入，并已经“主动成交” ，代表 外盘（以卖一价向上成交）
    “卖盘”：表示以比 买一价 低的价格进行委托卖出，并已经“主动成交”，代表 内盘（以买一价向下成交）
        内盘大于外盘：卖方实力强
        外盘 大于 内盘： 买方实力强

    重要指标：
    量比=（现成交总手数 / 现累计开市时间(分) ）/ 过去5日平均每分钟成交量   【市场活跃度】
        0.8-1.5倍，则说明成交量处于正常水平
        1.5-2.5倍之间则为温和放量：股价也处于温和缓升状态【升势相对健康，可继续持股】, 股价下跌【从量的方面判断应可考虑停损退出】
        2.5-5倍：明显放量【突破有效的几率高】
        5-10倍：剧烈放量【长期低位出现剧烈放量突破，涨势的后续空间巨大】【高位，则出逃】
        10倍以上：反向操作

        0.5倍以下：缩量情形【庄家长期控盘程度很高】
        小于1：开盘即封涨停的
    市盈率： 市价/每股盈利（Earnings Per Share： 过去一年的净利润/总发行已售出股数）【股票是便宜抑或昂贵的指标】
    换手率： 成交量/流通股本×100%  一定时间内市场中股票转手买卖的频率，
    """

    max_num = 800  # 每次请求的最大股票数
    stock_api = ""  # 股票 api

    def __init__(self):
        self._session = requests.session()
        stock_codes = self.load_stock_codes()
        self.stock_list = self.gen_stock_list(stock_codes)

    def gen_stock_list(self, stock_codes):
        stock_with_exchange_list = self._gen_stock_prefix(stock_codes)

        if self.max_num > len(stock_with_exchange_list):
            request_list = ",".join(stock_with_exchange_list)
            return [request_list]

        stock_list = []
        request_num = len(stock_codes) // (self.max_num + 1) + 1
        for range_start in range(request_num):
            num_start = self.max_num * range_start
            num_end = self.max_num * (range_start + 1)
            request_list = ",".join(
                stock_with_exchange_list[num_start:num_end]
            )
            stock_list.append(request_list)
        return stock_list

    def _gen_stock_prefix(self, stock_codes):
        return [
            stock.get_stock_type(code) + code[-6:]
            for code in stock_codes
        ]

    @staticmethod
    def load_stock_codes():
        with open(stock_util.stock_code_path()) as f:
            return json.load(f)["stock"]

    @property
    def all(self):
        warnings.warn("use market_snapshot instead", DeprecationWarning)
        return self.get_stock_data(self.stock_list)

    @property
    def all_market(self):
        """return quotation with stock_code prefix key"""
        return self.get_stock_data(self.stock_list, prefix=True)

    def stocks(self, stock_codes, prefix=False):
        return self.real(stock_codes, prefix)

    def real(self, stock_codes, prefix=False):
        """return specific stocks real quotation
        :param stock_codes: stock code or list of stock code, when prefix is True, stock code must start with sh/sz
        :param prefix: if prefix is True, stock_codes must contain sh/sz market flag.
            If prefix is False, index quotation can't return
        :return quotation dict, key is stock_code, value is real quotation.
            If prefix with True, key start with sh/sz market flag
        """
        if type(stock_codes) is not list:
            stock_codes = [stock_codes]

        stock_list = self.gen_stock_list(stock_codes)
        return self.get_stock_data(stock_list, prefix=prefix)

    def market_snapshot(self, prefix=False):
        """return all market quotation snapshot
        :param prefix: if prefix is True, return quotation dict's  stock_code key start with sh/sz market flag
        """
        return self.get_stock_data(self.stock_list, prefix=prefix)

    def get_stocks_by_range(self, params):
        headers = {
            "Accept-Encoding": "gzip, deflate, sdch",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36",
        }

        r = self._session.get(self.stock_api + params, headers=headers)
        return r.text

    def get_stock_data(self, stock_list, **kwargs):
        """获取并格式化股票信息"""
        res = self._fetch_stock_data(stock_list)
        return self.format_response_data(res, **kwargs)

    def _fetch_stock_data(self, stock_list):
        """获取股票信息"""
        pool = ThreadPool(len(stock_list))
        try:
            res = pool.map(self.get_stocks_by_range, stock_list)
        finally:
            pool.close()
        return [d for d in res if d is not None]

    def format_response_data(self, rep_data, **kwargs):
        pass


def main():
    BaseQuotation()


if __name__ == '__main__':
    main()
