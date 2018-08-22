#!/usr/bin/python
# -*- coding: utf-8 -*-
import pdfkit
    
url = "https://www.taobao.com/"

path_wk = r'D:\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wk)
    

pdfkit.from_url(url, r'D:\are you coding\pdf\taobao.pdf', configuration=config)