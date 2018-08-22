#!/usr/bin/python
# -*- coding: utf-8 -*-
import ftplib

host = '127.0.0.1'
username = '10086'
password = 'axiba'
file = '1.txt'


f = ftplib.FTP(host)  # 
f.login(username, password)  # 

# 
pwd_path = f.pwd()
print(u'我们:', pwd_path)

def ftp_upload():
    '''上传测试！'''
    file_remote = u'只给我.pdf'
    file_local = u'E:\\zx\\test\\uploadTest'
    bufsize = 1024
    fp = open(file_local, 'rb')
    f.storbinary('STOR ' + file_remote, fp, bufsize)
    fp.close()



#ftp_download()
ftp_upload()
f.quit()