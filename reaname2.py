#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
def gci(filepath):
	files = os.listdir(filepath)
	for obj in files:
		obj_path = os.path.join(filepath,obj)
		if os.path.isdir(obj_path):
			gci(obj_path)
			print('dir:'+obj_path)
		else:
			os.rename(os.path.join(filepath,obj_path),os.path.join(filepath,obj_path.upper()))
			print(os.path.join(filepath,obj_path)+'===>'+obj_path.upper())
gci('X:\\原文\\陈老师\\2013')