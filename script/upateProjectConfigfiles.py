#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


lszwBasePath = 'D:\code\java\LSZWFW'
servicesModules = ['platform-service','system-service','web-service']

platFormSerivceBasePath = 'D:\code\java\LSZWFW\platform-service'
platFormServiceServices = ['platform-approve','platform-auth','platform-charge','platform-demo','platform-flow','platform-flow','platform-form','platform-interfaces','platform-job','platform-lszw','platform-system']

systemServiceBasePath = 'D:\code\java\LSZWFW\system-service'
systemServiceServices = ['system-config','system-eureka','system-zuul']

webServiceBasePath = 'D:\code\java\LSZWFW\web-service'
webServiceServices = ['platform-api','platform-inner-web','platform-wxapp']


#修改平台模块配置文件
def updatePlatFormServiceConfig():
    global platFormSerivceBasePath,platFormServiceServices
    for platFormService in platFormServiceServices:
        tempPath =  os.path.join(os.path.join(platFormSerivceBasePath,platFormService),'src\\main\\resources\\bootstrap.properties')
        #platFormSerivceBasePath + '/' + platFormService + 'src/main/resources/bootstrap.properties'
        file_data = ''
        with open(tempPath,'r',encoding='utf-8') as f:
            for line in f:
                if '127.0.0.1\:7001' in line:
                    line = line.replace('127.0.0.1\:7001', 'system-eureka\:7001')
                file_data += line
        with open(tempPath,'w',encoding='utf-8') as f:
            f.write(file_data)
       

#修改服务模块配置文件
def updateSystemServiceConfig():
    global systemServiceBasePath,systemServiceServices
    for systemServcie in systemServiceServices:
        tempPath =  os.path.join(os.path.join(systemServiceBasePath,systemServcie),'src\\main\\resources\\application.properties')
        file_data = ''
        with open(tempPath,'r',encoding='utf-8') as f:
            for line in f:
                if '127.0.0.1\:7001' in line:
                    line = line.replace('127.0.0.1\:7001', 'system-eureka\:7001')
                file_data += line
        with open(tempPath,'w',encoding='utf-8') as f:
            f.write(file_data)

#修改web服务模块配置
def updateWebServiceConfig():
    global webServiceBasePath,webServiceServices
    for webServcie in webServiceServices:
        tempPath =  os.path.join(os.path.join(webServiceBasePath,webServcie),'src\\main\\resources\\bootstrap.properties')
        file_data = ''
        with open(tempPath,'r',encoding='utf-8') as f:
            for line in f:
                if '127.0.0.1\:7001' in line:
                    line = line.replace('127.0.0.1\:7001', 'system-eureka\:7001')
                file_data += line
        with open(tempPath,'w',encoding='utf-8') as f:
            f.write(file_data)
    pass

# def updateAllConfig():


updatePlatFormServiceConfig()
updateSystemServiceConfig()
updateWebServiceConfig()
