# -*- coding:utf-8 -*-
import xdrlib,sys
import xlrd
from reaname3 import gci 

#open excel
def open_excel(file='C:\\Users\\jjq\\Desktop\\everyday\\everyday\\source.xlsx'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except Exception as e:
		print(str(e))

#根据sheet名返回内容
def excel_table_byname(file='C:\\Users\\jjq\\Desktop\\everyday\\everyday\\source.xlsx',colnameindex=0,by_name=u'Sheet2'):
	data = open_excel(file)#打开目标excel
	table = data.sheet_by_name(by_name)#根据sheet名获取excel中sheet
	nrows = table.nrows#sheet的行数
	colnames = table.row_values(colnameindex)
	list = []
	for rowrum in range(0,nrows):
		row = table.row_values(rowrum)
		if row:
			app = []
			for i in range(len(colnames)):
				list.append(row[i].upper())
			#list.append(app)
	return list

	
def main():
	table = excel_table_byname()
	fileList = gci(u'X:\\',table)
	print(fileList)
	#for row in table:
		#print(row)

		
if __name__=="__main__":
	main();