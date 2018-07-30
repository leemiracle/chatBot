#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取Alexa 信息：
    1.top-sites
    2.
@Time    : 18-7-11
@Author  : leemiracle
"""

import zipfile
import io
import requests

ALEXA_DATA_URL = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'


def alexa_etl():
    """
    Generator that:
        Extracts by downloading the csv.zip, unzipping.
        Transforms the data into python via CSV lib
        Loads it to the end user as a python list
    """

    rep = requests.get(ALEXA_DATA_URL, allow_redirects=True)
    # buf = StringIO(rep.content)
    buf = io.BytesIO(rep.content)
    zfile = zipfile.ZipFile(buf)
    buf = zfile.read('top-1m.csv')
    buf = buf.decode("utf-8").split("\n")
    for line in buf:
        if len(line.split(',')) != 2:
            break
        (rank, domain) = line.split(',')
        print(int(rank), domain.strip())
        yield (int(rank), domain.strip())


def top_list(num=100):
    a = alexa_etl()
    return [a.__next__() for x in range(num)]


def alexa_url_data(uri='court.gov.cn'):
    base_uri = 'http://data.alexa.com/data?cli=10&dat=s&url={uri}'.format(uri=uri)
    # bs4.BeautifulSoup(urllib.urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ sys.argv[1]).read(), "xml").find("REACH")['RANK']
    requests.get(base_uri)


def alexa_url_parse(uri='youtube.com'):
    '''
    alexa.com官网上的能看的到的信息都能取到
    :param uri:
    :return:
    '''
    base_uri = 'https://www.alexa.com/siteinfo/{uri}'.format(uri=uri)
    resp = requests.get(base_uri)
    with open(uri, 'w+') as f:
        f.write(resp.text)


def parse_alexa_html():
    '''
    全球排名:
    国家排名【各个国家的比例】
    访客参与度： Bounce Rate【跳出率：上升比】【每个访问者每日浏览量：】 【每天在网站花的时间】
    在搜索引擎上的关键字：
    上游网站【来源】

    网站外链【外链量】：
    :return:
    '''
    pass

def main():
    # for d in alexa_etl():
    #     print(d)
    alexa_url_parse()


if __name__ == '__main__':
    main()
