#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
filenameList = []
f = open(u'H:\\work\\everyday\\h\\dq.log','w');
def gci(filepath,table):
	print('开始查找文件。。。。。。。。。。。。')
	files = os.listdir(filepath)
	for obj in files:
		#print(os.path.join(filepath,obj))
		print(os.path.join(filepath,obj),file=f)
		obj_path = os.path.join(filepath,obj)
		if os.path.isdir(obj_path):
			print(obj.upper(),file=f)
			if obj.upper() in table:
				print('开始复制文件夹:'+os.path.join(obj_path,''),file=f)
				shutil.copytree(os.path.join(obj_path,''),os.path.join('H:\\work\\everyday\\h\\dir\\jx',obj.upper()))
			else:
				gci(obj_path,table)
		else:
			(shotname,extension) = os.path.splitext(obj)
			for i in table:
				try:
					str(shotname.upper()).index(str(i.upper))
					filenameList.append(shotname)
					print('开始复制文件:'+os.path.join(filepath,obj),file=f)
					shutil.copyfile(os.path.join(filepath,obj),os.path.join('H:\\work\\everyday\\h\\jx',obj.upper()))
				except Exception as e:
					pass
	return filenameList
#gci('H:\\work\\everyday\\2015-DQTEST')