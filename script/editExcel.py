#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import xlrd
from xlutils.copy import copy
import  shutil
from openpyxl import load_workbook

"""
rb = xlrd.open_workbook(u'E:\\room\\python\\fileForTest\\我去你大爷的.xlsx')    #打开我去你大爷.xls
wb = copy(rb)                          											#利用xlutils.copy下的copy函数复制
ws = wb.get_sheet(0)                   											#获取表单0
ws.write(0, 0, 'changed!')             											#改变（0,0）的值
ws.write(8,0,label = '好的')           											#增加（8,0）的值
wb.save(u'E:\\room\\python\\fileForTest\\我去你大爷的.xlsx')
"""
def gci(filepath):
	files = os.listdir(filepath)
	for obj in files:
		absPath = os.path.join(filepath,obj)
		if os.path.isdir(absPath):
			print(absPath)
			gci(absPath)
		else:
			#print("开始处理文件:"+absPath)
			(shotname,extension) = os.path.splitext(obj)
			if extension.lower()=='.xlsx' or extension.lower()=='.xls':
				print("开始处理文件:"+absPath)
				try:
					rb = xlrd.open_workbook(absPath)    									#打开我去你大爷.xls
					wb = copy(rb)          													#利用xlutils.copy下的copy函数复制
					ws = wb.get_sheet(0)
					ws = wb.get_sheet(1)
					try:
						ws = wb.get_sheet(2)
					except Exception as eeeeee:
						pass
					this_filename = os.path.split(absPath)[1]
					target_filename_aj = os.path.splitext(this_filename)[0] + '案卷'+os.path.splitext(this_filename)[1] #案卷文件名
					target_filename_jn = os.path.splitext(this_filename)[0] + '卷内'+os.path.splitext(this_filename)[1] #卷内文件名
					
					target_fullpath_aj = os.path.join(os.path.split(absPath)[0],target_filename_aj)							#案卷文件绝对路径
					target_fullpath_jn = os.path.join(os.path.split(absPath)[0],target_filename_jn)						  	#卷内文件绝对路径
					
					#如果有归档文件
					try:
						ws = wb.get_sheet(2)
						target_filename_gdwj = os.path.splitext(this_filename)[0] + '归档文件'+os.path.splitext(this_filename)[1] #归档文件名
						target_fullpath_gdwj = os.path.join(os.path.split(absPath)[0],target_filename_gdwj)						  #归档文件绝对路径
						#复制一个作为归档文件 删除案卷卷内
						if os.path.exists(target_fullpath_gdwj):
							files.remove(target_fullpath_gdwj)
							os.remove(target_fullpath_gdwj)
						else:
							pass
						shutil.copyfile(absPath,target_fullpath_gdwj)
						this_gdwj_wb = xlrd.open_workbook(target_fullpath_gdwj)
						this_gdwj_ws = copy(this_gdwj_wb)
						this_gdwj_ws._Workbook__worksheets = [this_gdwj_ws._Workbook__worksheets[2]]
						this_gdwj_ws.save(target_fullpath_gdwj);
					except Exception as eeeeee:	
						pass
					
					#复制一个作为案卷 删除卷内
					if os.path.exists(target_fullpath_aj):
						files.remove(target_filename_aj)
						
						os.remove(target_fullpath_aj)
					else:
						pass
					
					shutil.copyfile(absPath,target_fullpath_aj)					
					this_aj_wb = xlrd.open_workbook(target_fullpath_aj)
					
					this_aj_ws = copy(this_aj_wb)
					
					this_aj_ws._Workbook__worksheets = [this_aj_ws._Workbook__worksheets[0]]
					this_aj_ws.save(target_fullpath_aj);
					#复制一个作为案卷 删除案卷
					
					if os.path.exists(target_fullpath_jn):
						
						files.remove(target_filename_jn)
						os.remove(target_fullpath_jn)
					else:
						pass
					shutil.copyfile(absPath,target_fullpath_jn)
					this_jn_wb = xlrd.open_workbook(target_fullpath_jn)
					this_jn_ws = copy(this_jn_wb)
					this_jn_ws._Workbook__worksheets = [this_jn_ws._Workbook__worksheets[1]]
					this_jn_ws.save(target_fullpath_jn);
					"""
					target_filename_aj = os.path.join()
					target_filename_jn = os.path.splitext(this_filename)[0] + '-卷内'+os.path.splitext(this_filename)[1]
					#print(os.path.splitext(this_filename))
					#print(os.path.splitext(target_filename))
					#print(os.path.split(absPath)[0]+shotname+'-案卷'+extension)
					#复制一个作为案卷 删除卷内
					shutil.copyfile(this_filename,os.path.target_filename_aj)
					this_aj_wb = xlrd.open_workbook(target_filename_aj)
					this_aj_ws = copy(this_aj_wb)
					this_aj_ws.del_sheet(1)
					this_aj_ws.save(target_filename_aj)
					#复制一个作为案卷 删除案卷
					shutil.copyfile(this_filename,target_filename_aj)
					this_jn_wb = xlrd.open_workbook(target_filename_aj)
					this_jn_ws = copy(this_jn_wb)
					this_jn_ws.del_sheet(0)
					this_jn_ws.save(target_filename_aj)
					"""
				except Exception as e:
					print(e)
					print("文件:"+absPath+ "  待定")
			else:
				pass
				print("文件:"+absPath+ "  待定")
		#a = str(obj)
		#print(len(obj[0:obj.index('-')]))
		
		#if(len(obj[0:obj.index('-')])==2):
			#print(obj)
			#os.rename(os.path.join(filepath,obj),os.path.join(filepath,'0'+obj))
		#if(len(obj[0:obj.index('-')])==1):
			#os.rename(os.path.join(filepath,obj),os.path.join(filepath,'00'+obj))
		#os.rename(os.path.join(filepath,obj),os.path.join(filepath,'0'+obj))
	
#gci(u'E:\\room\\forTest')

gci(u'E:\\zx\\project\\清远市档案局\\data\\量子伟业（第三次） - 副本2')