#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
baseFile = u'E:\\zx\\test\\fileTest\\dataTEest\\1success\\105-A12.2-0041-006\\105-A12.2-0039-024-001.pdf'

def gci(filepath):
	files = os.listdir(filepath)
	for index, obj in enumerate(files):
		obj_path = os.path.join(filepath,obj)
		if os.path.isdir(obj_path):
			#shutil.copyfile(baseFile,os.path.join(obj_path,"001.pdf"))
			gci(obj_path)
		else:
			(shotname,extension) = os.path.splitext(obj)
			
			obj_path_father = obj_path[1:obj_path.rfind("\\")]
			
			target_file_name = obj_path_father[obj_path_father.rfind("\\")+1:len(obj_path_father)]
			
			os.rename(os.path.join(filepath,obj),os.path.join(filepath,target_file_name+'-'+(str(index+1)).zfill(2)+extension))
			#print(os.path.join(filepath,shotname+str(index)+extension))
			#print(obj_path[int(obj_path.rfind("\\")),int(len(obj_path))])
			#os.rename(os.path.join(filepath,obj),os.path.join(filepath,shotname+str(index)+extension))
#def rename_file(filePath):
#	files = os.listdir()
	
gci(u'E:\\zx\\test\\fileTest\\dataTEest\\')