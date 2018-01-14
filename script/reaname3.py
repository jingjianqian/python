#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
filenameList = []
def gci(filepath,table):
	files = os.listdir(filepath)
	for obj in files:
		obj_path = os.path.join(filepath,obj)
		if os.path.isdir(obj_path):
			gci(obj_path,table)
		else:
			#os.rename(os.path.join(filepath,obj_path),os.path.join(filepath,obj_path.upper()))
			(shotname,extension) = os.path.splitext(obj)
			#print('shotname:'+shotname+" extension:"+extension)
			#if extension.
			if shotname.upper() in table:
				filenameList.append(shotname)
				shutil.copyfile(os.path.join(filepath,obj),os.path.join('H:\\work\\everyday\\have\\xzywyj',obj.upper()))
	return filenameList
#gci('H:\\work\\everyday\\2015-DQTEST')