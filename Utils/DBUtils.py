import pymysql

from Utils import MyUtils


# 连接mysql
def conn_mysql():
    cf = MyUtils.getPro("config")
    r_db_message = pymysql.connect(host=cf.get('mysql', 'host'), port=int(cf.get('mysql', 'port')),
                                   user=cf.get('mysql', 'user'), passwd=cf.get('mysql', 'passwd'),
                                   db=cf.get('mysql', 'db'), charset=cf.get('mysql', 'charset'))
    return r_db_message


# 关闭数据库连接
def dis_connect_mysql(connect):
    connect.close()
