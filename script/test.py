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
def excel_table_byname(file='C:\\Users\\jjq\\Desktop\\everyday\\everyday\\source.xlsx',colnameindex=0,by_name=u'Sheet1'):
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
	str1 = '2009-DQ13-013-009'
	str2 = '2009-DQ13-013'
	table = excel_table_byname()
	s = '2009-DQ13-013-009'
	for i in table:
		print(i)
		try:
			str(s).index(str(i))
			print('12323:'+s)
		except Exception as e:
			pass
			#print(str(e))
	
if __name__=="__main__":
	main();