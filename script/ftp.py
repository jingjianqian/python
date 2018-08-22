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



#ftp_download()
#ftp_upload()
f.quit()