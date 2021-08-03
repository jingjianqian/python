import threading
from queue import Queue
import requests
from lxml import etree
from Utils import DBUtils

details_queue = Queue()


# 查询100条数据
def updateDetails(queue):
    db_conn = DBUtils.conn_mysql()
    cursor = db_conn.cursor()
    select_sql = 'select *  from hot_record_temp t where t.href is not null and t.hot_details is null limit 100'
    result = cursor.execute(select_sql)
    if result > 0:
        pass
    else:
        return None
    result_arry = []

    for line in cursor.fetchall():
        temp_arry = list(line)
        result_arry.append(temp_arry)
    return result_arry


# 获取明细 每次 clows条目
def getHotDetails(hot_item_arry):
    pass


# 获取热搜详情
def getHtml(href):
    base_url = 'https://s.weibo.com'
    target_href = base_url + href
    print(target_href)
    r = requests.get(target_href)
    print(1111, r.text)
    target_href_lxml = etree.HTML(r.text)
    print(target_href_lxml)
    return target_href_lxml


def deal_hot_detail(queue):
    result = updateDetails(queue)
    update_sql = 'update hot_record_temp t set t.hot_details =%s where t.id =%s'
    sql_match_data = []
    if result is not None:
        for result_line in result:
            sql_match_data.append([getHtml(result_line[6]), result_line[0]])
    else:
        print("处理完成！")

    return
    db_conn = DBUtils.conn_mysql()
    cursor = db_conn.cursor()
    update_count = cursor.executemany(update_sql, sql_match_data)
    db_conn.commit()
    print(update_count)


# main入口方法
if __name__ == '__main__':
    getRecord_thread0 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    # getRecord_thread1 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    # getRecord_thread2 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    # getRecord_thread3 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    # getRecord_thread4 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    # getRecord_thread5 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    # getRecord_thread6 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    # getRecord_thread7 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    # getRecord_thread8 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    # getRecord_thread9 = threading.Thread(target=deal_hot_detail, args=(Queue,))
    getRecord_thread0.start()
    # getRecord_thread1.start()
    # getRecord_thread2.start()
    # getRecord_thread3.start()
    # getRecord_thread4.start()
    # getRecord_thread5.start()
    # getRecord_thread6.start()
    # getRecord_thread7.start()
    # getRecord_thread8.start()
    # getRecord_thread9.start()
    pass
