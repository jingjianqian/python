#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import xlrd
from xlutils.copy import copy
import  shutil
from openpyxl import load_workbook



rb = xlrd.open_workbook(u'Z:\\量子移交\\cs\\目录\\1\\1清远市委办公室-卷内.xlsx')    #打开我去你大爷.xls
wb = copy(rb)                         											#利用xlutils.copy下的copy函数复制

wb._Workbook__worksheets = [wb._Workbook__worksheets[0]]

#获取表单0
wb.save(u'Z:\\量子移交\\cs\\目录\\1\\1清远市委办公室-卷内.xlsx')
