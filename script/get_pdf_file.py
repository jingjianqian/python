#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
import random

def getPdfs(filepath):
	print('开始查找:'+filepath+' 下的pdf文件,准备好没有!?狗蛋')
	rootObjs = os.listdir(filepath)
	for rootObj in rootObjs:
		rootObjAbsPath = os.path.join(filepath,rootObj)
		if os.path.isdir(rootObjAbsPath):
			getPdfs(rootObjAbsPath)
		else:
			(shortname,extension) = os.path.splitext(rootObj)
			#print(extension.upper())
			if extension.upper() == '.PDF':
				#shutil.copyfile(os.path.join(filepath,rootObj),os.path.join('H:\\room\\py\\tool\\pdfs',rootObj.upper()))
				os.rename(os.path.join(filepath,rootObj),os.path.join(filepath,rootObj.upper()))
				print(os.path.join(filepath,rootObj)+'------->'+rootObj.upper())
				#print(shortname+'.'+extension)
			else:
				try:
					os.remove(os.path.join(filepath,rootObj))
					#shutil.move(os.path.join(filepath,rootObj),os.path.join('X:\\notpdf\\1',rootObj))
					print('delete:'+os.path.join(filepath,rootObj))
				except Exception as e:
					pass
					#os.remove(os.path.join(filepath,rootObj))
					#rang_num = random.randint(1,1000)
					#shutil.move(os.path.join(filepath,rootObj),os.path.join('X:\\notpdf\\1','1_'+str(rang_num)+rootObj))
					#print('move:'+os.path.join(filepath,rootObj))

print('start.....')
getPdfs(u'X:\\search\\原文2013以后\\jx')
