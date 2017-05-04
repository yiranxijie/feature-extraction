#!/usr/bin/env python
# coding=utf-8

#python 调用apktool批量解压apk文件
 
import os
 
 
path="E:/apk/test/" # this is apk files' store path

appPath = "E:/app_decompression_files/"	# this is apk decompression path

apklist = os.listdir(path) # get all the names of apps

for APK in apklist:
	portion = os.path.splitext(APK)
	appname=portion[0]
	filename=appname+portion[1]	# portion[1] is .apk
	print filename
	apktool_command = "cmd.exe /c apktool d -f " +path+filename+" -o "+appPath+appname
	os.system(apktool_command)
	
 
print "all work done!"