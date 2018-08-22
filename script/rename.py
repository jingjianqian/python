#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
def gci(filepath):
	print('开始重命名。。。。。。。。。。。。')
	files = os.listdir(filepath)
	for obj in files:
		#a = str(obj)
		#print(len(obj[0:obj.index('-')]))
		if(len(obj[0:obj.index('-')])==2):
			print(obj)
			os.rename(os.path.join(filepath,obj),os.path.join(filepath,'0'+obj))
		if(len(obj[0:obj.index('-')])==1):
			os.rename(os.path.join(filepath,obj),os.path.join(filepath,'00'+obj))
		#os.rename(os.path.join(filepath,obj),os.path.join(filepath,'0'+obj))
#gci(u'E:\\room\\forTest')
gci(u'Y:\\泰坦移交20150524\\泰坦数据\\chuli\\success3\\2')