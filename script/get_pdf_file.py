#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
import random

def getPdfs(filepath):
	print('开始查找:'+filepath+' 下的pdf文件,准备好没有!?狗蛋')
	a = random.randint(1,1000)
	print(a)
	rootObjs = os.listdir(filepath)
	for rootObj in rootObjs:
		rootObjAbsPath = os.path.join(filepath,rootObj)
		if os.path.isdir(rootObjAbsPath):
			getPdfs(rootObjAbsPath)
		else:
			(shortname,extension) = os.path.splitext(rootObj)
			#print(extension.upper())
			if extension.upper() == '.PDF':
				pass
				#shutil.copyfile(os.path.join(filepath,rootObj),os.path.join('H:\\room\\py\\tool\\pdfs',rootObj.upper()))
				os.rename(os.path.join(filepath,rootObj),os.path.join(filepath,rootObj.upper()))
				#print(shortname+'.'+extension)
			else:
				try:

					rang_num1 = random.randint(1,1000)
					rang_num2 = random.randint(1,1000)
					rang_num3 = random.randint(1,1000)
					shutil.move(os.path.join(filepath,rootObj),os.path.join('X:\\notpdf\\1',rootObj))
				except Exception as e:
					rang_num = random.randint(1,1000)
					shutil.move(os.path.join(filepath,rootObj),os.path.join('X:\\notpdf\\1','1_'+str(rang_num)+rootObj))

getPdfs(u'X:\\search')
