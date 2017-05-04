#!/usr/bin/env python
# coding=utf-8

# 批量解析 .xml文件
 
import os
import xml.sax
 
 
path="E:/app_decompression_files/" # this is apk decompression path

xmllist = os.listdir(path) # get all the names of apps

for apkfolder in xmllist:
	portion = os.path.splitext(apkfolder)
	foldername=portion[0]
	xmlpath=path+foldername+"/AndroidManifest.xml"
	print xmlpath