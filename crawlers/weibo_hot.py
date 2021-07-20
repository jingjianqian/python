import configparser
import os

import requests
from bs4 import BeautifulSoup
import pymysql
from lxml import etree
import time

from lxml.html import tostring
from pyasn1.compat.octets import null

"""固定常量"""
CONST_BASE_URL = 'https://s.weibo.com/top/summary?cate=realtimehot'
CONST_TIME = 60
CONST_ROOT_DIR = os.path.dirname(os.path.abspath('.'))


def init_db_message():
    cf = configparser.ConfigParser()
    cf.read(CONST_ROOT_DIR + '/config.ini')


def parse_weibo_hot(_url):
    r = requests.get(_url, 'lxml')
    soup = BeautifulSoup(r.text, 'lxml')
    table_soup = soup.select('table')
    return table_soup


def parse_from_github(_url):
    r = requests.get(_url)
    table_lxml = etree.HTML(r.text)
    titles = table_lxml.xpath('//tr[position()>1]/td[@class="td-02"]/a[not(contains(@href, "javascript:void('
                              '0);"))]/text()')
    titles = [title.strip() for title in titles]
    hots = table_lxml.xpath('//tr[position()>1]/td[@class="td-02"]/a[not(contains(@href, "javascript:void('
                            '0);"))]/../span/text()')
    hots = [int(hot.strip()) for hot in hots]
    hottie = []
    hottie_lxml = table_lxml.xpath('//tr[position()>1]/td[@class="td-03"]')
    for k in hottie_lxml:
        print(k.xpath('./i/text()'))


# def parse_webo_hot_lxml_2(_url):
#     r = requests.get(_url)
#     table_lxml = etree.HTML(r.text)
#     index = table_lxml.xpath("//table/tbody/tr[position()>1]/td[@class='td-01 ranktop']/text()")
#     title = table_lxml.xpath("//table/tbody/tr[position()>1]/td[@class='td-02']/a/text()")
#     hits = table_lxml.xpath("//table/tbody/tr[position()>1]/td[@class='td-02']/span/text()")
#     table_lxml.xpath("//table/tbody/tr[position()>1]/td[@class='td-03']")


# lxml解析html方法
def parse_weibo_hot_lxml(_url):
    r = requests.get(_url)
    table_lxml = etree.HTML(r.text)
    table_tr = table_lxml.xpath('//table/tbody/tr[position()>1]')
    indexArr = []
    title = []
    hits = []
    hotType = []
    for trs in table_tr:
        indexArr.append(trs.xpath('./td[@class="td-01 ranktop"]/text()')[0])
        title.append(trs.xpath('./td[@class="td-02"]/a/text()')[0])
        temp_hit = trs.xpath('./td[@class="td-02"]/span/text()')
        if len(temp_hit) > 0:
            hits.append(temp_hit[0])
        else:
            hits.append('0')
        temp_hotType = trs.xpath('./td[@class="td-03"]/i/text()')
        # print(temp_hotType)
        if len(temp_hotType) > 0:
            hotType.append(temp_hotType[0])
        else:
            hotType.append('0')

    # print(len(indexArr))
    # print(len(title))
    # print(len(hits))
    # print(len(hotType))
    # print(indexArr)
    # print(title)
    # print(hits)
    # print(hotType)
    return [indexArr, title, hits, hotType]


def conn_mysql():
    cf = configparser.ConfigParser()
    cf.read(CONST_ROOT_DIR + '/config.ini')
    r_db_message = pymysql.connect(host=cf.get('mysql', 'host'), port=int(cf.get('mysql', 'port')),
                                   user=cf.get('mysql', 'user'), passwd=cf.get('mysql', 'passwd'),
                                   db=cf.get('mysql', 'db'), charset=cf.get('mysql', 'charset'))
    return r_db_message


"""定时任务"""
while True:
    data = parse_weibo_hot_lxml(CONST_BASE_URL)
    print(data)
    db_conn = conn_mysql()
    cursor = db_conn.cursor()
    insert_sql = 'insert hot_record_01(temp_index,title,hit,type,date) values (%s, %s, %s, %s, now())'
    try:
        for i in range(0, len(data[0])):
            cursor.execute(insert_sql, (data[0][i], data[1][i], data[2][i], data[3][i]))
        db_conn.commit()
    except Exception as e:
        print("插入失败")
        print(e)
        db_conn.rollback()
    finally:
        db_conn.close()
    time.sleep(60)
