#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
filenameList = []
f = open(u'H:\\work\\everyday\\h\\dq.log','w');
def gci(filepath,table):
	files = os.listdir(filepath)
	for obj in files:
		print(os.path.join(filepath,obj))
		print(os.path.join(filepath,obj),file=f)
		obj_path = os.path.join(filepath,obj)
		if os.path.isdir(obj_path):
			if obj.upper() in table:
				print('开始复制文件夹:'+os.path.join(obj_path,obj),file=f)
				shutil.copytree(os.path.join(obj_path,obj),os.path.join('H:\\work\\everyday\\h\\dir\\dq',obj.upper()))
			else:
				gci(obj_path,table)
		else:
			(shotname,extension) = os.path.splitext(obj)
			#print('shotname:'+shotname+" extension:"+extension)
			#if extension.
			if shotname.upper() in table:
				filenameList.append(shotname)
				print('开始复制文件:'+os.path.join(filepath,obj),file=f)
				shutil.copyfile(os.path.join(filepath,obj),os.path.join('H:\\work\\everyday\\h\\dq',obj.upper()))
	return filenameList
#gci('H:\\work\\everyday\\2015-DQTEST')