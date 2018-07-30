#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 18-7-12
@Author  : leemiracle
"""

import re
import requests


class Boc(object):
    """中行美元最新汇率"""

    url = "http://www.boc.cn/sourcedb/whpj/"

    def get_exchange_rate(self, currency="usa"):
        rep = requests.get(self.url)
        data = re.findall(r"<td>(.*?)</td>", rep.text)

        if currency == "usa":
            return {"sell": data[-13], "buy": data[-15]}


def main():
    b = Boc()
    print(b.get_exchange_rate())


if __name__ == '__main__':
    main()
