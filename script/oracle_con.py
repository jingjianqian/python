import cx_Oracle
conn = cx_Oracle.connect('system/orcl@127.0.0.1/orcl')
c = conn.cursor()
x = c.execute('select  sysdate from dual')
x.fetchone()
c.close();
conn.colse